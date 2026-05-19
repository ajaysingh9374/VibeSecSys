### Vulnerability Classification Table

| System | Vulnerability | Classification | Evidence-Based Impact |
|--------|--------------|----------------|----------------------|
| web-prod | SQL Injection | OWASP A03 | Data extraction from database |

### Vulnerability Severity and Impact Assessment

| ID | Target System | Vulnerability | Severity | Potential Impact |
|----|--------------|--------------|----------|------------------|
| VULN-001 | web-prod | SQL Injection | High | Data extraction from database |

### Mitigation Recommendations

| Vulnerability | Recommended Mitigation |
|---------------|----------------------|
| SQL Injection | Use parameterized queries, validate input, enforce least privilege |
