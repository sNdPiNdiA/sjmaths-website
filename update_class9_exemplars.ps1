$files = Get-ChildItem -Path "classes\class-9\ncert-examplar-practice" -Recurse -Filter "exemplar-*.html"
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $modified = $false

    # Skip if already updated
    if ($content -match "hero-text-wrapper") {
        Write-Host "Skipping $($file.Name) - Already updated"
        continue
    }

    # 1. Update structure (Wrap H1 and P in hero-text-wrapper, Preserving Breadcrumb)
    # Match: <div class="hero"> ... <nav class="breadcrumb">...</nav> ... <h1>...</h1> ... <p>...</p> ... </div>
    # regex explanation:
    # <div class="hero">\s*                     -> Start of hero
    # (<nav class="breadcrumb">.*?</nav>)\s*    -> Capture breadcrumb ($1)
    # (<h1>.*?</h1>)\s*                         -> Capture H1 ($2)
    # (<p>.*?</p>)                              -> Capture P ($3)
    
    if ($content -match '(?s)<div class="hero">\s*(<nav class="breadcrumb">.*?</nav>)\s*(<h1>.*?</h1>)\s*(<p>.*?</p>)') {
        $replacement = '<div class="hero" style="display: flex; flex-direction: column; justify-content: flex-start; align-items: center; padding-top: 1rem; min-height: auto;">' + "`r`n" +
                       '        $1' + "`r`n" + # Breadcrumb
                       '        <div class="hero-text-wrapper" style="margin-top: 2rem; position: relative; z-index: 2;">' + "`r`n" +
                       '            $2' + "`r`n" + # H1
                       '            $3' + "`r`n" + # P
                       '        </div>'
        
        # Note: We replace only the opening part, assuming the closing </div> is after the <p>. 
        # Actually, the regex above matches up to the closing </p>. The closing </div> of hero is presumably after that.
        # So we just replace that chunk.
        
        $content = $content -replace '(?s)<div class="hero">\s*(<nav class="breadcrumb">.*?</nav>)\s*(<h1>.*?</h1>)\s*(<p>.*?</p>)', $replacement
        $modified = $true
    }

    # 2. Update CSS Link (min -> css + version) to ensure mobile fixes apply
    if ($content -match 'exercise-shared\.min\.css') {
        $content = $content -replace 'exercise-shared\.min\.css\?v=\d+', 'exercise-shared.css?v=99999'
        $modified = $true
    }

    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated $($file.Name)"
        $count++
    }
}

Write-Host "Total Class 9 Exemplar files updated: $count"
