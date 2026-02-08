
$files = Get-ChildItem -Path "classes/class-9" -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName
    $newContent = $content | Where-Object { $_ -notmatch 'chapter-list.css' -and $_ -notmatch 'chapter-list.js' }
    Set-Content -Path $file.FullName -Value $newContent -Force
}
