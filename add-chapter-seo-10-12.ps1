$basePath = "classes"

$classes = @("class-10", "class-11", "class-12")

foreach ($class in $classes) {
    $chapterRoot = Join-Path $basePath "$class\chapter-wise-notes"

    Get-ChildItem -Path $chapterRoot -Directory | ForEach-Object {

        $chapterFolder = $_.Name
        $chapterMatch = [regex]::Match($chapterFolder, "chapter-(\d+)-(.+)")
        if (!$chapterMatch.Success) { return }

        $chapterNo = $chapterMatch.Groups[1].Value
        $chapterName = $chapterMatch.Groups[2].Value -replace "-", " "
        $chapterName = (Get-Culture).TextInfo.ToTitleCase($chapterName)

        $indexFile = Join-Path $_.FullName "index.html"
        if (!(Test-Path $indexFile)) { return }

        $html = Get-Content $indexFile -Raw

        if ($html -notmatch "data-class") {

            $bodyTag = "<body data-class=`"$($class -replace 'class-','')`" data-chapter=`"$chapterNo`" data-chaptername=`"$chapterName`">"
            $html = $html -replace "<body>", $bodyTag
        }

        if ($html -notmatch "chapter-seo.js") {

            $seoScript = "`n<script src=`"/assets/js/chapter-seo.js`"></script>`n</body>"
            $html = $html -replace "</body>", $seoScript
        }

        Set-Content $indexFile $html -Encoding UTF8

        Write-Host "SEO added to: $indexFile"
    }
}
