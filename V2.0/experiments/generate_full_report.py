from pathlib import Path


VULN_CLASSIFICATION_ROWS = """| ASSET-001 | 192.168.56.20 | Exposed vsftpd 2.3.4 FTP Service | OWASP A06 Vulnerable and Outdated Components | FTP service on port 21 exposes vsftpd 2.3.4, creating risk of remote compromise and credential exposure |
| ASSET-001 | 192.168.56.20 | Exposed Telnet Service | OWASP A02 Cryptographic Failures | Telnet service on port 23 may transmit credentials in cleartext |
| ASSET-001 | 192.168.56.20 | Outdated OpenSSH Service | OWASP A06 Vulnerable and Outdated Components | OpenSSH 4.7p1 on port 22 indicates outdated remote administration exposure |
| ASSET-001 | 192.168.56.20 | Exposed Web and AJP Services | OWASP A05 Security Misconfiguration | Apache 2.2.8 on port 80, AJP13 on port 8009, and Tomcat/Coyote on port 8180 expose web and middleware attack surface |
| ASSET-001 | 192.168.56.20 | Exposed Samba NetBIOS Services | Service Misconfiguration | Samba services on ports 139 and 445 may enable enumeration, file-share abuse, and lateral movement |
| ASSET-001 | 192.168.56.20 | Exposed r-services | Service Misconfiguration | exec and login services on ports 512 and 513 expose insecure remote command and login pathways |
| ASSET-001 | 192.168.56.20 | Exposed Bindshell Service | Service Misconfiguration | Bash bindshell on port 1524 may allow direct shell access and full host compromise |
| ASSET-001 | 192.168.56.20 | Exposed NFS and rpcbind Services | Service Misconfiguration | rpcbind on port 111 and NFS on port 2049 may expose file shares and support lateral movement |
| ASSET-001 | 192.168.56.20 | Exposed Database Services | Service Misconfiguration | MySQL 5.0.51a on port 3306 and PostgreSQL 8.3.x on port 5432 expose database access to the network |
| ASSET-001 | 192.168.56.20 | Exposed VNC and X11 Services | Service Misconfiguration | VNC on port 5900 and X11 on port 6000 expose remote graphical access surfaces |
| ASSET-001 | 192.168.56.20 | Exposed Java RMI and IRC Services | OWASP A05 Security Misconfiguration | Java RMI on port 1099 and UnrealIRCd on port 6667 expose remote service interfaces that may be abused |
| ASSET-002 | 192.168.56.30 | Exposed SSH and HTTP Services | Service Misconfiguration | OpenSSH 9.6p1 on port 22 and Apache 2.4.58 on port 80 expose management and web services requiring hardening |
| ASSET-003 | 192.168.56.50 | Exposed Windows RPC and SMB Services | Service Misconfiguration | MSRPC on port 135, NetBIOS on port 139, and Microsoft-DS on port 445 expose Windows file-sharing and remote procedure services |"""
SEVERITY_ROWS = """| VULN-001 | ASSET-001 | 192.168.56.20 | Exposed vsftpd 2.3.4 FTP Service | Critical | Remote compromise risk and credential exposure from vulnerable FTP service | MIT-001 |
| VULN-002 | ASSET-001 | 192.168.56.20 | Exposed Telnet Service | High | Credential interception and unauthorized remote access | MIT-002 |
| VULN-003 | ASSET-001 | 192.168.56.20 | Outdated OpenSSH Service | Medium | Remote administration exposure with outdated service version | MIT-003 |
| VULN-004 | ASSET-001 | 192.168.56.20 | Exposed Web and AJP Services | High | Web application compromise, middleware abuse, and backend exposure | MIT-004 |
| VULN-005 | ASSET-001 | 192.168.56.20 | Exposed Samba NetBIOS Services | High | File-share enumeration, unauthorized access, and lateral movement | MIT-005 |
| VULN-006 | ASSET-001 | 192.168.56.20 | Exposed r-services | Critical | Unauthorized remote command execution and insecure login access | MIT-006 |
| VULN-007 | ASSET-001 | 192.168.56.20 | Exposed Bindshell Service | Critical | Direct shell access, full host compromise, and privilege escalation | MIT-007 |
| VULN-008 | ASSET-001 | 192.168.56.20 | Exposed NFS and rpcbind Services | High | Unauthorized file access and lateral movement through exposed file-sharing services | MIT-008 |
| VULN-009 | ASSET-001 | 192.168.56.20 | Exposed Database Services | High | Unauthorized database access and data exfiltration | MIT-009 |
| VULN-010 | ASSET-001 | 192.168.56.20 | Exposed VNC and X11 Services | High | Remote session compromise and unauthorized system interaction | MIT-010 |
| VULN-011 | ASSET-001 | 192.168.56.20 | Exposed Java RMI and IRC Services | High | Remote service abuse and potential exploitation of exposed interfaces | MIT-011 |
| VULN-012 | ASSET-002 | 192.168.56.30 | Exposed SSH and HTTP Services | Medium | Brute-force attempts, web exposure, and service-specific exploitation | MIT-012 |
| VULN-013 | ASSET-003 | 192.168.56.50 | Exposed Windows RPC and SMB Services | High | SMB enumeration, credential relay, lateral movement, and unauthorized file-sharing access | MIT-013 |"""
MITIGATION_ROWS = """| MIT-001 | Exposed vsftpd 2.3.4 FTP Service | Disable vulnerable FTP service or replace it with SFTP/FTPS and upgrade to a supported secure version |
| MIT-002 | Exposed Telnet Service | Disable Telnet and use SSH with strong authentication and restricted network access |
| MIT-003 | Outdated OpenSSH Service | Upgrade OpenSSH, disable weak algorithms, enforce key-based authentication, and restrict administrative access |
| MIT-004 | Exposed Web and AJP Services | Patch Apache and Tomcat components, restrict AJP to trusted internal hosts, and disable unused web services |
| MIT-005 | Exposed Samba NetBIOS Services | Restrict SMB and NetBIOS to trusted networks, disable anonymous access, and harden share permissions |
| MIT-006 | Exposed r-services | Disable exec and login services and replace them with hardened SSH-based administration |
| MIT-007 | Exposed Bindshell Service | Remove the bindshell immediately, isolate the host, and investigate for compromise |
| MIT-008 | Exposed NFS and rpcbind Services | Restrict NFS and rpcbind to approved hosts, enforce least-privilege exports, and block unnecessary access |
| MIT-009 | Exposed Database Services | Bind databases to trusted interfaces only, enforce strong authentication, patch database versions, and apply least privilege |
| MIT-010 | Exposed VNC and X11 Services | Restrict VNC and X11 to trusted networks or encrypted tunnels and enforce strong authentication |
| MIT-011 | Exposed Java RMI and IRC Services | Restrict Java RMI and IRC services, patch or remove unused components, and monitor for abuse |
| MIT-012 | Exposed SSH and HTTP Services | Harden SSH and HTTP services with patching, secure configuration, access control, and monitoring |
| MIT-013 | Exposed Windows RPC and SMB Services | Restrict RPC and SMB to trusted networks, enable SMB signing, patch Windows services, and disable unnecessary file-sharing exposure |"""
EXEC_SUMMARY = "The assessment identified a high-severity SQL Injection issue affecting web-prod, with evidence of database data extraction."
SYSTEM = "web-prod"
SCAN_SOURCE = "VibeSecSys v2.0 test data"
RISK_ROWS = "| web-prod | SQL Injection data extraction | Confidentiality loss and database compromise | High | High |"
CONCLUSION = "The identified SQL Injection vulnerability should be remediated as a priority through parameterized queries, input validation, and least-privilege database controls."


