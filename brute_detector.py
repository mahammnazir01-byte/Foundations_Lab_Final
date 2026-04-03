# The Counter: Starts at zero
attack_count = 0

# The Openers: "r" for reading the log, "w" for writing the report
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:

        # The Loop: Goes through the log line by line
        for line in log_file:

            # The Filter: Checks if "Failed password" is in the line
            if "Failed password" in line:
                
                # The Action: Writes that specific line to your report
                report_file.write(line)

                # The Math: Add 1 to our total count
                attack_count = attack_count + 1

# The Summary: This is NOT indented, so it runs only after the files close
print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")
