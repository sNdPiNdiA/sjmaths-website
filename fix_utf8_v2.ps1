$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

[byte[]]$utf8EmDash = 0xE2, 0x80, 0x93     # â€"
[byte[]]$utf8Ellipsis = 0xE2, 0x80, 0xA6  # â€¦
[byte[]]$utf8Minus = 0xE2, 0x88, 0x92     # âˆ'
[byte[]]$utf8Sqrt = 0xE2, 0x88, 0x9A      # âˆš
[byte[]]$utf8Copyright = 0xC2, 0xA9       # Â©
[byte[]]$utf8Quote = 0xE2, 0x80, 0x99     # â€™
[byte[]]$utf8Pi = 0xE2, 0x84, 0x80        # â„

$emDashStr = [System.Text.Encoding]::UTF8.GetString($utf8EmDash)
$ellipsisStr = [System.Text.Encoding]::UTF8.GetString($utf8Ellipsis)
$minusStr = [System.Text.Encoding]::UTF8.GetString($utf8Minus)
$sqrtStr = [System.Text.Encoding]::UTF8.GetString($utf8Sqrt)
$copyrightStr = [System.Text.Encoding]::UTF8.GetString($utf8Copyright)
$quoteStr = [System.Text.Encoding]::UTF8.GetString($utf8Quote)
$piStr = [System.Text.Encoding]::UTF8.GetString($utf8Pi)

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    [string]$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $original = $content
    
    $content = $content.Replace($emDashStr, "–")
    $content = $content.Replace($ellipsisStr, "…")
    $content = $content.Replace($minusStr, "−")
    $content = $content.Replace($sqrtStr, "√")
    $content = $content.Replace($copyrightStr, "©")
    $content = $content.Replace($quoteStr, "'")
    $content = $content.Replace($piStr, "π")
    
    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed: $($_.Name)"
    } else {
        Write-Host "OK: $($_.Name)"
    }
}

Write-Host "Complete!"
