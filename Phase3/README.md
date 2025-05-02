# ✅ Phase 3: Defensive Strategy – Securing ProFTPD

## 🔐 Chosen Defense: Disable mod_copy Module in ProFTPD

### Step 1: Defense Mechanism – Disabling mod_copy
```
<IfModule mod_copy.c> CopyEngine off </IfModule>
```
![Disabling mod_copy](Phase3/screenshots/A.png)
This line explicitly disables the CopyEngine of the mod_copy module in ProFTPD.

This action mitigates the vulnerability CVE-2015-3306, which allows arbitrary file copying via SITE CPFR and SITE CPTO.

### 🔁 Step 2: Re-run the attack
For the sake of comparison, we will run the attack twice — once before setting the defense and once after.

**Attack Before Defense:**
![attack before 1](Phase3/screenshots/B.png)
The whoami command returns www-data, confirming gained access as a web service user.
![attack before 2](Phase3/screenshots/C.png)

**Attack After Defense:**
![attack after](Phase3/screenshots/D.png)
As illustrated above, the attack failed due to a write failure during the proftpd_modcopy_exec attack
---

## 🔐 Before-and-After Security Status

| Scenario              | Attack Outcome        | Explanation                                |
|-----------------------|-----------------------|--------------------------------------------|
| **Before Defense**    | Reverse shell opened  | Exploit successful via mod_copy            |
| **After Defense**     | Exploit failed        | mod_copy module disabled in ProFTPD config |


