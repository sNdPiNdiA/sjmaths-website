# Remove duplicate script tags from exercise files
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Find all script blocks
    $scriptCount = [regex]::Matches($content, '<script>').Count
    
    if ($scriptCount -gt 1) {
        # Remove the first toggleSolution script (the inline one before footer)
        # Keep only the complete one that comes with footer
        $content = $content -replace '(?s)<script>\s*function toggleSolution\(btn\)\{\s*const sol = btn\.nextElementSibling;\s*sol\.style\.display = sol\.style\.display === "block" \? "none" : "block";\s*}\s*</script>\s*', ''
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Cleaned duplicates: $($_.Name)"
    }
}
