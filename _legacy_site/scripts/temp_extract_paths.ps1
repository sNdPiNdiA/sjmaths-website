# PowerShell script to extract and resolve CSS/JS file paths
param(
    [string]$searchOutput,
    [string]$fileType
)

$currentDir = "c:\Users\sande\Documents\GitHub\sjmaths-website" # Assuming this is the root of the project
$regex = ''
$extractedPaths = @()

if ($fileType -eq "css") {
    $regex = 'href="(?<path>[^"]+\.css)"'
} elseif ($fileType -eq "js") {
    $regex = 'src="(?<path>[^"]+\.js)"'
}

$searchOutputLines = $searchOutput -split "`n"

$referringFile = ""
foreach ($line in $searchOutputLines) {
    if ($line -match '^File: (.+)') {
        $referringFile = $Matches[1]
    } elseif ($line -match $regex) {
        $relativePath = $Matches["path"]
        if ($relativePath -notmatch '^https?://') { # Not an external URL
            # Resolve relative path
            $fullReferringPath = Join-Path $currentDir $referringFile
            $basePath = Split-Path $fullReferringPath -Parent

            $absolutePath = ""
            if ($relativePath.StartsWith('/')) {
                # Path is absolute from the root of the project
                $absolutePath = Join-Path $currentDir $relativePath
            } else {
                # Path is relative to the referring file
                $absolutePath = Join-Path $basePath $relativePath
            }
            # Normalize path (remove .. and make consistent)
            $normalizedPath = (Resolve-Path $absolutePath).Path
            $extractedPaths += $normalizedPath
        }
    }
}

$extractedPaths | Select-Object -Unique