def generate_baseline(parsed_data):
    print("Running baseline analysis...")

    hosts = parsed_data if isinstance(parsed_data, list) else []
    open_ports = 0
    discovered_services = set()

    for host in hosts:
        if not isinstance(host, dict):
            continue

        ports = host.get("ports", [])
        if not isinstance(ports, list):
            continue

        for port in ports:
            if not isinstance(port, dict):
                continue

            if port.get("state") == "open":
                open_ports += 1

            service = port.get("service")
            if service and service != "unknown":
                discovered_services.add(service)

    baseline_summary = {
        "total_hosts": len(hosts),
        "total_open_ports": open_ports,
        "discovered_services": sorted(discovered_services),
    }

    print("Baseline analysis complete")
    return baseline_summary
