# VibeSecSys Version 2.0 Experimental Report Pipeline

## Purpose

Version 2.0 explores a richer cybersecurity assessment report format. The goal is to move beyond the simpler Version 1.0 AI report and produce a structured report containing executive summary, system overview, vulnerability classification, severity assessment, risk assessment, mitigation recommendations, and conclusion.

## Current Status

Version 2.0 is experimental.

It has generated working report artifacts, but it is not integrated into the main application.

<span style="color:red">TODO</span> Integrate Version 2.0 report generation into the CLI only after review and approval.

## Folder Structure

```text
V2.0/
  samples/
  templates/
  experiments/
```

## Inputs

Primary sample XML files:

- `V2.0/samples/Vibe.xml`
- `V2.0/samples/VibeSecSys.xml`

Important scan scope identified from `V2.0/samples/VibeSecSys.xml`:

| Host | Description |
|---|---|
| `192.168.56.20` | `filesrv01`, broad multi-service server profile |
| `192.168.56.30` | `web-prod`, SSH and HTTP service profile |
| `192.168.56.50` | Windows-oriented RPC, NetBIOS, and SMB services |

## Templates

| Template | Purpose |
|---|---|
| `full_report.txt` | Main report skeleton |
| `vuln_classification.txt` | Vulnerability classification table section |
| `severity_assessment.txt` | Severity assessment table section |
| `mitigation_table.txt` | Mitigation recommendation table section |
| `OCTAVE_STRIDE.txt` | OCTAVE/STRIDE related template asset |

## Experiment Scripts and Prompt Files

| File | Purpose |
|---|---|
| `test_rows_prompt.txt` | Tests row formatting expectations |
| `generate_injection_script.txt` | Prompt to generate template injection script |
| `inject_template_rows.py` | Script for injecting rows into templates |
| `generate_full_report_script.txt` | Prompt to generate full report script |
| `generate_full_report.py` | Experimental full report assembly script |
| `generate_rows_from_xml.txt` | Prompt for creating rows from XML |
| `generate_rows_v2_final.txt` | Prompt for final Version 2.0 row generation |
| `fix_formatting_rows.txt` | Prompt for row formatting cleanup |
| `insert_final_rows_into_report.txt` | Prompt for inserting final rows |
| `SYSTEM_script.txt` | Prompt for system overview content |
| `SCAN_SOURCE_script.txt` | Prompt for scan source content |
| `RISK_ROWS_script.txt` | Prompt for risk rows |
| `EXEC_SUMMARY_script.txt` | Prompt for executive summary |
| `CONCLUSION_script.txt` | Prompt for conclusion |
| `FINAL_REPORT_MD.txt` and `FINAL_REPORT_MD1.txt` | Prompts for final report assembly |
| `ReportRefinement.txt` | First report refinement prompt |
| `ReportRefinement_01.txt` | Second report refinement prompt |
| `ReportRefinement_02.txt` | Final presentation refinement prompt |

## Generated Reports

| File | Description |
|---|---|
| `final_report.md` | Early template test report |
| `final_report_NEW.md` | Assembled richer report |
| `final_report_NEW_v2.md` | Report with table separator formatting fixed |
| `final_report_NEW_v3.md` | Report with report information and restructured system overview |
| `final_report_NEW_v4.md` | Latest refined Markdown report with CSS and inline report information |

## Latest Version 2.0 Output

```text
V2.0/experiments/final_report_NEW_v4.md
```

This is the latest refined Markdown report. It includes styling, report information, executive summary, system overview, vulnerability classification, severity assessment, risk assessment, mitigation recommendations, and conclusion.

## Boundaries

Version 2.0 currently should be treated as evidence of design direction and experimentation.

Not yet implemented as production application behavior:

- Calling Version 2.0 report generation from `main.py`.
- Selecting Version 2.0 output through CLI arguments.
- Automatically parsing all V2.0 fields into a reusable structured risk model.
- Automatic PDF generation from the main application.
- Human approval workflow for final report release.
