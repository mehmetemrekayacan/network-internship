# OPNsense Firewall Configuration Rules

This document outlines the firewall rules implemented on the OPNsense router for the virtual corporate network lab. The rules are designed to enforce a multi-tier security architecture with separate network segments for Management, Software, DMZ, and Database.

### Network Interface Definitions

| Interface Name | Virtual Network | IP Subnet         | Purpose                                     |
|----------------|-----------------|-------------------|---------------------------------------------|
| YONETIM (LAN)  | `YONETIM_NET`   | `192.168.20.0/24` | Secure Management Network for administrators. |
| YAZILIM (WAN)  | `YAZILIM_NET`   | `192.168.10.0/24` | Software Dept. / Simulated "Internet".      |
| DMZ (OPT1)     | `DMZ_NET`       | `192.168.30.0/24` | Demilitarized Zone for the public web server. |
| VERITABANI(OPT2)| `VERITABANI_NET`| `192.168.40.0/24` | Secure network for the database server.       |

### Default Policy

The default firewall policy for all interfaces is **Deny/Block All**. Any traffic not explicitly allowed by a rule below is blocked. This enforces a "minimum privilege" security model.

---

### Implemented Firewall Rules

#### 1. YONETIM (Management) Interface Rules

* **Rule 1: Allow All Outbound from Management**
    * **Action:** `PASS`
    * **Protocol:** `any`
    * **Source:** `YONETIM net`
    * **Destination:** `any`
    * **Purpose:** Allows administrators on the management network to access all other networks (Yazilim, DMZ, Veritabani) and the internet for management and testing purposes. This is a highly privileged network.

#### 2. YAZILIM (Simulated Internet) Interface Rules

* **Rule 1: Allow Web Access to DMZ**
    * **Action:** `PASS`
    * **Protocol:** `TCP`
    * **Source:** `YAZILIM net`
    * **Destination:** `DMZ net`
    * **Destination Port:** `HTTP (80)`, `HTTPS (443)`
    * **Purpose:** Allows external users (from the simulated internet) to access the web server located in the DMZ on standard web ports.

#### 3. DMZ Interface Rules

* **Rule 1: Allow DMZ to access Database Server**
    * **Action:** `PASS`
    * **Protocol:** `TCP`
    * **Source:** `DMZ net`
    * **Destination:** `VERITABANI net`
    * **Destination Port:** `3306 (MySQL)`
    * **Purpose:** Allows the web server in the DMZ to connect to the database server in the secure database network. **All other traffic from the DMZ to any other internal network is blocked by the default deny rule.** This is a critical security measure.

#### 4. VERITABANI (Database) Interface Rules

* **Rule 1: Allow Database to Make Outbound Connections**
    * **Action:** `PASS`
    * **Source:** `VERITABANI net`
    * **Destination:** `any`
    * **Purpose:** Allows the database server to initiate connections to the outside for essential tasks like downloading system updates. In a higher-security production environment, this rule would be made more restrictive.