import subprocess


SUPPORTED_SCAN_MODES = ("localhost", "network", "xml")


def select_scan_mode():
    selected_mode = "localhost"
    print("Scan mode selected: localhost")
    return selected_mode


def run_localhost_scan():
    xml_file_path = "reports/localhost_scan.xml"
    command = ["nmap", "-oX", xml_file_path, "127.0.0.1"]

    print("Running localhost scan...")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error:
        print(f"Nmap scan failed with exit code {error.returncode}.")
        raise SystemExit(1)
    except FileNotFoundError:
        print("Nmap scan failed: nmap command was not found.")
        raise SystemExit(1)

    print(f"Scan complete. XML saved to: {xml_file_path}")
    return xml_file_path
