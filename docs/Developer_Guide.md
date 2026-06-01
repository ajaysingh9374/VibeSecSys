# VibeSecSys Developer Guide

## Project Structure

```text
VibeSecSys/
  ai/
  docs/
  prompts/
  reporting/
  reports/
  samples/
  scanner/
  V2.0/
  main.py
  requirements.txt
```

## Main Entry Point

`main.py` controls the Version 1.0 application flow.

Responsibilities:

- Parse CLI arguments.
- Select XML input or localhost scan mode.
- Validate input file path.
- Load XML content.
- Parse scan data.
- Generate baseline summary.
- Prepare AI input.
- Call AI analysis.
- Generate Markdown report.
- Save report output.

## Scanner Module

| File | Responsibility |
|---|---|
| `scanner/scan_runner.py` | Selects scan mode and runs localhost Nmap XML scan |
| `scanner/xml_loader.py` | Reads XML file content |
| `scanner/xml_parser.py` | Parses Nmap XML into host and port data |
| `scanner/baseline.py` | Calculates host count, open port count, and discovered services |

## AI Module

| File | Responsibility |
|---|---|
| `ai/data_preparation.py` | Converts parsed data and baseline data into AI-ready text |
| `ai/ai_engine.py` | Loads `.env`, prepares analysis prompt, and calls OpenAI |

Current model:

```text
gpt-5.4-mini
```

## Reporting Module

| File | Responsibility |
|---|---|
| `reporting/report_generator.py` | Extracts sections from AI output and creates Markdown report content |
| `reporting/file_writer.py` | Writes report content to disk |

## Version 2.0 Development Area

`V2.0/` contains the experimental richer report pipeline.

| Folder | Responsibility |
|---|---|
| `V2.0/samples/` | Version 2.0 sample XML input files |
| `V2.0/templates/` | Report section templates |
| `V2.0/experiments/` | Prompt files, scripts, generated Markdown reports, and generated PDFs |

Important boundary:

<span style="color:red">TODO</span> Version 2.0 scripts and templates are not yet integrated into the main application. They should be treated as experimental development assets until a deliberate integration stage is started.

## Development Rules Used So Far

- Keep API keys out of code.
- Use `.env` for `OPENAI_API_KEY`.
- Keep generated reports in `reports/`, `docs/`, or `V2.0/experiments/` depending on purpose.
- Keep staged prompt files in `prompts/` or `V2.0/experiments/`.
- Do not integrate experimental work into `main.py` until explicitly approved.

## Suggested Future Development Direction

| Future Work | Status |
|---|---|
| Add a formal V2 report-generation command | <span style="color:red">TODO</span> |
| Add a central config file for model, report version, analyst ID, and template paths | <span style="color:red">TODO</span> |
| Add tests for XML parsing, AI input generation, and report assembly | <span style="color:red">TODO</span> |
| Add structured logging instead of print-only output | <span style="color:red">TODO</span> |
| Add graceful handling for invalid XML parse errors | <span style="color:red">TODO</span> |
