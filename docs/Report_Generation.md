# VibeSecSys Report Generation

## Version 1.0 Report Generation

The main application generates Markdown reports through `reporting/report_generator.py`.

The current report structure is:

```text
# VibeSecSys Security Report
## Summary of Findings
## Risks Identified
## Misconfigurations
## Recommendations
```

The report generator tries to extract these sections from AI output. If the expected headings are not found, it falls back to using the full AI output in each section.

Default output path:

```text
reports/report.md
```

Custom output path:

```powershell
python main.py --input samples\Vibe.xml --output reports\Vibe.md
```

## Stage 10 Reports

Stage 10 created one-time OCTAVE and STRIDE report documents.

Files:

- `docs/octave_stride_report.md`
- `docs/octave_stride_report_2.md`

These are generated documents, not currently a reusable report mode.

<span style="color:red">TODO</span> Add Stage 10 OCTAVE/STRIDE generation as a supported CLI option only if approved later.

## Version 2.0 Report Generation

Version 2.0 report generation is template-driven and currently experimental.

Templates:

- `V2.0/templates/full_report.txt`
- `V2.0/templates/vuln_classification.txt`
- `V2.0/templates/severity_assessment.txt`
- `V2.0/templates/mitigation_table.txt`
- `V2.0/templates/OCTAVE_STRIDE.txt`

Main experimental script:

- `V2.0/experiments/generate_full_report.py`

Generated reports:

- `V2.0/experiments/final_report.md`
- `V2.0/experiments/final_report_NEW.md`
- `V2.0/experiments/final_report_NEW_v2.md`
- `V2.0/experiments/final_report_NEW_v3.md`
- `V2.0/experiments/final_report_NEW_v4.md`

Latest refined Markdown report:

```text
V2.0/experiments/final_report_NEW_v4.md
```

## Report Output Types

| Output Type | Current Status |
|---|---|
| Markdown from main app | Implemented |
| Markdown OCTAVE/STRIDE documents | Generated as one-time Stage 10 outputs |
| Markdown V2.0 final report | Generated experimentally |
| PDF outputs | Present as generated experiment files, not main app functionality |
| HTML export | <span style="color:red">TODO</span> |
| Main app V2.0 report mode | <span style="color:red">TODO</span> |

## Known Report Generation Gaps

| Gap | Status |
|---|---|
| Section extraction depends on AI heading format | <span style="color:red">TODO</span> |
| Main report does not yet include structured tables | <span style="color:red">TODO</span> |
| V2.0 templates are not connected to `main.py` | <span style="color:red">TODO</span> |
| PDF generation is not implemented as a supported command | <span style="color:red">TODO</span> |
| No formal report version metadata in the main app report | <span style="color:red">TODO</span> |
