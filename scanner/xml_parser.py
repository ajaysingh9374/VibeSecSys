import xml.etree.ElementTree as ET


def parse_xml(xml_content: str):
    print("Parsing XML data...")

    root = ET.fromstring(xml_content)
    parsed_data = []

    for host in root.findall("host"):
        address = host.find("address")
        ip_address = address.get("addr", "unknown") if address is not None else "unknown"
        host_data = {
            "ip_address": ip_address,
            "ports": [],
        }

        ports = host.find("ports")
        if ports is not None:
            for port in ports.findall("port"):
                state = port.find("state")
                service = port.find("service")
                host_data["ports"].append(
                    {
                        "port": port.get("portid", "unknown"),
                        "service": service.get("name", "unknown") if service is not None else "unknown",
                        "state": state.get("state", "unknown") if state is not None else "unknown",
                    }
                )

        parsed_data.append(host_data)

    print("XML parsing complete")
    return parsed_data
