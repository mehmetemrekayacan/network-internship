# Applied Network Administration and Security Lab

This repository documents the projects and tasks completed during my summer internship at the **Süleyman Demirel University IT Department** (Network and System Administration unit) in August 2025.

The main objective of this internship was to apply theoretical networking concepts to real-world scenarios using both physical and virtual hardware. This repository serves as a portfolio of the skills I gained in system administration, network segmentation, and security configuration.

---

## 🚀 Technologies and Tools Used

| Category | Tools |
| :--- | :--- |
| **Virtualization** | Oracle VirtualBox |
| **Operating Systems** | Ubuntu Server, Rocky Linux, OPNsense (FreeBSD) |
| **Networking Hardware** | HP ProCurve 2626 (Managed L2 Switch) |
| **Firewall & Routing** | OPNsense, iptables (Netfilter), PF |
| **Analysis & Simulation** | Wireshark, Cisco Packet Tracer, PuTTY |
| **Automation & Scripting**| Python (socket, subprocess, paramiko), Bash |

---

## 📂 Project Structure

This repository is organized into the following directories:

* [cite_start]**/report:** Contains the final internship report in both PDF and Markdown formats. [cite: 1]
* [cite_start]**/configs:** Includes detailed configuration files for the hardware and software used in the lab. [cite: 1]
* **/scripts:** Contains a Python script for network and service monitoring automation.
* [cite_start]**/screenshots:** Includes various screenshots from the lab environment for visual reference. [cite: 2]

---

## 🔧 Key Projects and Skills Learned

### 1. Multi-Layered Virtual Network Laboratory
I designed and implemented a complete virtual corporate network using VirtualBox and OPNsense.
- **Learned Skills:**
  - Deployed and configured a professional-grade firewall/router (OPNsense).
  - Created multiple, isolated network segments (`YONETIM`, `YAZILIM`, `DMZ`, `VERITABANI`) to simulate a secure corporate architecture.
  - Implemented inter-network routing and DHCP services for each segment.
  - **See configuration details:** [`configs/opnsense-firewall-rules.md`](Configs/opnsense-firewall-rules.md)

### 2. Physical Switch Configuration (HP ProCurve 2626)
Gained hands-on experience with enterprise-grade network hardware.
- **Learned Skills:**
  - Connected to a managed switch via console port using PuTTY.
  - Implemented network segmentation using **VLANs**.
  - Configured **Trunk Ports** to carry multi-VLAN traffic.
  - **See configuration details:** [`configs/hp2626-vlan-config.md`](Configs/hp2626-vlan-config.md)

### 3. Network Automation Scripting
Developed a Python script to automate network monitoring tasks.
- **Learned Skills:**
  - Used Python libraries like `socket` to check the status of critical network services (HTTP, MySQL, SSH).
  - Automated `ping` tests to verify host reachability.
  - **See the script:** [`scripts/network_monitor.py`](Scripts/network_monitor.py)

---

## 📜 Full Internship Report

For a detailed, day-by-day account of all tasks, challenges, and learning outcomes, please see the full internship report.

➡️ **[View the Full Report (PDF)](Report/CENG_summerInternshipReport.pdf)**

---

### Career Impact

This internship was a definitive experience that solidified my interest in **Network Engineering and Cybersecurity**. The hands-on challenges and problem-solving involved in configuring and securing a network were far more engaging than my previous academic focus on pure software development.
