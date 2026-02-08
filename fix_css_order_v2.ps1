
$targetDir = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-11\tests"
$files = Get-ChildItem -Path $targetDir -Filter "*.html" -Recurse

foreach ($file in $files) {
    $lines = Get-Content -Path $file.FullName
    $testInterfaceLine = $null
    $hasUI = $false
    
    # scan for existence and capture the line
    foreach ($line in $lines) {
        if ($line -match "test-interface\.min\.css") {
            $testInterfaceLine = $line
        }
        if ($line -match "improved-ui\.min\.css") {
            $hasUI = $true
        }
    }
    
    if ($testInterfaceLine -ne $null -and $hasUI) {
        Write-Host "Processing $($file.Name)..."
        $newContent = @()
        
        foreach ($line in $lines) {
            # Skip the existing test-interface line (we will re-insert it)
            if ($line -match "test-interface\.min\.css") {
                continue
            }
            
            $newContent += $line
            
            # Insert it immediately after improved-ui
            if ($line -match "improved-ui\.min\.css") {
                $newContent += $testInterfaceLine
            }
        }
        
        $newContent | Set-Content -Path $file.FullName
    }
}
