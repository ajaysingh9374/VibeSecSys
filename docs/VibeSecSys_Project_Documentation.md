# VibeSecSys Project Documentation

## Project Summary

VibeSecSys is a Python-based cybersecurity scan analysis project. The application accepts Nmap XML data, extracts host and service information, prepares a baseline security summary, sends structured scan context to OpenAI for analysis, and saves a Markdown security report.

The project has been developed in controlled stages. Version 1.0 focuses on a working CLI-based scan analysis pipeline. Version 2.0 focuses on an experimental template-driven cybersecurity report format with OCTAVE, STRIDE, vulnerability classification, severity assessment, mitigation recommendations, and report refinement.

## Current Application Status

The main application is implemented as a command-line workflow using `main.py`.

Implemented capabilities:

- Default localhost scan using Nmap when no input file is supplied.
- XML input mode using `--input`.
- Markdown report output using default `reports/report.md` or custom `--output`.
- XML loading and parsing.
- Baseline analysis for total hosts, total open ports, and discovered services.
- AI input preparation from parsed scan data.
- OpenAI analysis call using environment-based API key loading.
- Markdown report generation from the AI response.
- File output using the reporting module.

## Current Main Pipeline

1. User runs `main.py`.
2. If `--input` is provided, the application reads that XML file.
3. If no input is provided, the application runs a localhost Nmap scan.
4. XML content is loaded.
5. XML data is parsed into host and port records.
6. Baseline summary is generated.
7. AI input text is prepared.
8. AI analysis is requested.
9. Markdown report content is generated.
10. Report is saved to disk.

## Main Commands

Default localhost scan:

```powershell
python main.py
```

Use an existing XML file:

```powershell
python main.py --input samples\Vibe.xml
```

Use an existing XML file and custom report output:

```powershell
python main.py --input samples\Vibe.xml --output reports\Vibe.md
```

## Major Project Areas

| Area | Status | Description |
|---|---|---|
| Main CLI application | Complete for Version 1.0 | Handles input, scan execution, parsing, AI analysis, and report output |
| Scanner module | Complete for Version 1.0 | Contains scan runner, XML loader, XML parser, and baseline analysis |
| AI module | Complete for Version 1.0 | Prepares scan data and calls OpenAI |
| Reporting module | Complete for Version 1.0 | Builds Markdown report and writes it to disk |
| Stage 10 OCTAVE/STRIDE reports | One-time generated documents | Created as separate Markdown outputs, not a reusable app feature |
| V2.0 report templates | Experimental | Template and row-based report generation exists outside the main application |
| V2.0 final report refinement | Experimental | Final Markdown reports and PDFs were generated from experiments |
| V2.0 integration into `main.py` | <span style="color:red">TODO</span> | Not integrated into the main CLI workflow |

## Version 1.0 Stage Summary

| Stage | Summary | Status |
|---|---|---|
| Stage 1 | Created project skeleton and verified `main.py` execution | Complete |
| Stage 2 | Added scan selection, localhost XML scan, XML loader, parser, and baseline analysis | Complete |
| Stage 3 | Originally planned separately; merged into Stage 2 baseline work | Merged |
| Stage 4 | Structured parsed scan data for AI input | Complete |
| Stage 5 | Added AI module, OpenAI API configuration, prompt construction, AI call, and response handling | Complete |
| Stage 6 | Added Markdown report generation | Complete |
| Stage 7 | Added report file output | Complete |
| Stage 8 | Added CLI input/output options and default localhost behavior | Complete |
| Stage 9 | Tested application execution paths and report output | Complete |
| Stage 10 | Generated OCTAVE and STRIDE reports as one-time documents | Complete as documentation output |

## Version 2.0 Summary

Version 2.0 work is focused on a richer cybersecurity report format. It uses sample XML data, report templates, generated table rows, and report refinement prompts.

Version 2.0 artifacts include:

- Sample XML files in `V2.0/samples/`.
- Report templates in `V2.0/templates/`.
- Experiment scripts and prompt files in `V2.0/experiments/`.
- Generated reports such as `final_report_NEW.md`, `final_report_NEW_v2.md`, `final_report_NEW_v3.md`, and `final_report_NEW_v4.md`.
- Generated PDF versions of refined reports.

Important note:

<span style="color:red">TODO</span> Version 2.0 is not yet coded as a supported feature inside the main application pipeline. It exists as experimental scripts, templates, prompts, and generated output files.

## Documentation Set

This project documentation is split across multiple files:

- `Documentation_Index.md`
- `VibeSecSys_Project_Documentation.md`
- `User_Guide.md`
- `Developer_Guide.md`
- `Architecture.md`
- `AI_Usage.md`
- `Report_Generation.md`
- `V2_Experimental_Report_Pipeline.md`
- `Current_Gaps_and_TODO.md`

## Human Validation Requirement

AI-assisted cybersecurity analysis should be treated as decision support, not final authority. All findings, severity ratings, risk statements, and remediation guidance should be reviewed by a human analyst before operational use.
