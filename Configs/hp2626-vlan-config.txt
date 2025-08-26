
# HP ProCurve 2626 Switch Configuration File

**Intern:** Mehmet Emre KAYACAN  
**Date:** August 2025  
**Performed at:** Suleyman Demirel University, IT Department  

---

This configuration was created for a **lab environment** to practice  
network segmentation using **VLANs**.

---

## Basic Setup
```plaintext
hostname "SDU-IT-LAB-SW01"

---

## VLAN Creation

Four separate VLANs were created to logically isolate different
network segments, mimicking a corporate network structure:

* **VLAN 10** → Software Department (for developers)
* **VLAN 20** → Management Department (for administrators)
* **VLAN 30** → DMZ (for public-facing servers like the web server)
* **VLAN 40** → Database Department (for secure backend servers)

```plaintext
vlan 10
   name "YAZILIM_DEPARTMANI"
   exit
vlan 20
   name "YONETIM_DEPARTMANI"
   exit
vlan 30
   name "DMZ_SUNUCULARI"
   exit
vlan 40
   name "VERITABANI_SUNUCULARI"
   exit
```

---

## Port Assignments (Access Ports)

Untagged ports are assigned to a single VLAN. Devices connected
to these ports (like PCs and servers) do not need to be VLAN-aware.

```plaintext
vlan 10
   untagged 1-8
   exit
vlan 20
   untagged 9-16
   exit
vlan 30
   untagged 17-20
   exit
vlan 40
   untagged 21-22
   exit
```

---

## Trunk Port Configuration

A tagged port (trunk) can carry traffic for multiple VLANs simultaneously.
Port **24** is configured as the trunk port to connect to the **OPNsense router**.

```plaintext
vlan 10
   tagged 24
   exit
vlan 20
   tagged 24
   exit
vlan 30
   tagged 24
   exit
vlan 40
   tagged 24
   exit
```

---

## Management and Security

Enabling **SSH** for secure remote management.
Telnet was disabled due to its lack of encryption.

```plaintext
ip ssh
```

---

## Notes

* Don’t forget to **save the configuration** with:

  ```plaintext
  write memory
  ```
* This setup simulates a real corporate network structure,
  focusing on **departmental isolation** and **secure access**.

---

