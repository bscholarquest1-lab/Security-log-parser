import os
import datetime

def parse_log_file(input_file, output_report):
    if not os.path.exists(input_file):
        print(f"[ERROR] Target log file '{input_file}' not found.")
        return

    print(f"[*] Processing security metrics from {input_file}...")
    
    failed_attempts = 0
    suspicious_ips = set()
    alert_lines = []

    # Open and process the input raw log file
    with open(input_file, 'r') as file:
        for line in file:
            if "Invalid password attempt" in line or "unauthorized access" in line:
                failed_attempts += 1
                ip_address = line.strip().split()[-1]
                suspicious_ips.add(ip_address)
                alert_lines.append(f"[ALERT] {line.strip()}")

    # Generate an external text file report summary
    with open(output_report, 'w') as report:
        report.write(f"==================================================\n")
        report.write(f"AUTOMATED INCIDENT RESPONSE REPORT - {datetime.date.today()}\n")
        report.write(f"==================================================\n\n")
        
        report.write(f"[+] Total Malicious Events Flagged: {failed_attempts}\n")
        report.write(f"[+] Unique Offending IP Addresses Isolated: {list(suspicious_ips)}\n\n")
        
        report.write(f"--- DETAILED INCIDENT LOG ---\n")
        for alert in alert_lines:
            report.write(f"{alert}\n")
            
    print(f"[SUCCESS] Analysis complete. Security report generated: '{output_report}'")

if __name__ == "__main__":
    # Define file path variables
    LOG_FILE = "server_access.log"
    REPORT_FILE = "security_report.txt"
    
    parse_log_file(LOG_FILE, REPORT_FILE)

