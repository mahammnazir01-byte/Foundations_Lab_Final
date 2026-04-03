#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# YOUR CODE HERE:


# INSTRUCTION 2: Search the captured output for the malicious process
# YOUR CODE HERE:


# INSTRUCTION 3: If found, create a dictionary and save it to 'security_alert.json'
# YOUR CODE HERE:


print("[+] Audit Complete.")
# Execute ps aux and capture the results as text
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)
# Check if the unauthorized process is in the captured output
if "unauthorized_cryptominer" in process_list.stdout:
# Create the high-severity alert
    alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": "unauthorized_cryptominer"
    }
    
    # Save the alert to a JSON file
    with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
    
    print("[!] THREAT DETECTED: alert saved to security_alert.json")

