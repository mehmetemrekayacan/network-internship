# HP ProCurve 2626 Switch Configuration File

**Intern:** Mehmet Emre KAYACAN  
**Date:** August 2025  
**Performed at:** Suleyman Demirel University, IT Department  

---

This configuration was created for a **lab environment** to practice network segmentation using **VLANs**.

---

## Configuration

```plaintext
! --- Basic Setup ---
hostname "SDU-IT-LAB-SW01"

! --- VLAN Creation ---
! VLAN 10: Software Department
! VLAN 20: Management Department
! VLAN 30: DMZ (public-facing servers)
! VLAN 40: Database Department

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

! --- Port Assignments (Access Ports) ---
! Untagged ports assigned to a single VLAN
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

! --- Trunk Port Configuration ---
! Port 24 as trunk for all VLANs
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

! --- Management and Security ---
! Enable SSH, disable Telnet
ip ssh

! End of configuration
! Save with 'write memory'
