# Fix UTF-8 encoding issues
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

$emDash = "`u{00e2}`u{0080}`u{0093}"  # â€"
$ellipsis = "`u{00e2}`u{0080}`u{00a6}" # â€¦
$minus = "`u{00e2}`u{0088}`u{0092}"    # âˆ'
$sqrt = "`u{00e2}`u{0088}`u{009a}"     # âˆš
$copyright = "`u{00c2}`u{00a9}"        # Â©
$quote = "`u{00e2}`u{0080}`u{0099}"    # â€™
$pi = "`u{00e2}`u{0084}`u{0080}"       # â„

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    [string]$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $originalContent = $content
    
    # Replace corrupted characters
    $content = $content.Replace($emDash, "–")
    $content = $content.Replace($ellipsis, "…")
    $content = $content.Replace($minus, "−")
    $content = $content.Replace($sqrt, "√")
    $content = $content.Replace($copyright, "©")
    $content = $content.Replace($quote, "'")
    $content = $content.Replace($pi, "π")
    
    # Write back if changes were made
    if ($content -ne $originalContent) {
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed: $($_.Name)"
    } else {
        Write-Host "OK: $($_.Name)"
    }
}

Write-Host "Done!"