def read_template(path):
    return path.read_text(encoding="utf-8")


def replace_placeholders(content, replacements):
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    return content


def main():
    base_dir = Path(__file__).resolve().parent
    templates_dir = base_dir.parent / "templates"

    vuln_section = replace_placeholders(
        read_template(templates_dir / "vuln_classification.txt"),
        {"{VULN_CLASSIFICATION_ROWS}": VULN_CLASSIFICATION_ROWS},
    )
    severity_section = replace_placeholders(
        read_template(templates_dir / "severity_assessment.txt"),
        {"{SEVERITY_ROWS}": SEVERITY_ROWS},
    )
    mitigation_section = replace_placeholders(
        read_template(templates_dir / "mitigation_table.txt"),
        {"{MITIGATION_ROWS}": MITIGATION_ROWS},
    )

    report_content = replace_placeholders(
        read_template(templates_dir / "full_report.txt"),
        {
            "{EXEC_SUMMARY}": EXEC_SUMMARY,
            "{SYSTEM}": SYSTEM,
            "{SCAN_SOURCE}": SCAN_SOURCE,
            "{VULN_CLASSIFICATION_SECTION}": vuln_section.strip(),
            "{SEVERITY_SECTION}": severity_section.strip(),
            "{RISK_ROWS}": RISK_ROWS,
            "{MITIGATION_SECTION}": mitigation_section.strip(),
            "{CONCLUSION}": CONCLUSION,
        },
    )

    output_path = base_dir / "final_report.md"
    output_path.write_text(report_content, encoding="utf-8")


if __name__ == "__main__":
    main()
