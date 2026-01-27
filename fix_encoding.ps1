# PowerShell Script to fix text encoding artifacts in Class 11 Notes
$targetPath = "classes\class-11\chapter-wise-notes"

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

# Define correct symbols using Unicode Code Points to be ASCII-safe
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
    "$([char]0xD83C)$([char]0xDFAF)", # Target 🎯 (Surrogate pair)
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

# Build replacement map
$replacements = @{}
foreach ($sym in $symbols) {
    $mojibake = Get-Mojibake $sym
    $replacements[$mojibake] = $sym
}

Get-ChildItem -Path $targetPath -Recurse -Filter "*.html" | ForEach-Object {
    $path = $_.FullName
    $content = Get-Content $path -Raw -Encoding UTF8
    $originalContent = $content
    
    # Sort keys by length descending to prevent partial replacements
    $keys = $replacements.Keys | Sort-Object -Property Length -Descending
    foreach ($key in $keys) {
        if ($content.Contains($key)) {
            $content = $content.Replace($key, $replacements[$key])
        }
    }

    if ($content -ne $originalContent) {
        $content | Set-Content $path -Encoding UTF8
        Write-Host "Fixed encoding in: $($_.Name)" -ForegroundColor Green
    }
}
Write-Host "Done! All Class 11 chapters processed." -ForegroundColor Cyan
