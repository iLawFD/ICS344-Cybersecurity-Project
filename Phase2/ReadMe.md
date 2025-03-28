# 📊 Phase 2: SIEM Dashboard Analysis

## 🔧 SIEM Setup

In this phase, we integrated logs from both the **victim** and **attacker** environments into **Splunk**, our chosen SIEM tool. This step enables central analysis, threat detection, and deeper insight into attacker behavior.

### ✅ Logs Integrated:
- **Victim (Metasploitable3)**: Apache access logs (`access.log`)
- **Attacker (Kali Linux)**: System journal logs (`system-journal.log`)

> 📸 *Screenshot A: Uploading system-journal.log into Splunk (Attacker logs)*  
![Screenshot A](/Screenshots/A.png)

---

## 📈 Log Visualization & Analysis

Once both log files were uploaded, we used Splunk's **Search & Reporting** app to analyze patterns. This visualization helped us:
- Confirm the execution of the reverse shell attack
- Identify client IPs involved in the attack
- Analyze HTTP requests, user-agents, and payloads

> 📸 *Screenshot B: Splunk main dashboard after successful data ingestion*  
![Screenshot B](../Screenshots/B.png)

---

## 🔍 Attack Comparison

We compared logs from:
- The **attacker (10.0.2.5)** — initiating the reverse shell
- The **victim (127.0.0.1)** — showing incoming HTTP requests and unusual activity

This correlation allowed us to validate the success of the attack and its exact timeline.

> 📸 *Screenshot C: Splunk search showing HTTP GET requests from attacker*  
![Screenshot C](../screenshots/C.png)

---

## ✅ Deliverables Checklist

- [x] **Screenshot of SIEM Integration** (victim + attacker logs)  
- [x] **Screenshot of attack visualization** using Splunk dashboard  
- [x] **Screenshot of log analysis** showing behavior and correlation  
