# Cybersecurity Analysis Report

---

## 1. Executive Summary
The assessment identified an elevated overall risk posture across three systems, with the greatest concern concentrated on 192.168.56.20 due to multiple critical and high-risk exposures involving legacy services, remote access pathways, database access, file-sharing services, and shell-like access. The environment also includes a smaller web-facing system at 192.168.56.30 with moderate exposure and a Windows-oriented host at 192.168.56.50 with high-risk RPC and SMB-related exposure. Priority remediation should focus on reducing unnecessary services, removing critical remote access risks, restricting exposed services to trusted networks, and hardening authentication and monitoring controls.

---

## 2. System Overview
- Target System: The assessment scope consists of three systems within the 192.168.56.0/24 network segment: 192.168.56.20, 192.168.56.30, and 192.168.56.50. The host at 192.168.56.20 is identified as filesrv01 and presents a broad multi-service server profile, including remote access, file-sharing, database, web, naming, and administrative service functions. The host at 192.168.56.30 is identified as web-prod and presents a focused service profile consistent with a web-facing system offering SSH and HTTP services. The host at 192.168.56.50 presents characteristics of a Windows-based system, with Microsoft RPC, NetBIOS, and Microsoft-DS services exposed. Overall, the assessed environment represents a mixed service landscape containing Linux/Unix-style server functions, a web production host, and a Windows-oriented network service host.
- Scan Source: The scan source is an Nmap 7.92 XML output file generated using service/version detection and default script scanning. The scan data was collected in XML format from the targets filesrv01, web-prod, and 192.168.56.50, then processed to identify assessed hosts, open ports, exposed services, service metadata, and related security observations for reporting.

---

## 3. Vulnerability Classification

### Vulnerability Classification Table

| Asset ID | System | Vulnerability | Classification | Evidence-Based Impact |
|---|---|---|---|---|
| ASSET-001 | 192.168.56.20 | Exposed vsftpd 2.3.4 FTP Service | OWASP A06 Vulnerable and Outdated Components | FTP service on port 21 exposes vsftpd 2.3.4, creating risk of remote compromise and credential exposure |
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
| ASSET-003 | 192.168.56.50 | Exposed Windows RPC and SMB Services | Service Misconfiguration | MSRPC on port 135, NetBIOS on port 139, and Microsoft-DS on port 445 expose Windows file-sharing and remote procedure services |

---

## 4. Severity Assessment

### Vulnerability Severity and Impact Assessment

| VULN ID | Asset ID | Target System | Vulnerability | Severity | Potential Impact | Mitigation ID |
|---|---|---|---|---|---|---|
| VULN-001 | ASSET-001 | 192.168.56.20 | Exposed vsftpd 2.3.4 FTP Service | Critical | Remote compromise risk and credential exposure from vulnerable FTP service | MIT-001 |
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
| VULN-013 | ASSET-003 | 192.168.56.50 | Exposed Windows RPC and SMB Services | High | SMB enumeration, credential relay, lateral movement, and unauthorized file-sharing access | MIT-013 |

---

## 5. Risk Assessment (OCTAVE / STRIDE)

| Asset | Threat | Impact | Likelihood | Risk Level |
|------|--------|--------|------------|------------|
| ASSET-001 | Legacy and vulnerable service exposure | Credential theft, unauthorized remote access, lateral movement, and host compromise | High | Critical |
| ASSET-001 | Exposed database services | Unauthorized database access, data exfiltration, and integrity compromise | High | High |
| ASSET-001 | Exposed file-sharing and remote administration services | Unauthorized file access, remote command execution, and privilege escalation | High | Critical |
| ASSET-001 | Exposed web and middleware services | Web application compromise, backend service abuse, and remote exploitation | Medium | High |
| ASSET-002 | Exposed SSH and HTTP services | Brute-force attempts, web service exploitation, and unauthorized access | Medium | Medium |
| ASSET-003 | Exposed Windows RPC and SMB services | SMB enumeration, credential relay, unauthorized file-sharing access, and lateral movement | High | High |

---

## 6. Mitigation Recommendations

### Mitigation Recommendations

| MIT ID | Vulnerability | Recommended Mitigation |
|---|---|---|
| MIT-001 | Exposed vsftpd 2.3.4 FTP Service | Disable vulnerable FTP service or replace it with SFTP/FTPS and upgrade to a supported secure version |
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
| MIT-013 | Exposed Windows RPC and SMB Services | Restrict RPC and SMB to trusted networks, enable SMB signing, patch Windows services, and disable unnecessary file-sharing exposure |

---

## 7. Conclusion

The assessed environment demonstrates a security posture that requires prioritised remediation, particularly around the concentration of critical and high-risk exposures on 192.168.56.20. The presence of legacy protocols, exposed administrative services, database access, file-sharing services, and shell-like access pathways substantially increases the likelihood of unauthorised access, credential compromise, lateral movement, and service abuse. Remediation should therefore focus first on removing unnecessary and high-risk services, restricting access to trusted networks, strengthening authentication, patching outdated components, and improving monitoring. Addressing these areas will reduce the attack surface and improve the resilience of the assessed environment.
