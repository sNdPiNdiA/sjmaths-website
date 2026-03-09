# Fix navigation links in previous-year-questions
# Add folder name when missing from chapter-wise URLs
Get-ChildItem -Recurse -Path .\classes\class-10\previous-year-questions\chapter-wise\chapter-* -Filter *.html | ForEach-Object {
    $file = $_.FullName
    $folder = Split-Path $file -Parent | Split-Path -Leaf
    $content = Get-Content $file
    $changed = $false
    for ($i = 0; $i -lt $content.Count; $i++) {
        $line = $content[$i]
        if ($line -match 'href="/classes/class-10/previous-year-questions/chapter-wise/([^"\s]+)"') {
            $target = $matches[1]
            if ($target -notmatch '^chapter-') {
                $newTarget = "$folder/$target"
                $content[$i] = $line -replace [regex]::Escape($target), $newTarget
                $changed = $true
            }
        }
    }
    if ($changed) {
        Write-Host "Patched $file"
        $content | Set-Content $file
    }
}