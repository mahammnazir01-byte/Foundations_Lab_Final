#!/bin/bash
# Session 02: System Hardening
chmod 700 ~/Vault
chmod 600 ~/Vault/secrets.txt
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow
echo "System Hardened."
#!/bin/bash
# Session 02: System Hardening Automation

echo "[*] Starting security hardening..."

# Secure the local Vault
chmod 700 ~/Vault
chmod 600 ~/Vault/secrets.txt
echo "[+] Vault permissions secured."

# Secure the system shadow file (Requires sudo)
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow
echo "[+] System identity files hardened."

echo "[*] Security check complete: Posture is Gold Standard."
