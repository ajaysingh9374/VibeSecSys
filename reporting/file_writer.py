def save_report(report_content: str, file_path: str = "reports/report.md"):
    print("Saving report to file...")

    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_content)

    print("Report saved successfully")
    return file_path
