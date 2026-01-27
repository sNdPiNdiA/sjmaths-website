# PowerShell Script to CHECK for text encoding artifacts (Mojibake)
$targetPath = "classes"

# Ensure console output handles UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Register encoding provider for PowerShell Core / .NET Core compatibility
try {
    [System.Text.Encoding]::RegisterProvider([System.Text.CodePagesEncodingProvider]::Instance)
} catch {
    # Ignore if running on Windows PowerShell where this is not needed/available
}

# Function to generate the "Mojibake" string (UTF-8 bytes interpreted as Windows-1252)
function Get-Mojibake($correctChar) {
    $utf8 = [System.Text.Encoding]::UTF8
    $bytes = $utf8.GetBytes($correctChar)
    # Windows-1252 (Code Page 1252)
    $win1252 = [System.Text.Encoding]::GetEncoding(1252)
    return $win1252.GetString($bytes)
}

# Define correct symbols using Unicode Code Points
$symbols = @(
    [char]0x2022, # Bullet •
    [char]0x222A, # Union ∪
    [char]0x2229, # Intersection ∩
    [char]0x2019, # Right Single Quote ’
    [char]0x2018, # Left Single Quote ‘
    [char]0x201C, # Left Double Quote “
    [char]0x201D, # Right Double Quote ”
    [char]0x2013, # En Dash –
    [char]0x2014, # Em Dash —
    "$([char]0x26A0)$([char]0xFE0F)", # Warning ⚠️
    [char]0x2714, # Check ✔
    [char]0x274C, # Cross ❌
    "$([char]0xD83C)$([char]0xDFAF)", # Target 🎯
    [char]0x2212, # Minus −
    [char]0x2264, # Less equal ≤
    [char]0x2265, # Greater equal ≥
    [char]0x2192, # Right Arrow →
    [char]0x2200, # For All ∀
    [char]0x2203, # Exists ∃
    [char]0x2208, # Element Of ∈
    [char]0x2282, # Subset ⊂
    [char]0x2286, # Subset Eq ⊆
    [char]0x2205, # Empty Set ∅
    [char]0x2260, # Not Equal ≠
    [char]0x211D, # Real Numbers ℝ
    [char]0x221A, # Square Root √
    [char]0x221E, # Infinity ∞
    [char]0x00B2, # Superscript 2 ²
    "$([char]0xD83D)$([char]0xDCCC)" # Pushpin 📌
)

# Build map of Bad -> Good
$mojibakeMap = @{}
foreach ($sym in $symbols) {
    $bad = Get-Mojibake $sym
    if ($bad -ne $sym) { 
        $mojibakeMap[$bad] = $sym 
    }
}

$foundIssues = $false

if (-not (Test-Path $targetPath)) {
    Write-Error "Target path '$targetPath' not found. Please run this script from the website root folder."
    exit
}

Get-ChildItem -Path $targetPath -Recurse -Filter "*.html" | ForEach-Object {

    try {
        $content = Get-Content $_.FullName -Raw -Encoding UTF8
    } catch {
        Write-Warning "Could not read file: $($_.FullName)"
        return
    }

    if ($null -eq $content) { return }

    $fileIssues = @()

    foreach ($bad in $mojibakeMap.Keys) {
        if ($content -and $content.Contains($bad)) {
            $fileIssues += "Found '$bad' -> Should be '$($mojibakeMap[$bad])'"
        }
    }

    if ($fileIssues.Count -gt 0) {
        $foundIssues = $true
        Write-Host "Issues in: $($_.FullName)" -ForegroundColor Red
        foreach ($issue in $fileIssues) { 
            Write-Host "  $issue" -ForegroundColor Yellow 
        }
    }
}

if (-not $foundIssues) { 
    Write-Host "No encoding artifacts found!" -ForegroundColor Green 
}
