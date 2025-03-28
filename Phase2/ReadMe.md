# 📊 Phase 2: SIEM Dashboard Analysis

## 🔧 SIEM Setup

In this phase, we integrated logs from both the **victim** and **attacker** environments into **Splunk**, our chosen SIEM tool. This step enables central analysis, threat detection, and deeper insight into attacker behavior.

> 📸 *Screenshot A: Uploading system-journal.log into Splunk (Attacker logs)*  
![Screenshot A](Screenshots/A.png)


### ✅ Logs Integrated:
- **Victim (Metasploitable3)**: Apache access logs (`access.log`)
- **Attacker (Kali Linux)**: System journal logs (`system-journal.log`)


-
> 📸 *Screenshot C: Uploading `system-journal.log` into Splunk (Attacker logs)*
![Screenshot C](./Screenshots/C.png)

---

## 📊 Log Visualization & Analysis

Once both log files were uploaded, we used Splunk's **Search & Reporting** app to:


> 📸 *Screenshot B: Splunk main dashboard after logging in successfully*
![Screenshot B](./Screenshots/B.png)

> 📸 *Screenshot D: Querying `system-journal.log` inside Splunk*
![Screenshot D](./Screenshots/D.png)
