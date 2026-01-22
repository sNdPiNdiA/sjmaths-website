# Add CSS links to remaining exercise files
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

# Files that still need CSS links
$filesToUpdate = @(
    'chapter-2-polynomials/exercise-2-1.html',
    'chapter-2-polynomials/exercise-2-2.html',
    'chapter-3-pair-of-linear-equations-in-two-variables/exercise-3-1.html',
    'chapter-3-pair-of-linear-equations-in-two-variables/exercise-3-2.html',
    'chapter-5-arithmetic-progressions/exercise-5-1.html',
    'chapter-5-arithmetic-progressions/exercise-5-2.html',
    'chapter-5-arithmetic-progressions/exercise-5-3.html',
    'chapter-5-arithmetic-progressions/exercise-5-4.html',
    'chapter-6-triangles/exercise-6-1.html',
    'chapter-6-triangles/exercise-6-2.html',
    'chapter-6-triangles/exercise-6-3.html',
    'chapter-7-coordinate-geometry/exercise-7-1.html'
)

foreach ($relativePath in $filesToUpdate) {
    $filePath = Join-Path $basePath $relativePath
    if (Test-Path $filePath) {
        $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
        
        # Find the line with <style> and add CSS links before it
        if ($content -match '<style') {
            $newline = [System.Environment]::NewLine
            $cssLinks = $newline + '<link rel="stylesheet" href="/assets/css/exercise-shared.css">' + $newline + '<link rel="stylesheet" href="/assets/css/footer.css">' + $newline
            $content = $content -replace '(<style)', ($cssLinks + '$1')
            [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
            Write-Host "Added CSS links: $relativePath"
        }
    } else {
        Write-Host "File not found: $filePath"
    }
}
