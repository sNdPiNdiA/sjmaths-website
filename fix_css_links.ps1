# Fix CSS links in all class-10 exercise files
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Remove malformed links
    $content = $content -replace '`n<link rel="stylesheet" href="/assets/css/exercise-shared.css">`n<link rel="stylesheet" href="/assets/css/footer.css">', ''
    
    # Add proper links after Font Awesome
    if ($content -match '<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+">') {
        $newline = [System.Environment]::NewLine
        $cssLinks = $newline + '<link rel="stylesheet" href="/assets/css/exercise-shared.css">' + $newline + '<link rel="stylesheet" href="/assets/css/footer.css">'
        $content = $content -replace '(<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+">)', ('$1' + $cssLinks)
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed: $($_.Name)"
    }
}
