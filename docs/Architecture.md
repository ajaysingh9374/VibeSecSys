# VibeSecSys Architecture

## Current Architecture

VibeSecSys is currently a modular CLI application.

```text
User CLI
  |
  v
main.py
  |
  +-- scanner/scan_runner.py
  |     Select localhost scan or use XML input
  |
  +-- scanner/xml_loader.py
  |     Load XML file content
  |
  +-- scanner/xml_parser.py
  |     Parse host and port records
  |
  +-- scanner/baseline.py
  |     Generate baseline summary
  |
  +-- ai/data_preparation.py
  |     Build AI-ready scan context
  |
  +-- ai/ai_engine.py
  |     Call OpenAI
  |
  +-- reporting/report_generator.py
  |     Build Markdown report
  |
  +-- reporting/file_writer.py
        Save report to disk
```

## Data Flow

| Step | Input | Output |
|---|---|---|
| Scan or XML selection | CLI arguments | XML file path |
| XML loading | XML file path | XML text |
| XML parsing | XML text | List of hosts and ports |
| Baseline analysis | Parsed host data | Summary dictionary |
| AI preparation | Parsed host data and baseline summary | Plain text AI input |
| AI analysis | AI prompt | AI-generated analysis text |
| Report generation | AI-generated analysis text | Markdown report content |
| File output | Markdown report content and output path | Saved report file |

## Current Main Data Model

Parsed host data is represented as a list of dictionaries.

Example:

```text
[
  {
    "ip_address": "192.168.56.20",
    "ports": [
      {
        "port": "80",
        "service": "http",
        "state": "open"
      }
    ]
  }
]
```

Baseline summary is represented as:

```text
{
  "total_hosts": 1,
  "total_open_ports": 2,
  "discovered_services": ["http", "ssh"]
}
```

## Version 2.0 Experimental Architecture

Version 2.0 uses a template and placeholder approach.

```text
V2.0 sample XML / manually derived findings
  |
  v
V2.0 row blocks and section text
  |
  v
V2.0/templates/*.txt
  |
  v
V2.0/experiments/generate_full_report.py
  |
  v
V2.0/experiments/final_report_NEW*.md
```

<span style="color:red">TODO</span> The Version 2.0 architecture is not connected to the main Version 1.0 CLI architecture.

## Architecture Risks

| Risk | Status |
|---|---|
| AI response section extraction depends on expected headings | <span style="color:red">TODO</span> |
| V2.0 uses manual/experimental row variables instead of a reusable structured data model | <span style="color:red">TODO</span> |
| No central report configuration layer | <span style="color:red">TODO</span> |
| No formal separation between experimental report generation and production report generation | <span style="color:red">TODO</span> |
