def prepare_ai_input(parsed_data, baseline_data):
    print("Preparing data for AI analysis...")

    hosts = parsed_data if isinstance(parsed_data, list) else []
    services = baseline_data.get("discovered_services", []) if isinstance(baseline_data, dict) else []

    lines = [
        "VibeSecSys AI Input",
        "",
        "Host Details:",
    ]

    if hosts:
        for host in hosts:
            ip_address = host.get("ip_address", "unknown") if isinstance(host, dict) else "unknown"
            ports = host.get("ports", []) if isinstance(host, dict) else []

            lines.append(f"- Host: {ip_address}")
            lines.append(f"  Open Ports:")

            open_ports = [
                port for port in ports
                if isinstance(port, dict) and port.get("state") == "open"
            ]

            if open_ports:
                for port in open_ports:
                    lines.append(
                        f"  - Port {port.get('port', 'unknown')}: "
                        f"{port.get('service', 'unknown')} ({port.get('state', 'unknown')})"
                    )
            else:
                lines.append("  - None")
    else:
        lines.append("- No hosts discovered")

    lines.extend(
        [
            "",
            "Services:",
            f"- {', '.join(services) if services else 'None'}",
            "",
            "Baseline Summary:",
            f"- Total hosts: {baseline_data.get('total_hosts', 0) if isinstance(baseline_data, dict) else 0}",
            f"- Total open ports: {baseline_data.get('total_open_ports', 0) if isinstance(baseline_data, dict) else 0}",
            f"- Discovered services: {', '.join(services) if services else 'None'}",
        ]
    )

    ai_input = "\n".join(lines)

    print("AI input preparation complete")
    return ai_input
