
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



