def save_report(report_content: str):
    print("Saving report to file...")

    file_path = "reports/report.md"
    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)

    print("Report saved successfully")
    return file_path
