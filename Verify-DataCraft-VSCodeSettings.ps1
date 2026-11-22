[CmdletBinding()]
param(
    [string]$RepositoryRoot = (Get-Location).Path,
    [string]$VSCodeProfile = 'DataCraft Development',
    [switch]$IncludeAllWorkspaceSettings,
    [switch]$FailOnUnknown
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Test-JsonFile {
    param([Parameter(Mandatory)][string]$Path)

    try {
        $null = Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
        return $true
    }
    catch {
        Write-Error "Invalid JSON: $Path`n$($_.Exception.Message)"
        return $false
    }
}

function Get-ConfigurationPropertiesFromManifest {
    param([Parameter(Mandatory)][string]$PackageJson)

    $manifest = Get-Content -LiteralPath $PackageJson -Raw -Encoding UTF8 | ConvertFrom-Json
    $properties = @{}
    $configuration = $manifest.contributes.configuration

    if ($null -eq $configuration) {
        return $properties
    }

    $sections = if ($configuration -is [System.Array]) {
        @($configuration)
    }
    else {
        @($configuration)
    }

    foreach ($section in $sections) {
        if ($null -eq $section.properties) { continue }

        foreach ($property in $section.properties.PSObject.Properties) {
            # Some settings do not declare scope or type. Under StrictMode,
            # reading a missing property throws and used to discard the
            # complete Copilot manifest. Read optional fields safely.
            $scopeProperty = $property.Value.PSObject.Properties['scope']
            $typeProperty = $property.Value.PSObject.Properties['type']

            $scopeValue = if ($null -ne $scopeProperty) {
                [string]$scopeProperty.Value
            }
            else {
                ''
            }

            $typeValue = if ($null -ne $typeProperty) {
                if ($typeProperty.Value -is [System.Array]) {
                    ($typeProperty.Value -join '|')
                }
                else {
                    [string]$typeProperty.Value
                }
            }
            else {
                ''
            }

            $properties[$property.Name] = [PSCustomObject]@{
                Extension = "$($manifest.publisher).$($manifest.name)"
                Version   = [string]$manifest.version
                Setting   = $property.Name
                Scope     = $scopeValue
                Type      = $typeValue
                Manifest  = $PackageJson
            }
        }
    }

    return $properties
}

function Get-VSCodeExtensionManifestPaths {
    param([string]$ProfileName)

    $manifests = New-Object System.Collections.Generic.List[string]

    # 1. Extensions utilisateur classiques.
    $userRoots = @(
        (Join-Path $env:USERPROFILE '.vscode\extensions'),
        (Join-Path $env:USERPROFILE '.vscode-insiders\extensions')
    ) | Where-Object { $_ -and (Test-Path $_) }

    foreach ($root in $userRoots) {
        Get-ChildItem -LiteralPath $root -Directory -ErrorAction SilentlyContinue |
            ForEach-Object {
                $candidate = Join-Path $_.FullName 'package.json'
                if (Test-Path $candidate) {
                    $manifests.Add($candidate)
                }
            }
    }

    # 2. Copilot Chat peut etre integre a VS Code au lieu d'etre sous ~/.vscode/extensions.
    #    On demande donc directement a la CLI de VS Code son emplacement reel.
    try {
        $located = @(
            & code --locate-extension github.copilot-chat --profile $ProfileName 2>$null
        ) | Where-Object { $_ -and $_.Trim() }

        foreach ($line in $located) {
            $root = $line.Trim()
            $candidate = Join-Path $root 'package.json'
            if (Test-Path $candidate) {
                $manifests.Add($candidate)
            }
        }
    }
    catch {
        Write-Verbose "Integrated Copilot discovery unavailable: $($_.Exception.Message)"
    }

    return @($manifests | Select-Object -Unique)
}

function Get-InstalledExtensionSettings {
    param([string]$ProfileName)

    $known = @{}
    $manifests = @(Get-VSCodeExtensionManifestPaths -ProfileName $ProfileName)

    foreach ($package in $manifests) {
        try {
            $items = Get-ConfigurationPropertiesFromManifest -PackageJson $package
            foreach ($key in $items.Keys) {
                $known[$key] = $items[$key]
            }
        }
        catch {
            Write-Verbose "Manifest ignored: $package - $($_.Exception.Message)"
        }
    }

    return [PSCustomObject]@{
        Settings  = $known
        Manifests = $manifests
    }
}

$settingsPath = Join-Path $RepositoryRoot '.vscode\settings.json'

if (-not (Test-Path $settingsPath)) {
    throw "Workspace settings not found: $settingsPath"
}

if (-not (Test-JsonFile -Path $settingsPath)) {
    exit 2
}

$settings = Get-Content -LiteralPath $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
$discovery = Get-InstalledExtensionSettings -ProfileName $VSCodeProfile
$knownExtensionSettings = $discovery.Settings
$manifestPaths = @($discovery.Manifests)

$workspaceKeys = @($settings.PSObject.Properties.Name)
$keysToCheck = if ($IncludeAllWorkspaceSettings) {
    $workspaceKeys
}
else {
    @($workspaceKeys | Where-Object { $_ -like 'github.copilot*' })
}

$report = foreach ($key in $keysToCheck) {
    if ($knownExtensionSettings.ContainsKey($key)) {
        $meta = $knownExtensionSettings[$key]
        [PSCustomObject]@{
            Setting   = $key
            Status    = 'RECOGNIZED'
            Extension = $meta.Extension
            Version   = $meta.Version
            Scope     = $meta.Scope
            Manifest  = $meta.Manifest
        }
    }
    elseif ($key -like 'github.copilot*') {
        [PSCustomObject]@{
            Setting   = $key
            Status    = 'UNKNOWN'
            Extension = ''
            Version   = ''
            Scope     = ''
            Manifest  = ''
        }
    }
    else {
        [PSCustomObject]@{
            Setting   = $key
            Status    = 'CORE_OR_UNVERIFIED'
            Extension = ''
            Version   = ''
            Scope     = ''
            Manifest  = ''
        }
    }
}

$unknown = @($report | Where-Object Status -eq 'UNKNOWN')
$recognized = @($report | Where-Object Status -eq 'RECOGNIZED')

Write-Host ''
Write-Host 'DataCraft - VS Code setting verification v3' -ForegroundColor Cyan
Write-Host "Repository: $RepositoryRoot"
Write-Host "Settings:   $settingsPath"
Write-Host "Profile:    $VSCodeProfile"
Write-Host ''

if ($manifestPaths.Count -eq 0) {
    Write-Host 'No extension manifest was discovered.' -ForegroundColor Yellow
}
else {
    Write-Host 'Extension manifests used:' -ForegroundColor Cyan
    $manifestPaths | ForEach-Object { Write-Host " - $_" }
}

Write-Host ''
$report | Sort-Object Status, Setting | Format-Table Setting, Status, Extension, Version, Scope -AutoSize

Write-Host ''
Write-Host ("Recognized extension settings: {0}" -f $recognized.Count) -ForegroundColor Green
Write-Host ("Unknown Copilot settings:       {0}" -f $unknown.Count) -ForegroundColor $(if ($unknown.Count) { 'Yellow' } else { 'Green' })

if ($unknown.Count -gt 0) {
    Write-Host ''
    Write-Host 'Unknown settings were not declared by the manifests discovered on this machine.' -ForegroundColor Yellow
    Write-Host 'Review those settings before keeping them in the versioned workspace configuration.' -ForegroundColor Yellow
}

$outputDir = Join-Path $RepositoryRoot '.datacraft\validation'
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
$outputPath = Join-Path $outputDir 'vscode-settings-verification.json'

$result = [ordered]@{
    subject = '.vscode/settings.json'
    executed_at = (Get-Date).ToUniversalTime().ToString('o')
    repository_root = $RepositoryRoot
    vscode_profile = $VSCodeProfile
    manifest_paths = $manifestPaths
    recognized_count = $recognized.Count
    unknown_count = $unknown.Count
    settings = @($report)
    limitation = 'Extension manifests validate extension-contributed settings. VS Code core settings are reported as CORE_OR_UNVERIFIED when -IncludeAllWorkspaceSettings is used.'
}

$result | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $outputPath -Encoding UTF8

Write-Host ''
Write-Host "Machine-readable result: $outputPath" -ForegroundColor Cyan

if ($FailOnUnknown -and $unknown.Count -gt 0) {
    exit 1
}

exit 0
