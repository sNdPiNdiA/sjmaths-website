# Remove old footer sections and keep only the new standardized footer
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Remove old footer sections (the complex ones with multiple links)
    # Keep only the new simple footer with 3 links
    $content = $content -replace '(?s)<footer>[\s\S]*?</footer>\s*(?=<div class="bottom-nav")', ''
    $content = $content -replace '(?s)<footer[^>]*>[\s\S]*?</footer>\s*(?=<div class="bottom-nav")', ''
    
    [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Fixed footer: $($_.Name)"
}
