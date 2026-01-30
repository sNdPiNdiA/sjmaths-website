

$files = Get-ChildItem -Path "classes/class-9" -Recurse -Filter "*.html"
$cssLink = '<link rel="stylesheet" href="{0}assets/css/chapter-list.css">'
$jsModuleImport = @"
<script type="module">
    import {{ initChapterList }} from '{0}assets/js/chapter-list.js';
    // Your chapter data and initChapterList call here
</script>
"@

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw

    # Calculate relative path
    $relativePath = ""
    $depth = ($file.Directory.FullName.Replace($pwd.Path, "") -split '[\\/]').Length - 2
    for ($i = 0; $i -lt $depth; $i++) {
        $relativePath += "../"
    }

    # Add CSS link if not present
    if ($content -notmatch 'chapter-list.css') {
        $formattedCssLink = $cssLink -f $relativePath
        $content = $content -replace '</head>', "$formattedCssLink`n</head>"
    }

    # Add JS module import if not present
    if ($content -notmatch 'chapter-list.js') {
        # This is a placeholder for the actual script content.
        # The user will need to manually add the chapter data for each page.
        $formattedJsModuleImport = $jsModuleImport -f $relativePath
        $content = $content -replace '</body>', "$formattedJsModuleImport`n</body>"
    }

    Set-Content -Path $file.FullName -Value $content -Force
}

