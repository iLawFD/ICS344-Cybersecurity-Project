# ✅ Phase 3: Defensive Strategy – Securing ProFTPD
## 🔐 Chosen Defense: Disable mod_copy Module in ProFTPD + Firewall Rule

### Step 1: Defense Mechanism – Disabling mod_copy
Edit ProFTPD’s configuration file:
```
sudo nano /etc/proftpd/proftpd.conf
```
Comment out or remove the following line:
```
LoadModule mod_copy.c
```
Restart the service:
```
sudo service proftpd restart
```

### Step 2: Add a Local Firewall Rule
As an added layer of protection, block FTP from external access 
```
sudo ufw deny from 10.0.2.5 to any port 21
```
Verify:
```
sudo ufw status
```

### 🔁 Step 3: Re-run the Attack
Now that we've set up our defense, let's re-run the attack.

