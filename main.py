# Project: VibeSecSys
# Goal: Build a working cybersecurity application
# Execution: Strict step-by-step execution
# Co-development: CodeX + K2509118

from scanner.scan_runner import select_scan_mode


def main():
    print("HELLO WORLD")
    selected_mode = select_scan_mode()
    print(f"Returned scan mode: {selected_mode}")


if __name__ == "__main__":
    main()
