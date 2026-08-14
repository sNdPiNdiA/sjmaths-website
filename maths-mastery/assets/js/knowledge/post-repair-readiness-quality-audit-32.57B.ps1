$ErrorActionPreference = "Stop"

$root = "maths-mastery"

$questionRoot =
    "$root\data\questions\readiness"


function Read-BomSafeJson {

    param(
        [string]$Path
    )


    $raw =
        Get-Content `
            $Path `
            -Raw


    return (
        $raw.TrimStart(
            [char]0xFEFF
        ) |
        ConvertFrom-Json
    )
}


$issues =
    @()


$allIds =
    @{}


$globalText =
    @{}


$files =
    @(
        Get-ChildItem `
            $questionRoot `
            -Recurse `
            -File `
            -Filter "questions.json"
    )


foreach (
    $file
    in $files
) {

    $payload =
        Read-BomSafeJson `
            $file.FullName


    $skill =
        [string]$payload.readinessSkillId


    $localText =
        @{}


    foreach (
        $question
        in @(
            $payload.questions
        )
    ) {

        $id =
            [string]$question.id


        $text =
            [string]$question.questionText


        $normalized =
            $text.ToLower().Trim()


        # ----------------------------------------------------
        # ID
        # ----------------------------------------------------

        if (
            $allIds.ContainsKey(
                $id
            )
        ) {

            $issues +=
                "DUPLICATE_ID | $id"
        }
        else {

            $allIds[
                $id
            ] =
                $file.FullName
        }


        # ----------------------------------------------------
        # WITHIN BANK
        # ----------------------------------------------------

        if (
            $localText.ContainsKey(
                $normalized
            )
        ) {

            $issues +=
                "DUPLICATE_WITHIN_BANK | $skill | $id | $text"
        }
        else {

            $localText[
                $normalized
            ] =
                $id
        }


        # ----------------------------------------------------
        # GLOBAL
        # ----------------------------------------------------

        if (
            $globalText.ContainsKey(
                $normalized
            )
        ) {

            $existing =
                $globalText[
                    $normalized
                ]


            if (
                $existing -notmatch
                ("^{0}/" -f [regex]::Escape($skill))
            ) {

                $issues +=
                    "DUPLICATE_GLOBAL | $skill | $id | $existing"
            }

        }
        else {

            $globalText[
                $normalized
            ] =
                "$skill/$id"
        }


        # ----------------------------------------------------
        # OLD GENERIC QUESTION
        # ----------------------------------------------------

        if (
            $text -match
            "What should be checked before applying parallel-line angle rules"
        ) {

            $issues +=
                "GENERIC_QUESTION | $skill | $id"
        }
    }
}


Write-Host ""
Write-Host "============================================================"
Write-Host "POST-REPAIR QUALITY CHECK"
Write-Host "============================================================"
Write-Host ""

Write-Host (
    "Banks scanned : {0}" -f
    $files.Count
)

Write-Host (
    "Unique IDs    : {0}" -f
    $allIds.Count
)

Write-Host (
    "Issues        : {0}" -f
    $issues.Count
)


foreach (
    $issue
    in $issues
) {

    Write-Host `
        $issue `
        -ForegroundColor Yellow
}


if (
    $issues.Count -eq 0
) {

    Write-Host ""
    Write-Host `
        "✓ ZERO DUPLICATE / GENERIC CONTENT DEFECTS" `
        -ForegroundColor Green

}
else {

    throw (
        "Post-repair quality audit found {0} remaining issue(s)." -f
        $issues.Count
    )
}
