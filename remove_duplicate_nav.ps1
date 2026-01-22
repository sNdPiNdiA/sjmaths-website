# Remove duplicate bottom-nav sections
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Count bottom-nav sections
    $navCount = [regex]::Matches($content, '<div class="bottom-nav"').Count
    
    if ($navCount -gt 1) {
        # Remove the first bottom-nav (the original one), keep the second one (our new standardized one)
        # Remove all bottom-nav before the footer
        $content = $content -replace '(?s)<div class="bottom-nav">\s*<a href="[^"]*" class="nav-btn btn-prev">[^<]*</a>\s*<a href="[^"]*" class="nav-btn btn-next">[^<]*</a>\s*</div>\s*(?=</div>\s*<div class="bottom-nav")', ''
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Removed duplicate nav: $($_.Name)"
    }
}
