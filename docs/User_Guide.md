# VibeSecSys User Guide

## Overview

VibeSecSys is currently used from the command line. It can run a localhost Nmap scan or process an existing Nmap XML file, send structured scan information to AI, and write a Markdown security report.

## Requirements

- Python environment with project dependencies installed.
- Nmap installed and available in the system path for localhost scanning.
- `.env` file containing `OPENAI_API_KEY` for OpenAI analysis.

The API key is loaded from the environment and should not be hardcoded in source files.

## Default Run

When no input file is provided, the application uses the localhost scan path.

```powershell
python main.py
```

Expected behavior:

1. Selects localhost mode.
2. Runs Nmap against `127.0.0.1`.
3. Saves XML scan output to `reports/localhost_scan.xml`.
4. Parses the XML.
5. Sends structured scan context to AI.
6. Saves the final Markdown report to `reports/report.md`.

## XML Input Mode

Use `--input` to analyze an existing Nmap XML file.

```powershell
python main.py --input samples\Vibe.xml
```

If the file path is invalid, the application prints a clear error message and exits.

## Custom Output File

Use `--output` to control where the Markdown report is saved.

```powershell
python main.py --input samples\Vibe.xml --output reports\Vibe.md
```

Default output:

```text
reports/report.md
```

## Common Output Files

| File | Description |
|---|---|
| `reports/report.md` | Default Markdown report |
| `reports/Vibe.md` | Example report generated from sample XML |
| `reports/new_report.md` | Report used as source for Stage 10 table-based OCTAVE/STRIDE output |
| `docs/octave_stride_report.md` | One-time OCTAVE/STRIDE generated report |
| `docs/octave_stride_report_2.md` | One-time OCTAVE/STRIDE generated report with tables |

## Current User-Facing Limitations

| Limitation | Status |
|---|---|
| No graphical user interface | <span style="color:red">TODO</span> |
| No built-in PDF export from the main application | <span style="color:red">TODO</span> |
| Version 2.0 final report generation is not exposed through `main.py` | <span style="color:red">TODO</span> |
| No interactive human approval workflow before using AI findings | <span style="color:red">TODO</span> |
