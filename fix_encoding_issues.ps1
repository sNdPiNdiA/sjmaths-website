# Fix UTF-8 encoding issues using character codes
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $originalContent = $content
    
    # Fix corrupted em-dash (â€" to –)
    $content = $content -replace 'â€"', [char]0x2013
    
    # Fix corrupted ellipsis (â€¦ to …)
    $content = $content -replace 'â€¦', [char]0x2026
    
    # Fix corrupted minus (âˆ' to −)
    $content = $content -replace 'âˆ'', [char]0x2212
    
    # Fix corrupted sqrt (âˆš to √)
    $content = $content -replace 'âˆš', [char]0x221A
    
    # Fix corrupted copyright (Â© to ©)
    $content = $content -replace 'Â©', [char]0xA9
    
    # Fix corrupted right quote (â€™ to ')
    $content = $content -replace 'â€™', [char]0x2019
    
    # Fix corrupted pi (â„ to π)
    $content = $content -replace 'â„', [char]0x03C0
    
    # Write back if changes were made
    if ($content -ne $originalContent) {
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed: $($_.Name)"
    } else {
        Write-Host "No issues: $($_.Name)"
    }
}

Write-Host "Encoding fixes complete!"
