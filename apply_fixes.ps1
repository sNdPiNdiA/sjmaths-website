$parentDir = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice\"

$folders = @(
    "chapter-3-pair-of-linear-equations-in-two-variables",
    "chapter-4-quadratic-equations",
    "chapter-5-arithmetic-progressions",
    "chapter-6-triangles",
    "chapter-7-coordinate-geometry",
    "chapter-8-introduction-to-trigonometry",
    "chapter-9-applications-of-trigonometry",
    "chapter-10-circles",
    "chapter-11-areas-related-to-circles",
    "chapter-12-surface-areas-and-volumes",
    "chapter-13-statistics",
    "chapter-14-probability"
)

foreach ($folder in $folders) {
    $currentDir = Join-Path -Path $parentDir -ChildPath $folder
    $files = Get-ChildItem -Path $currentDir -Filter *.html -Recurse

    foreach ($file in $files) {
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

        # 1. Rename toggleSolution to toggleStepSolution
        $content = $content -replace 'onclick="toggleSolution\(this\)"', 'onclick="toggleStepSolution(this)"'
        $content = $content -replace 'function toggleSolution\(btn\)', 'function toggleStepSolution(btn)'

        # 2. Add exercise.js script
        if ($content -notmatch '<script src="/assets/js/exercise.js"></script>') {
            $replacement = '<script src="/assets/js/exercise.js"></script>' + "`n" + '</body>'
            $content = $content -replace '</body>', $replacement
        }

        # 3. Add formula button
        if ($content -notmatch 'class="formula-btn"') {
            $replacement = '${1}' + "`n" + '  <button class="formula-btn"><i class="fas fa-square-root-alt"></i> Formulas</button>'
            $content = $content -replace '(<button class="theme-toggle-btn".*?</button>)', $replacement
        }

        # 4. Fix encoding
        $content = $content -replace 'â€“', '–'
        $content = $content -replace 'â‚¹', '₹'

        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Processed $($file.FullName)"
    }
}
