from pathlib import Path


VULN_CLASSIFICATION_ROWS = "| web-prod | SQL Injection | OWASP A03 | Data extraction from database |"
SEVERITY_ROWS = "| VULN-001 | web-prod | SQL Injection | High | Data extraction from database |"
MITIGATION_ROWS = "| SQL Injection | Use parameterized queries, validate input, enforce least privilege |"


def read_template(path):
    return path.read_text(encoding="utf-8")


def inject_rows(template_content, placeholder, rows):
    return template_content.replace(placeholder, rows)


def main():
    base_dir = Path(__file__).resolve().parent
    templates_dir = base_dir.parent / "templates"

    vuln_template = read_template(templates_dir / "vuln_classification.txt")
    severity_template = read_template(templates_dir / "severity_assessment.txt")
    mitigation_template = read_template(templates_dir / "mitigation_table.txt")

    vuln_section = inject_rows(
        vuln_template,
        "{VULN_CLASSIFICATION_ROWS}",
        VULN_CLASSIFICATION_ROWS,
    )
    severity_section = inject_rows(
        severity_template,
        "{SEVERITY_ROWS}",
        SEVERITY_ROWS,
    )
    mitigation_section = inject_rows(
        mitigation_template,
        "{MITIGATION_ROWS}",
        MITIGATION_ROWS,
    )

    report_content = "\n\n".join(
        [
            vuln_section.strip(),
            severity_section.strip(),
            mitigation_section.strip(),
        ]
    )

    output_path = base_dir / "final_report.md"
    output_path.write_text(report_content + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
