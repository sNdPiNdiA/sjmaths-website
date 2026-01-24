# This script automates adding a shared, dynamic breadcrumb navigation to chapter notes and exercise pages.
# It targets specific 'index.html' files across all "class-*" directories.

# Get the directory where the script is located to create a full path to the 'classes' directory.
$PSScriptRoot = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
$basePath = Join-Path $PSScriptRoot "classes"

# Define the sub-folders within each class directory that should be processed.
$targetSubFolders = @(
    "chapter-wise-notes",
    "ncert-exercise-practice",
    "previous-year-questions",
    "previous-years-papers",
    "full-length-test-papers",
    "sample-papers",
    "tests",
    "worksheets",
    "ncert-examplar-practice"
)

# 1. Find all relevant 'index.html' files.
$targetFiles = Get-ChildItem -Path $basePath -Recurse -Filter "index.html" | Where-Object {
    $parentName = $_.Directory.Parent.Name
    $targetSubFolders -contains $parentName
}

if ($targetFiles.Count -eq 0) {
    Write-Host "No files found in the target directories. Please check the paths in the script." -ForegroundColor Yellow
    exit
}

Write-Host "Found $($targetFiles.Count) files to process..." -ForegroundColor Cyan

# Regex to find an existing hardcoded breadcrumb navigation.
$breadcrumbRegex = '(?s)<nav class="breadcrumb">.*?</nav>'

foreach ($file in $targetFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content

    # 2. Replace the hardcoded breadcrumb with a placeholder div.
    # If a breadcrumb is found, it's replaced.
    # If not, it inserts the placeholder after the <header></header> tag.
    if ($content -match $breadcrumbRegex) {
        $content = $content -replace $breadcrumbRegex, '<div id="breadcrumb-container"></div>'
    } elseif ($content -match '(<header></header>)' -and -not ($content -match 'id="breadcrumb-container"')) {
        # Using CRLF for Windows-style line endings.
        $content = $content -replace '(<header></header>)', "`$1`r`n<div id=`"breadcrumb-container`"></div>"
    }

    # 3. Add the script tag for the breadcrumb loader if it's not already present.
    # This assumes a consistent folder depth for all target pages.
    if (-not ($content -match 'loadBreadcrumb.js')) {
        # This path is relative to the location of the index.html files.
        # classes/class-*/<subfolder>/<chapter>/index.html -> ../../../../
        $scriptPath = "../../../../utils/loadBreadcrumb.js"
        $scriptTag = "<script src=`"$scriptPath`"></script>"

        # Insert the new script tag after 'loadScrollProgress.js' for consistency.
        $insertionPattern = '(<script src=".*\/loadScrollProgress.js"><\/script>)'
        if ($content -match $insertionPattern) {
            $content = $content -replace $insertionPattern, "`$1`r`n    $scriptTag"
        } else {
            # As a fallback, add it before the closing body tag.
            $content = $content -replace '</body>', "    $scriptTag`r`n</body>"
        }
    }

    # 4. Write the changes back to the file only if something was modified to avoid unnecessary file writes.
    if ($content -ne $originalContent) {
        Write-Host "Updating $($file.FullName)" -ForegroundColor Green
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
    }
}

Write-Host "`nDone. All targeted files have been checked and updated where necessary." -ForegroundColor Cyan
