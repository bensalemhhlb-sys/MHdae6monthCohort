# 3-Month Network Security Home Lab Project Plan

This comprehensive plan guides a beginner through building an isolated home network lab, capturing and analyzing traffic, and configuring an open-source firewall. 

## Month 1: Lab Architecture & Environment Setup

### Week 1: Hypervisor Deployment & Virtual Networking
* Install Oracle VM VirtualBox or VMware Workstation Player.
* Configure a host-only or internal virtual network to isolate the lab from your home network.
* Document your network topology, IP addressing scheme, and subnet masks.

### Week 2: Provisioning the Attacker Machine
* Download the official Kali Linux virtual machine image.
* Import the image into your hypervisor and assign it to your isolated network.
* Update system packages and configure basic environment preferences.

### Week 3: Provisioning the Victim Machine
* Download the Metasploitable 2 or Metasploitable 3 virtual machine.
* Import and boot the vulnerable target within the isolated network.
* Verify connectivity between the Kali Linux attacker machine and the Metasploitable victim via a simple ICMP ping test.

### Week 4: Base Environment Verification
* Perform a basic network mapping scan from Kali Linux to ensure the target is visible.
* Take snapshots of all clean virtual machines to establish a recovery baseline.
* Review basic Linux command-line operations and navigation.

---

## Month 2: Traffic Analysis & Attack Simulation

### Week 5: Wireshark Installation & Interface Mastery
* Launch Wireshark on your analyst workstation or Kali Linux machine.
* Familiarize yourself with the capture interfaces, display filters, and coloring rules.
* Practice capturing a baseline of normal, idle network traffic.

### Week 6: Cleartext Protocol Analysis (FTP/HTTP)
* Execute a simulated FTP or HTTP login from the attacker machine to the target machine.
* Capture the traffic stream using Wireshark.
* Use the "Follow TCP Stream" feature to isolate and extract cleartext usernames and passwords.

### Week 7: Port Scanning & Reconnaissance Footprints
* Run a basic Nmap stealth scan (SYN scan) from Kali Linux against the target.
* Analyze the resulting PCAP file to see how port scans appear to network defenders.
* Identify the specific TCP flags (SYN, ACK, RST) used during host discovery.

### Week 8: Exploit Captures & Log Review
* Execute a basic, well-documented exploit using the Metasploit Framework (e.g., VSFTPD backdoor).
* Capture the full exploit payload delivery in Wireshark.
* Analyze the network artifacts left behind by the successful intrusion.

---

## Month 3: Perimeter Defense & Network Segmentation

### Week 9: pfSense Deployment & Interface Mapping
* Download the pfSense or OPNsense ISO image.
* Create a new virtual machine acting as the central security gateway.
* Map the WAN interface to your internet-connected bridge and the LAN interface to your isolated lab network.

### Week 10: Firewall Policy Configuration
* Access the web management portal of the firewall.
* Configure strict "Default Deny" inbound rules for the internal network segment.
* Create targeted rules allowing only specific protocols (e.g., SSH, HTTPS) between designated hosts.

### Week 11: Network Segmentation & DMZ Isolation
* Create a third network interface (DMZ) within the firewall configuration.
* Move the Metasploitable target into the DMZ network segment.
* Write rules preventing the compromised DMZ target from initiating any traffic back into your secure management LAN.

### Week 12: Final Review & Lab Documentation
* Attempt to rerun your previous port scans and exploits to verify that the new firewall rules successfully block them.
* Export your final firewall configurations and save your Wireshark analysis notes.
* Compile a summary report detailing the lab architecture, discovered vulnerabilities, and implemented defenses.
