# 📊 Phase 2: SIEM Dashboard Analysis

## 🔧 SIEM Setup

In this phase, we integrated logs from both the **victim** and **attacker** environments into **Splunk**, our chosen SIEM tool. This step enables central analysis, threat detection, and deeper insight into attacker behavior.

> 📸 *Screenshot A: Uploading system-journal.log into Splunk (Attacker logs)*  
![Screenshot A](Screenshots/A.png)


### ✅ Logs Integrated: ("logs from both environments") 
- **Victim (Metasploitable3)**: Apache access logs (`access.log`)
- **Attacker (Kali Linux)**: System journal logs (`system-journal.log`)


-
> 📸 *Screenshot C: Uploading `system-journal.log` into Splunk (Attacker logs)*
![Screenshot C](./Screenshots/C.png)

---

### 📊 Log

Once both log files were uploaded, we used Splunk's **Search & Reporting** app to:


> 📸 *Screenshot B: Splunk main dashboard after logging in successfully*
![Screenshot B](./Screenshots/B.png)

> 📸 *Screenshot D: Querying `system-journal.log` inside Splunk*
![Screenshot D](./Screenshots/D.png)


### Now Lets transfer the "access.log" to kali and upload it to splunk 
> 📸 *Screenshot E: Setting up local Python server on Metasploitable3 to share the log file*
![Screenshot E](./Screenshots/E.png)

> 📸 *Screenshot F: SCP command on Kali to download the log from the victim*
![Screenshot F](./Screenshots/F.png)

> 📸 *Screenshot G: Log file successfully transferred to Kali*
![Screenshot G](./Screenshots/G.png)

> 📸 *Screenshot H: Uploading Apache `access.log` into Splunk*
![Screenshot H](./Screenshots/H.png)
>
> ## 🧠 Attack Analysis & Pattern Detection

In this section, we deep-dive into Splunk’s powerful analytics capabilities to uncover meaningful patterns that shed light on the attack behavior. Our focus was to:

- Identify **frequently accessed endpoints**
- Determine **malicious IP activity**
- Highlight trends in attacker interaction with the system

---

### 📊 Attack Pattern Visualization

To detect potential malicious behavior, we ran pattern analysis on the `access_combined` logs. Splunk’s pattern detection grouped similar request patterns together, making it easier to visually spot suspicious actions.

> 🖼 *Screenshot: Request pattern analysis using Splunk’s pattern view*

![Attack Pattern](Screenshots/attack pattern.png)

**Findings:**
- The requests to `exploit.php` and `read_log.php` were repeatedly triggered, suggesting automation tools or scripts were involved.
- The pattern reveals constant interaction with chat logs (`/chat/read_log.php`), likely as part of a payload delivery or exfiltration mechanism.
- Consistent user-agents (`Node.js` and custom agents) hint at non-browser-based access, further confirming attack automation.

---

### 📌 Most Accessed Client IPs

Next, we analyzed the **top client IPs** to determine who interacted with the server most frequently. This allows us to narrow down potential attacker IPs.

> 🖼 *Screenshot: Top IPs accessing the victim system*
  
![Top IPs](Screenshots/Mostaccessed IPS.png)

**Findings:**
- The IP `10.0.2.5` (our known **attacker machine**) had an extremely high volume of requests. This clearly links the attacker to the reverse shell activity and payload delivery.
- `127.0.0.1` appeared frequently as well — this is normal localhost activity from the victim system.
- Several corrupted or anomalous IP values appeared as hex/garbage characters — these could be malformed logs or intentionally obfuscated traffic, possibly worth deeper review.

---

### ✅ Summary of Insights

From the two analyses above, we confirmed:
- Consistent malicious interaction with vulnerable PHP endpoints.
- Automated tools used from the attacker's IP (`10.0.2.5`) with repeated exploit attempts.
- A recognizable **pattern of payload delivery and interaction**, which aligns with the reverse shell and attack phases from Phase 1.

Together, these visualizations serve as a forensic trace of the attack behavior in Phase 2, providing clear, time-aligned, and IP-based evidence of compromise.

