# OPNsense Router - Virtual Machine Configuration

This document outlines the VirtualBox settings for the central OPNsense router VM used in this lab project.

### Virtual Machine Specifications

- **VM Name:** `OPNsense-Router`
- **Operating System Type:** `BSD / FreeBSD (64-bit)`
- **Base Memory:** `4096 MB (4 GB)`
- **Processors:** `2 CPU`
- **Boot Order:** Hard Disk first
- **Enable EFI:** `Disabled` (For compatibility with the installation image)

### Storage Configuration

- **SATA Controller:**
  - `OPNsense-Router.vdi` (16 GB, Dynamically Allocated)
- **IDE Controller:**
  - `Empty` (Installer ISO removed after installation)

### Network Adapter Configuration

Four separate internal networks were created to simulate a segmented corporate network with VLANs.

| Adapter | Status    | Attached to      | Network Name         | Purpose                |
|---------|-----------|------------------|----------------------|------------------------|
| **1** | `Enabled` | `Internal Network` | `YAZILIM_NET`        | Software Dept. / "WAN" |
| **2** | `Enabled` | `Internal Network` | `YONETIM_NET`        | Management Dept. (LAN) |
| **3** | `Enabled` | `Internal Network` | `DMZ_NET`            | DMZ for Web Server     |
| **4** | `Enabled` | `Internal Network` | `VERITABANI_NET`     | Secure Database Network|