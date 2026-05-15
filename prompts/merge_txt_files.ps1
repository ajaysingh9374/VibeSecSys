# Merge all stage text files into one BIGMASTER file
# Filename becomes heading followed by file content

$outputFile = "BIGMASTER.txt"

$files = @(
    "stage1-step1-project-start_checks.txt",
    "stage10-OCTAVE_STRIDE Report.txt",
    "stage10-OCTAVE_STRIDE with Table Report.txt",
    "stage2-step1-scan-mode-selector.txt",
    "stage2-step2-localhost-xml-scan.txt",
    "stage2-step3-xml-loader.txt",
    "stage2-step4-xml-parser.txt",
    "stage2-step5-baseline-analysis.txt",
    "stage4-step1-data-structuring.txt",
    "stage5-step1-ai-module-setup.txt",
    "stage5-step2-api-config.txt",
    "stage5-step3-prompt-embedding.txt",
    "stage5-step4-ai-call.txt",
    "stage5-step5-response-handling.txt",
    "stage6-step1-markdown-report.txt",
    "stage7-file-output.txt",
    "stage8-cli.txt",
    "stage9-testing.txt"
)

# Clear/Create output file
"" | Set-Content -Path $outputFile -Encoding UTF8

foreach ($file in $files) {

    if (Test-Path $file) {

        Add-Content -Path $outputFile -Value "==================================================" -Encoding UTF8
        Add-Content -Path $outputFile -Value "FILE: $file" -Encoding UTF8
        Add-Content -Path $outputFile -Value "==================================================" -Encoding UTF8
        Add-Content -Path $outputFile -Value "" -Encoding UTF8

        Get-Content -Path $file -Raw | Add-Content -Path $outputFile -Encoding UTF8

        Add-Content -Path $outputFile -Value "`r`n`r`n" -Encoding UTF8

    }
    else {

        Add-Content -Path $outputFile -Value "MISSING FILE: $file" -Encoding UTF8
        Add-Content -Path $outputFile -Value "`r`n" -Encoding UTF8

    }
}

Write-Host ""
Write-Host "BIGMASTER.txt created successfully."
Write-Host ""