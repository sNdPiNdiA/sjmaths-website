$baseDir = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"
$chapterDirs = Get-ChildItem -Path $baseDir -Directory

foreach ($chapterDir in $chapterDirs) {
    $chapterNameRaw = $chapterDir.Name
    $chapterParts = $chapterNameRaw.Split('-')
    
    # Skip if folder name format isn't standard (e.g. doesn't have chapter number)
    if ($chapterParts.Length -lt 3) { continue }

    $chapterNumber = $chapterParts[1]
    
    # Capitalize each word in the chapter name (e.g., "real-numbers" -> "Real Numbers")
    $chapterNameParts = $chapterParts[2..($chapterParts.Length - 1)]
    $chapterName = ""
    foreach ($part in $chapterNameParts) {
        $chapterName += $part.Substring(0, 1).ToUpper() + $part.Substring(1) + " "
    }
    $chapterName = $chapterName.Trim()

    $exerciseFiles = Get-ChildItem -Path $chapterDir.FullName -Filter "*.html"

    foreach ($exerciseFile in $exerciseFiles) {
        if ($exerciseFile.Name -eq "index.html") { continue }
        
        $exerciseNameRaw = $exerciseFile.BaseName
        $exerciseParts = $exerciseNameRaw.Split('-')
        $exerciseNumber = $exerciseParts[1] + "." + $exerciseParts[2]

        $content = Get-Content $exerciseFile.FullName -Raw
        $newBodyTag = "<body
  data-class=`"10`"
  data-chapter=`"$chapterNumber`"
  data-chaptername=`"$chapterName`"
  data-exercise=`"$exerciseNumber`"
>"
        
        if ($content -notmatch 'data-class=') {
            $newContent = $content -replace '<body>', $newBodyTag
            Set-Content -Path $exerciseFile.FullName -Value $newContent -Encoding UTF8
            Write-Output "Updated: $($exerciseFile.Name)"
        }
    }
}