# KONYA FOOD AND AGRICULTURE UNIVERSITY

## FACULTY OF ENGINEERING AND ARCHITECTURE  
### COMPUTER ENGINEERING DEPARTMENT  

**COMP 3800**  
**SUMMER INTERNSHIP REPORT**  

**Mehmet Emre KAYACAN**  
**212010020011**  

**Performed at**  
**Süleyman Demirel Üniversitesi  
Bilgi İşlem Daire Başkanlığı**  

**04.08.2025 - 29.08.2025**

---

# Table of Contents

1. [Abstract](#1-abstract)  
2. [Introduction](#2-introduction)  
3. [Company Information](#3-company-information)  
4. [Work Done](#4-work-done)  
   - [4.1. Network Infrastructure Projects](#41-network-infrastructure-projects)  
   - [4.2. Virtual Machine and Firewall Configuration](#42-virtual-machine-and-firewall-configuration)  
   - [4.3. Field Service and Technical Support](#43-field-service-and-technical-support)  
   - [4.4. Advanced Python Scripting for Network Automation](#44-advanced-python-scripting-for-network-automation)  
5. [Conclusion](#5-conclusion)  
6. [References](#6-references)  
7. [Questionnaire](#7-questionnaire)  
   - [Work Focus](#work-focus)  
   - [Courses that are useful to your internship](#courses-that-are-useful-to-your-internship)  
   - [Target Industry](#target-industry)  
   - [Team Profile](#team-profile)  
   - [The Joel Test: 12 Steps to Better Code](#the-joel-test-12-steps-to-better-code)  
8. [Appendices](#8-appendices)  
   - [Appendix A – Python Network Automation Script (Snippet)](#appendix-a--python-network-automation-script-snippet)  
   - [Appendix B – Example VLAN Configuration (HP2626 Switch CLI)](#appendix-b--example-vlan-configuration-hp2626-switch-cli)  
   - [Appendix C – Firewall Rule Example (OpnSense)](#appendix-c--firewall-rule-example-opnsense)

---

# 1. Abstract

During my summer internship at Süleyman Demirel University Information Technology Department, I worked in the Network and System Administration unit from August 4 to August 29, 2025. My main activities included network infrastructure setup, VLAN configuration using HP2626 switches, virtual machine installation with firewall implementations using OpnSense, and providing technical support across the university campus.  
I gained practical experience in network troubleshooting, cable management, and system administration. This internship enhanced my understanding of enterprise-level network operations and strengthened my interest in pursuing a career in network engineering and cybersecurity.

---

# 2. Introduction

I completed my summer internship at Süleyman Demirel University Information Technology Department, specifically within the Network and System Administration unit. Süleyman Demirel University is a major state university that requires robust IT infrastructure to support thousands of students, faculty, and staff members.  

I chose this institution for my internship because I wanted to gain experience in a government organization and observe corporate-level IT operations in an educational environment.  

During my three-week internship, I primarily focused on network infrastructure management, virtual machine configuration, firewall security implementations, and field service support. The work involved hands-on experience with enterprise networking equipment, security protocols, and troubleshooting real-world network issues across the university campus.  

This report is organized into four main sections:  
- **Introduction**  
- **Company Information**  
- **Work Done** (technical work performed)  
- **Conclusion**

---

# 3. Company Information

**Organization:** Süleyman Demirel University Information Technology Department  
**Address:** Süleyman Demirel University, Isparta, Turkey  
**Department:** Network and System Administration Unit  

### Supervisor Information
- **Name:** Kadir Sümer  
- **Position:** Computer Engineering Faculty Member & Staff, Network and System Administration Unit  
- **Education:**  
  - B.Sc. Computer Engineering, SDÜ (2019)  
  - M.Sc. Computer Engineering (Thesis), SDÜ (2019)  

### Team Composition
- 1 Faculty Member & Staff (Kadir Sümer)  
- 6 Full-time Computer Engineering Personnel  
- 1 Part-time Technical Staff  
- 2 Summer Interns (including myself)  

**Team Members:**  
- Sinan Ece (Part-time Technical Staff)  
- Furkan Özdemir (Summer Intern)  

### Department Focus and Resources
The department manages the entire IT infrastructure of Süleyman Demirel University, including network connectivity, server management, security systems, and technical support services. Hardware resources include enterprise-level switches (HP2626 series), routers, firewalls, servers, and virtualization platforms.  

### Software & Environment
- Linux distributions (Ubuntu, Rocky Linux)  
- Windows systems  
- Virtualization (VirtualBox, etc.)  
- Network monitoring and security tools  

---

# 4. Work Done

## 4.1. Network Infrastructure Projects

**HP2626 Switch Configuration and VLAN Implementation**  
- Configured VLANs via CLI  
- Management VLAN, Software VLAN, and General Access VLAN  
- Implemented trunk and access ports with 802.1Q tagging  

**Cable Infrastructure Management**  
- CAT7 cable installation and RJ45 terminations  
- Provided connectivity across campus offices  

**Diagnostics & Troubleshooting**  
- Used RJ45 testers for physical checks  
- Switch-level port/VLAN checks  
- Log analysis for performance monitoring  

---

## 4.2. Virtual Machine and Firewall Configuration

**Virtualization Setup**  
- 7 Virtual Machines in VirtualBox  
- Ubuntu (4), Rocky Linux (2), OpnSense Firewall (1)  

**Firewall (OpnSense)**  
- Configured DMZ  
- Database port access rules (e.g. MySQL 3306 only from Web Server)  
- NAT for outbound internet  

**Linux System Administration**  
- Worked with `systemd`, DNF, IPTables  
- Learned enterprise-grade Rocky Linux operations  

---

## 4.3. Field Service and Technical Support

- Supported IT needs in Engineering Faculty, Arts & Sciences, Admin offices  
- Designed topology for new office network  
- Cable + VLAN planning, implementation, and troubleshooting  
- Used step-by-step physical-to-logical troubleshooting methodology  

---

## 4.4. Advanced Python Scripting for Network Automation

**Developed Script (~200 lines):**  
- Libraries: `socket`, `subprocess`, `psutil`  
- Functions:  
  - Ping test (automated)  
  - Bandwidth monitoring  
  - Interface status checking  

**Outcome:**  
Combined programming skills with network admin tasks, providing automation and faster diagnostics.  

---

# 5. Conclusion

**Key Learning Outcomes:**  
- VLAN segmentation & HP2626 switch management  
- Linux administration & virtualization  
- Firewall configuration with OpnSense & IPTables  
- Real-world troubleshooting & support experience  
- Programming + Network integration (Python automation)  

**Career Impact:**  
This internship directed my focus toward **Network Engineering & Cybersecurity**, shifting away from pure software development. I now have both the theoretical foundation and practical experience to pursue this career path.  

---

# 6. References

1. Süleyman Demirel Univ., *IT Dept. Internal Docs & Training Materials*  
2. Kurose, J. F., & Ross, K. W., *Computer Networking: A Top-Down Approach*, 8th Ed., Pearson, 2020  
3. HP, *ProCurve 2626 Switch Configuration Guide*  
4. OpnSense, *Firewall Configuration & Management Docs*  
5. Konya Food & Agriculture Univ., *Computer Networks Course Materials*  

---

# 7. Questionnaire

### Operating Systems Used
☑ Windows ☑ Linux ☐ Mac OS ☐ Other  

### Programming Languages Used
☑ Python  

### Work Focus
☑ Security and Network  

### Courses Useful to Internship
☑ Introduction to Programming (Python)  
☑ Computer Networks  

### Target Industry
☑ Government ☑ Education  

---

## Team Profile
- Engineers: 6  
- Scientists: 0  
- Other workers: 1  
- High school graduates: 1  
- University graduates: 6  
- MS graduates: 2  
- PhD graduates: 1  

---

## The Joel Test: 12 Steps to Better Code
- Source control: Yes  
- One-step build: Yes  
- Daily builds: Partially  
- Bug database: Yes  
- Fix-before-new-code: Yes  
- Up-to-date schedule: Yes  
- Spec availability: Yes  
- Quiet workspace: Yes  
- Best tools: Partially  
- Testers: Yes  
- Code in interview: Not applicable  
- Hallway usability testing: Yes  

---

# 8. Appendices

## Appendix A – Python Network Automation Script (Snippet)

```python
import socket, subprocess, psutil

# Ping Test Function
def ping(host):
    result = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE)
    return result.stdout.decode()

# Network Interface Status
def get_interfaces():
    interfaces = psutil.net_if_addrs()
    for iface, addrs in interfaces.items():
        print(f"Interface: {iface}")
        for addr in addrs:
            print(f"  {addr.address}")

# Example usage
print(ping("8.8.8.8"))
get_interfaces()
