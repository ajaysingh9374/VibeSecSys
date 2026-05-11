def load_xml(xml_file_path: str):
    print(f"Loading XML from: {xml_file_path}")

    try:
        with open(xml_file_path, "r", encoding="utf-8") as xml_file:
            xml_content = xml_file.read()
    except FileNotFoundError:
        print("Error: XML file not found")
        raise SystemExit(1)

    print("XML loaded successfully")
    return xml_content
