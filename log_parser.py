
import datetime

# Mock log data to simulate a server security log
mock_log_data = """
2026-09-24 10:15:32 INFO User 'admin' logged in successfully from 192.168.1.50
2026-09-24 10:16:11 WARNING Invalid password attempt for user 'root' from 203.0.113.5
2026-09-24 10:16:15 WARNING Invalid password attempt for user 'root' from 203.0.113.5
2026-09-24 10:16:20 WARNING Invalid password attempt for user 'root' from 203.0.113.5
2026-09-24 10:17:01 INFO User 'unixguy' logged in successfully from 192.168.1.22
2026-09-24 10:18:45 CRITICAL Database unauthorized access attempt from 198.51.100.12
"""

def analyze_security_logs():
    print(f"=== CYBERSECURITY LOG ANALYSIS REPORT ({datetime.date.today()}) ===")
    lines = mock_log_data.strip().split('\n')
    
    failed_attempts = 0
    suspicious_ips = set()
    
    for line in lines:
        # Scan for high-risk security keywords
        if "Invalid password attempt" in line or "unauthorized access" in line:
            failed_attempts += 1
            # Extract the IP address (the last item in the log entry)
            ip_address = line.split()[-1]
            suspicious_ips.add(ip_address)
            print(f"[ALERT] Security Incident Found: {line}")

    print("\n=== SYSTEM METRICS SUMMARY ===")
    print(f"Total Security Alerts Flagged: {failed_attempts}")
    print(f"Flagged Suspicious IP Addresses: {list(suspicious_ips)}")

if __name__ == "__main__":
    analyze_security_logs()
