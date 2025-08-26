!######################################################
! VirtualBox VM Configuration for OPNsense Router
!
! Purpose: To serve as the central router/firewall for the virtual lab.
!######################################################

# --- Virtual Machine Specifications ---
VM Name: OPNsense-Router
Operating System Type: BSD / FreeBSD (64-bit)
Base Memory: 4096 MB (4 GB)
Processors: 2 CPU
Boot Order: Hard Disk
Chipset: PIIX3
Pointing Device: PS/2 Mouse
Enable I/O APIC: Enabled
Enable EFI: Disabled (for compatibility with the installation image)
Enable Hardware Clock in UTC Time: Enabled

# --- Storage Configuration ---
SATA Controller:
  - OPNsense-Router.vdi (16 GB, Dynamically Allocated)
IDE Controller:
  - Empty (Installer ISO removed after installation)

# --- Network Adapter Configuration ---
# Four separate internal networks were created to simulate VLANs.
Adapter 1 (em0):
  - Attached to: Internal Network
  - Name: YAZILIM_NET
Adapter 2 (em1):
  - Attached to: Internal Network
  - Name: YONETIM_NET
Adapter 3 (em2):
  - Attached to: Internal Network
  - Name: DMZ_NET
Adapter 4 (em3):
  - Attached to: Internal Network
  - Name: VERITABANI_NET