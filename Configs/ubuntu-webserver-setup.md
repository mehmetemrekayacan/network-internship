!######################################################
! Configuration Steps for Ubuntu Web Server in DMZ
!
! Purpose: To host a dynamic website, accessible from the "Internet" network.
!######################################################

# --- Initial Setup ---
# Base OS: Ubuntu Server 22.04 LTS
# Role: Dynamic Web Server
# Network: DMZ_NET (IP assigned by OPNsense DHCP)

# --- Required Software Installation ---
# 1. Update package lists
sudo apt update

# 2. Install Nginx Web Server
sudo apt install nginx -y

# 3. Install PHP-FPM for dynamic content processing
sudo apt install php-fpm -y


# --- Nginx Configuration for PHP ---
# The default Nginx site configuration was edited to process PHP files.
# File edited: /etc/nginx/sites-available/default
#
# Changes made:
# - Added 'index.php' to the index directive.
# - Uncommented the location block for '\.php$' to pass PHP scripts
#   to the PHP-FPM socket.

# --- Firewall Configuration (on the server itself) ---
# Although the main firewall is OPNsense, it's good practice
# to also configure the local firewall (UFW).
sudo ufw allow 'Nginx Full'
sudo ufw enable