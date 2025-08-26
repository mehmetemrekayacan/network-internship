# Ubuntu Web Server - Configuration Steps

This document details the steps taken to configure a standard Ubuntu Server 22.04 LTS VM for its role as a dynamic web server within the DMZ.

### Initial Setup

- **Base OS:** `Ubuntu Server 22.04 LTS`
- **VM Role:** Dynamic Web Server
- **Network:** `DMZ_NET` (IP address is assigned by the OPNsense DHCP server)

### Required Software Installation

The following commands were used to install the necessary services from the official Ubuntu repositories.

```bash
# 1. First, update all package lists to ensure we get the latest versions.
sudo apt update

# 2. Install the Nginx Web Server. The '-y' flag automatically confirms the installation.
sudo apt install nginx -y

# 3. Install PHP-FPM, the FastCGI Process Manager, which is required for Nginx to process PHP code.
sudo apt install php-fpm -y
```

### Nginx Configuration for PHP

To enable dynamic content, the default Nginx site configuration file was modified.

- **File Edited:** `/etc/nginx/sites-available/default`
- **Changes Made:**
  - Added `index.php` to the `index` directive to prioritize it as a default page.
  - Uncommented the `location ~ \.php$` block to enable the processing of PHP files.
  - Ensured the `fastcgi_pass` directive pointed to the correct PHP-FPM socket file for the installed version.

### Local Firewall Configuration (UFW)

Although the primary network security is handled by the OPNsense firewall, it is a security best practice to also configure the local firewall on the server.

```bash
# Allow standard web traffic (ports 80 for HTTP and 443 for HTTPS)
sudo ufw allow 'Nginx Full'

# Enable the Uncomplicated Firewall (UFW)
sudo ufw enable
```