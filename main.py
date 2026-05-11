# Project: VibeSecSys
# Goal: Build a working cybersecurity application
# Execution: Strict step-by-step execution
# Co-development: CodeX + K2509118

from scanner.scan_runner import run_localhost_scan, select_scan_mode


def main():
    print("HELLO WORLD")
    selected_mode = select_scan_mode()
    print(f"Returned scan mode: {selected_mode}")

    if selected_mode == "localhost":
        xml_file_path = run_localhost_scan()
        print(f"Generated XML path: {xml_file_path}")


if __name__ == "__main__":
    main()
