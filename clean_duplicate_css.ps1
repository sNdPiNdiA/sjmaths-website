# Remove duplicate CSS from exercise files
# Keep only page-specific styles like .container, .section, .quick-nav, .formula-box, .solution-btn, .solution

$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Only process if has style tag
    if ($content -match '<style>[\s\S]*?</style>') {
        # Extract everything between <style> and </style>
        $styleMatch = $content -match '<style>([\s\S]*?)</style>'
        if ($styleMatch) {
            $styleContent = $matches[1]
            
            # Remove CSS for properties we handle in exercise-shared.css
            # Remove :root variables (all vars defined there)
            $styleContent = $styleContent -replace '(?s):root\s*\{[^}]+\}', ''
            
            # Remove header, hero, button styles (all in shared CSS)
            $styleContent = $styleContent -replace '(?s)header\s*\{[^}]+\}', ''
            $styleContent = $styleContent -replace '(?s)\.hero\s*\{[^}]+\}', ''
            $styleContent = $styleContent -replace '(?s)\.hero\s+h1\s*\{[^}]+\}', ''
            $styleContent = $styleContent -replace '(?s)\.btn[^{]*\{[^}]+\}', ''
            $styleContent = $styleContent -replace '(?s)\.nav-btn[^{]*\{[^}]+\}', ''
            $styleContent = $styleContent -replace '(?s)\.floating-controls\s*\{[^}]+\}', ''
            
            # Remove dark mode styles
            $styleContent = $styleContent -replace '(?s)@media\s*\(prefers-color-scheme:\s*dark\)\s*\{[^}]+\}', ''
            
            # Remove animations
            $styleContent = $styleContent -replace '(?s)@keyframes[^{]*\{[^}]+\}', ''
            
            # Clean up multiple spaces and newlines
            $styleContent = $styleContent -replace '\s+', ' '
            $styleContent = $styleContent -replace '^\s+|\s+$', ''
            
            # If empty or mostly empty, remove the entire style tag
            if ([string]::IsNullOrWhiteSpace($styleContent) -or $styleContent.Length -lt 50) {
                $content = $content -replace '(?s)<style>[\s\S]*?</style>\s*', ''
            } else {
                # Replace with cleaned content
                $content = $content -replace '(?s)<style>[\s\S]*?</style>', ("<style>" + $styleContent + "</style>")
            }
            
            [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
            Write-Host "Cleaned: $($_.Name)"
        }
    }
}
