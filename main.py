# Project: VibeSecSys
# Goal: Build a working cybersecurity application
# Execution: Strict step-by-step execution
# Co-development: CodeX + K2509118

from scanner.scan_runner import run_localhost_scan, select_scan_mode
from scanner.xml_loader import load_xml
from scanner.xml_parser import parse_xml


def main():
    print("HELLO WORLD")
    selected_mode = select_scan_mode()
    print(f"Returned scan mode: {selected_mode}")

    if selected_mode == "localhost":
        xml_file_path = run_localhost_scan()
        print(f"Generated XML path: {xml_file_path}")
        xml_content = load_xml(xml_file_path)
        print("XML content loaded into application")
        parsed_data = parse_xml(xml_content)
        print("Parsed scan summary:")
        for host in parsed_data:
            print(f"Host: {host['ip_address']}")
            print(f"Ports found: {len(host['ports'])}")
            for port in host["ports"]:
                print(
                    f"Port: {port['port']} | Service: {port['service']} | State: {port['state']}"
                )


if __name__ == "__main__":
    main()
