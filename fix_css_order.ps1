
$targetDir = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-11\tests"

# Get all HTML files recursively
$files = Get-ChildItem -Path $targetDir -Filter "*.html" -Recurse

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Check if file has both CSS links
    if ($content -match "test-interface\.min\.css" -and $content -match "improved-ui\.min\.css") {
        
        # Check if test-interface is BEFORE improved-ui (which is the problem)
        $testPos = $content.IndexOf("test-interface.min.css")
        $uiPos = $content.IndexOf("improved-ui.min.css")
        
        if ($testPos -lt $uiPos) {
            Write-Host "Fixing CSS order in: $($file.Name)"
            
            # 1. Remove the test-interface link (and surrounding lines/comments if possible, but regex is safer for just the link)
            # We match the whole line containing test-interface
            $content = $content -replace '(?m)^\s*<link.*test-interface\.min\.css.*\r?\n?', ''
            
            # 2. Append it after improved-ui link
            # We find the improved-ui link and add test-interface after it
            $replacement = "<link rel=`"stylesheet`" href=`"/assets/css/improved-ui.min.css`">`n    <link rel=`"stylesheet`" href=`"../../../../../assets/css/test-interface.min.css?v=1770179813`">"
            
            # CAUTION: The relative path complexity. 
            # We should capture the original link tag to preserve the correct relative path!
            
            # Rethink: Use Regex to capture the exact line used in the file
             if ($content -match '(<link[^>]*test-interface\.min\.css[^>]*>)') {
                 $originalLink = $Matches[1]
                 
                 # Remove original
                 $content = $content -replace [regex]::Escape($originalLink), ''
                 
                 # Insert after improved-ui
                 $content = $content -replace '(<link[^>]*improved-ui\.min\.css[^>]*>)', "`$1`n    $originalLink"
                 
                 Set-Content -Path $file.FullName -Value $content
             }
        }
    }
}
