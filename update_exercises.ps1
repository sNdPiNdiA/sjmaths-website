$files = Get-ChildItem -Path "classes" -Recurse -Filter "exercise-*.html"
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $modified = $false

    # Skip if already updated
    if ($content -match "hero-text-wrapper") {
        Write-Host "Skipping $($file.Name) - Already updated"
        continue
    }

    # 1. Update structure (Wrap H1 and P in hero-text-wrapper, Apply Inline Styles)
    # Regex explanation:
    # (?s) enables single-line mode (dot matches newline)
    # Match <section class="hero">...<h1>...</h1>...<p>...</p>
    # Capture H1 content and P content
    if ($content -match '(?s)<section class="hero">\s*(<h1>.*?</h1>)\s*(<p>.*?</p>)') {
        $replacement = '<section class="hero" style="display: flex; flex-direction: column; justify-content: flex-start; align-items: center; padding-top: 1rem; min-height: auto;">' + "`r`n" +
                       '  <!-- Breadcrumb will be inserted here by JS -->' + "`r`n" +
                       '  <div class="hero-text-wrapper" style="margin-top: 2rem; position: relative; z-index: 2;">' + "`r`n" +
                       '    $1' + "`r`n" +
                       '    $2' + "`r`n" +
                       '  </div>'
        
        $content = $content -replace '(?s)<section class="hero">\s*(<h1>.*?</h1>)\s*(<p>.*?</p>)', $replacement
        $modified = $true
    }

    # 2. Update CSS Link (min -> css + version)
    if ($content -match 'exercise-shared\.min\.css') {
        $content = $content -replace 'exercise-shared\.min\.css\?v=\d+', 'exercise-shared.css?v=99999'
        $modified = $true
    }

    # 3. Remove Home Button
    if ($content -match '<a href="/" class="btn btn-outline">Home</a>') {
        $content = $content -replace '\s*<a href="/" class="btn btn-outline">Home</a>', ''
        $modified = $true
    }
    
    # 4. Center the Back Button (if it exists in hero-buttons)
    # Ensure hero-buttons container centers its content (it does by CSS, but let's be clean)
    
    # 5. Remove Text from Floating Button
    # Match: <a ... class="back-btn-floating"> <i ...></i> Back to Class X </a>
    # Replace with just icon
    if ($content -match 'class="back-btn-floating">\s*<i class="fas fa-arrow-left"></i>\s*Back to Class \d+') {
        $content = $content -replace '(class="back-btn-floating">\s*<i class="fas fa-arrow-left"></i>)\s*Back to Class \d+', '$1'
        $modified = $true
    }

    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated $($file.Name)"
        $count++
    }
}

Write-Host "Total files updated: $count"
