# VibeSecSys AI Usage

## Purpose of AI Usage

AI is used to convert structured scan context into readable cybersecurity analysis. The current AI output is used to generate report sections such as summary, risks, misconfigurations, and recommendations.

## Main Application AI Flow

1. Parsed scan data and baseline summary are prepared by `ai/data_preparation.py`.
2. `ai/ai_engine.py` builds a cybersecurity analysis prompt.
3. The OpenAI client sends the prompt to the configured model.
4. The response text is returned to `main.py`.
5. `reporting/report_generator.py` converts the AI response into Markdown sections.

## API Key Handling

The project uses `.env` loading through `python-dotenv`.

Expected environment variable:

```text
OPENAI_API_KEY
```

The API key should not be hardcoded in source code.

## Current Model

```text
gpt-5.4-mini
```

## Stage 10 AI Usage

Stage 10 used AI as a one-time document generation step. Source reports were sent to AI to generate formal OCTAVE and STRIDE reports.

Generated files:

- `docs/octave_stride_report.md`
- `docs/octave_stride_report_2.md`

Important boundary:

Stage 10 is not currently implemented as a reusable feature in the main application.

<span style="color:red">TODO</span> Add a formal application option if OCTAVE/STRIDE generation should become a supported feature.

## Version 2.0 AI Usage

Version 2.0 used AI-assisted reasoning and staged prompts to create:

- System overview text.
- Scan source text.
- Executive summary.
- Risk rows.
- Conclusion.
- Report refinement instructions.

These outputs were used to assemble richer Markdown reports in `V2.0/experiments/`.

Important boundary:

<span style="color:red">TODO</span> Version 2.0 AI-assisted report generation is not yet automated inside `main.py`.

## Human Validation

AI-generated cybersecurity content should be reviewed by a human analyst before use.

Validation should check:

- Whether findings are supported by scan evidence.
- Whether risk severity is reasonable.
- Whether mitigations are appropriate.
- Whether the report avoids invented hosts, services, or vulnerabilities.
- Whether final recommendations are safe and actionable.

## AI-Related Future Work

| Item | Status |
|---|---|
| Store prompts in a structured prompt registry | <span style="color:red">TODO</span> |
| Add configurable model name instead of fixed code value | <span style="color:red">TODO</span> |
| Add retry and timeout handling for API calls | <span style="color:red">TODO</span> |
| Add clear error detail without exposing secrets | <span style="color:red">TODO</span> |
| Add deterministic JSON or schema-based AI output for report generation | <span style="color:red">TODO</span> |
