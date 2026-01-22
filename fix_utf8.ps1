$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    [string]$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $original = $content
    
    # Replace using .NET methods - these are safer
    $content = $content.Replace([char]0xE2 + [char]0x80 + [char]0x93, "–")
    $content = $content.Replace([char]0xE2 + [char]0x80 + [char]0xA6, "…")
    $content = $content.Replace([char]0xE2 + [char]0x88 + [char]0x92, "−")
    $content = $content.Replace([char]0xE2 + [char]0x88 + [char]0x9A, "√")
    $content = $content.Replace([char]0xC2 + [char]0xA9, "©")
    $content = $content.Replace([char]0xE2 + [char]0x80 + [char]0x99, "'")
    $content = $content.Replace([char]0xE2 + [char]0x84 + [char]0x80, "π")
    
    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed: $($_.Name)"
    } else {
        Write-Host "OK: $($_.Name)"
    }
}

Write-Host "Complete!"
