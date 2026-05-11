def _extract_section(ai_output: str, headings: tuple[str, ...]):
    lines = ai_output.splitlines()
    captured_lines = []
    capturing = False

    for line in lines:
        normalized = line.strip().lower().strip("#").strip()
        is_heading = normalized in headings

        if is_heading:
            capturing = True
            continue

        if capturing and normalized.startswith(("summary", "identified", "risks", "misconfigurations", "recommendations")):
            break

        if capturing:
            captured_lines.append(line)

    return "\n".join(captured_lines).strip()


def generate_report(ai_output: str):
    print("Generating report...")

    clean_ai_output = str(ai_output).strip()
    summary = _extract_section(clean_ai_output, ("summary of findings", "summary"))
    risks = _extract_section(clean_ai_output, ("identified risks", "risks identified", "risks"))
    misconfigurations = _extract_section(clean_ai_output, ("misconfigurations",))
    recommendations = _extract_section(clean_ai_output, ("recommendations",))

    if not any((summary, risks, misconfigurations, recommendations)):
        summary = clean_ai_output
        risks = clean_ai_output
        misconfigurations = clean_ai_output
        recommendations = clean_ai_output

    report_content = "\n\n".join(
        [
            "# VibeSecSys Security Report",
            "## Summary of Findings\n\n" + (summary or clean_ai_output),
            "## Risks Identified\n\n" + (risks or clean_ai_output),
            "## Misconfigurations\n\n" + (misconfigurations or clean_ai_output),
            "## Recommendations\n\n" + (recommendations or clean_ai_output),
        ]
    )

    print("Report generation complete")
    return report_content
