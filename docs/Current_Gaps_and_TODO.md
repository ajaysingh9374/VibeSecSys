# VibeSecSys Current Gaps and TODO Items

## Purpose

This document lists work that is known but not yet coded, integrated, tested, or finalized. These items are intentionally documented for later planning.

## Main Application TODOs

| Item | Status | Notes |
|---|---|---|
| Add Version 2.0 report generation to `main.py` | <span style="color:red">TODO</span> | V2.0 exists as experiments only |
| Add CLI option for V2.0 report mode | <span style="color:red">TODO</span> | Example future option could be `--report-version 2` |
| Add CLI option for OCTAVE/STRIDE generation | <span style="color:red">TODO</span> | Stage 10 was one-time generation only |
| Add PDF export command | <span style="color:red">TODO</span> | PDFs exist from experiments but are not app-generated |
| Add central configuration file | <span style="color:red">TODO</span> | Model, report metadata, template paths, default output path |
| Add structured logging | <span style="color:red">TODO</span> | Current application uses print statements |
| Add invalid XML handling | <span style="color:red">TODO</span> | XML parse errors should be user-friendly |

## AI TODOs

| Item | Status | Notes |
|---|---|---|
| Make model configurable | <span style="color:red">TODO</span> | Current code uses `gpt-5.4-mini` directly |
| Add retries and timeouts | <span style="color:red">TODO</span> | API failure currently returns generic failure text |
| Add schema-based AI output | <span style="color:red">TODO</span> | Would reduce fragile section extraction |
| Add no-secret error handling | <span style="color:red">TODO</span> | Errors should be clear without exposing API key details |
| Add formal prompt registry | <span style="color:red">TODO</span> | Prompts exist as text files but are not centrally managed |

## Report Generation TODOs

| Item | Status | Notes |
|---|---|---|
| Integrate V2.0 templates into app workflow | <span style="color:red">TODO</span> | Templates currently live under `V2.0/templates/` |
| Replace manual row variables with structured data generation | <span style="color:red">TODO</span> | Current V2 rows are stored in experimental script variables |
| Add report metadata to main app reports | <span style="color:red">TODO</span> | V2 has report information, main app does not |
| Add report validation checks | <span style="color:red">TODO</span> | Could verify required sections and table formatting |
| Add consistent styling/export strategy | <span style="color:red">TODO</span> | V2 Markdown uses CSS, main app report does not |

## Testing TODOs

| Item | Status | Notes |
|---|---|---|
| Unit tests for XML loader/parser | <span style="color:red">TODO</span> | Useful for malformed or partial Nmap XML |
| Unit tests for baseline analysis | <span style="color:red">TODO</span> | Check no-port, few-port, and multi-host cases |
| Unit tests for AI input preparation | <span style="color:red">TODO</span> | Confirm consistent output format |
| Tests for report generator fallback behavior | <span style="color:red">TODO</span> | Important when AI headings vary |
| Tests for V2.0 report assembly | <span style="color:red">TODO</span> | Needed before integration |

## Version 2.0 TODOs

| Item | Status | Notes |
|---|---|---|
| Decide whether V2.0 becomes main report format | <span style="color:red">TODO</span> | Needs review of output quality |
| Convert V2.0 experiments into reusable modules | <span style="color:red">TODO</span> | Avoid keeping logic only in experiment scripts |
| Add structured XML-to-risk extraction | <span style="color:red">TODO</span> | Needed for reliable repeatable reports |
| Add human validation workflow | <span style="color:red">TODO</span> | Reports already state validation is required |
| Add PDF/HTML generation workflow | <span style="color:red">TODO</span> | Current PDF files are generated artifacts |

## Not Coded Yet Summary

The following are not currently coded as main application features:

- Version 2.0 full report mode.
- OCTAVE/STRIDE report mode.
- PDF export mode.
- Human review/approval workflow.
- Central configuration.
- Formal test suite for Version 2.0.
- Structured risk object model.
- GUI or web interface.

These items are documented for later planning and should not be treated as implemented functionality.
