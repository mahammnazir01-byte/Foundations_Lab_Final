#!/usr/bin/env python3
import subprocess
import json

print("[*] Initiating Automated Threat Hunt...")

# TASK 1: Use subprocess to grep for "Failed password" in /var/log/titan_sim/auth_sim.log
# Ensure you capture the output and convert it to text!
# YOUR CODE HERE:


# TASK 2: Parse the captured output to extract ONLY the attacking IP addresses.
# Hint: Loop through each line, split the line by spaces, and grab index [10].
# Save the IPs to a Python List called attacker_ips.
# YOUR CODE HERE:


# TASK 3: Create a dictionary containing the extracted IPs and export it to 'threat_report.json'
# Dictionary format: {"alert_type": "Brute Force", "attacker_ips": attacker_ips}
# YOUR CODE HERE:


print("[+] Threat Hunt Complete. Report generated.")
import subprocess
import json

# PHASE 1: LOG INTERROGATION
# Using Linux 'grep' to find all failed password attempts in the log
result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# PHASE 2: DATA PARSING
# Split the big block of text into a list of strings (one per line)
lines = raw_output.strip().split('\n')

attacker_ips = []

for line in lines:
    if line:
        # In this specific log format, the IP address is at index 10 
        # (the 11th word) when splitting by spaces
        parts = line.split(" ")
        if len(parts) > 10:
            ip = parts[10]
            attacker_ips.append(ip)

# PHASE 3: THE EXPORT
# Put the list into a structured dictionary
alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": list(set(attacker_ips)) # 'set' removes duplicates for a cleaner report
}

# Write the data to your JSON artifact
with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print(f"[*] Analysis Complete. {len(attacker_ips)} incidents logged to threat_report.json")
