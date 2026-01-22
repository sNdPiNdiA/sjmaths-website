$roots = @(
  "C:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10",
  "C:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-11",
  "C:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-12"
)

foreach ($root in $roots) {
  Get-ChildItem -Path $root -Recurse -Filter "exercise-*.html" | ForEach-Object {

    $file = $_.FullName
    $html = Get-Content $file -Raw

    if ($html -match "data-class=") {
      Write-Host "Already done:" $file
      return
    }

    if ($file -match "class-(\d+)") { $class = $matches[1] }

    if ($file -match "chapter-(\d+)-([a-z\-]+)") {
      $chapter = $matches[1]
      $chapterName = ($matches[2] -replace "-", " ")
      $chapterName = (Get-Culture).TextInfo.ToTitleCase($chapterName)
    }

    if ($file -match "exercise-(\d+)-(\d+)") {
      $exercise = "$($matches[1]).$($matches[2])"
    }

    $newBody = "<body data-class=`"$class`" data-chapter=`"$chapter`" data-chaptername=`"$chapterName`" data-exercise=`"$exercise`">"
    $html = $html -replace "<body>", $newBody

    Set-Content -Path $file -Value $html -Encoding UTF8
    Write-Host "Injected SEO data into:" $file
  }
}
