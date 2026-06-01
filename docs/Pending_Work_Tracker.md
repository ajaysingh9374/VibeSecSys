# VibeSecSys Pending Work Tracker

## Purpose

This tracker lists pending, incomplete, or not-yet-integrated work for VibeSecSys up to Version 2.0. These items are documented for future planning and should not be treated as implemented functionality.

Status marker:

<span style="color:red">TODO</span>

## Pending Work

| # | Area | Pending Work | Priority | Status | Notes |
|---|---|---|---|---|---|
| 1 | Version 2.0 Integration | Integrate Version 2.0 report generation into `main.py` | High | <span style="color:red">TODO</span> | Current V2.0 work exists under `V2.0/experiments/` |
| 2 | CLI | Add a CLI option for Version 2.0 report mode | High | <span style="color:red">TODO</span> | Possible future option: `--report-version 2` |
| 3 | Report Generation | Connect `V2.0/templates/` to a reusable report-generation workflow | High | <span style="color:red">TODO</span> | Templates are currently used experimentally |
| 4 | Data Model | Replace manual V2.0 row variables with structured XML-to-risk data generation | High | <span style="color:red">TODO</span> | Needed for repeatable reports from different XML inputs |
| 5 | OCTAVE/STRIDE | Add OCTAVE/STRIDE generation as an optional supported feature | Medium | <span style="color:red">TODO</span> | Stage 10 was one-time document generation |
| 6 | AI Configuration | Move AI model name and related settings into configuration | Medium | <span style="color:red">TODO</span> | Current model is fixed in code as `gpt-5.4-mini` |
| 7 | AI Reliability | Add retry, timeout, and clearer error handling for OpenAI calls | Medium | <span style="color:red">TODO</span> | Current failure output is generic |
| 8 | Prompt Management | Create a structured prompt registry or prompt documentation map | Medium | <span style="color:red">TODO</span> | Prompts exist across root, `prompts/`, and `V2.0/experiments/` |
| 9 | Report Export | Add supported PDF or HTML export workflow | Medium | <span style="color:red">TODO</span> | PDFs exist as generated artifacts, not main app output |
| 10 | Report Metadata | Add report version, analyst ID, reviewer, and date metadata to main app reports | Medium | <span style="color:red">TODO</span> | V2.0 report has richer metadata |
| 11 | Validation | Add report validation checks for required sections and table formatting | Medium | <span style="color:red">TODO</span> | Useful before generating final report files |
| 12 | Human Review | Add a documented or coded human validation workflow | Medium | <span style="color:red">TODO</span> | Reports state human validation is required |
| 13 | XML Handling | Add user-friendly handling for invalid or malformed XML | Medium | <span style="color:red">TODO</span> | Current XML parsing can fail without a tailored message |
| 14 | Testing | Add unit tests for XML loading, XML parsing, baseline analysis, and AI input preparation | Medium | <span style="color:red">TODO</span> | Needed before expanding the application |
| 15 | Testing | Add tests for Version 2.0 report assembly | Medium | <span style="color:red">TODO</span> | Needed before integrating V2.0 into main app |
| 16 | Logging | Replace or supplement print statements with structured logging | Low | <span style="color:red">TODO</span> | Current app uses console print statements |
| 17 | UI | Consider a future web or desktop interface | Low | <span style="color:red">TODO</span> | Current project is CLI/file-based |
| 18 | Documentation | Keep documentation updated after each future stage | Medium | <span style="color:red">TODO</span> | Current documentation covers up to V2.0 |

## Not Currently Planned for Immediate Coding

The following should remain pending until explicitly approved:

- Version 2.0 integration into the main application.
- PDF/HTML export.
- GUI or web interface.
- Human approval workflow implementation.
- Central configuration refactor.

## Review Notes

Use this tracker before starting the next development stage. Each item should be reviewed, prioritized, and converted into a specific stage/step prompt before coding begins.
