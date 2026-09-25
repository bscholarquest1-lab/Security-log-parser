![Python application](https://github.com)
# Automated Security Log Parser

## Project Description
A lightweight Python automation tool engineered to parse server authentication logs, flag unauthorized intrusion vectors, isolate malicious IP addresses, and generate automated security incident summary reports.

## Features
- **Dynamic File I/O Operations:** Parses native target text files (`.log`) utilizing robust memory buffers instead of hardcoded strings.
- **Threat Isolation Architecture:** Audits raw data sequences to flag malicious access attempts, brute-force patterns, and privilege escalations.
- **Automated Report Generation:** Compiles findings dynamically into formal external audit files (`security_report.txt`) for Security Operation Center (SOC) review.

## Technical Skills Used
- Python Scripting & File Handling
- Automated Threat Detection
- Incident Analysis Logic
- Version Control (Git/GitHub)

## How To Run
To execute the log parser locally, ensure you have Python installed and run the following command in your terminal:
```bash
python log_parser.py
```

## Expected Output Report Preview (`security_report.txt`)
When executed, the script automatically generates an external audit report that looks like this:
```text
==================================================
AUTOMATED INCIDENT RESPONSE REPORT - [CURRENT DATE]
==================================================

[+] Total Malicious Events Flagged: 5
[+] Unique Offending IP Addresses Isolated: ['203.0.113.5', '198.51.100.12', '198.51.100.44']

--- DETAILED INCIDENT LOG ---
[ALERT] 2026-09-24 10:16:11 WARNING Invalid password attempt for user 'root' from 203.0.113.5
[ALERT] 2026-09-24 10:16:15 WARNING Invalid password attempt for user 'root' from 203.0.113.5
[ALERT] 2026-09-24 10:16:20 WARNING Invalid password attempt for user 'root' from 203.0.113.5
[ALERT] 2026-09-24 10:18:45 CRITICAL Database unauthorized access attempt from 198.51.100.12
[ALERT] 2026-09-24 11:02:14 WARNING Invalid password attempt for user 'guest' from 198.51.100.44
