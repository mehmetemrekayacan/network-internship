import os
import subprocess
import platform
import socket

SERVERS = {
    "Web-Server-DMZ": {
        "ip": "192.168.30.100",
        "services": {
            "HTTP (Nginx)": 80,
            "SSH": 22
        }
    },
    "Database-Server": {
        "ip": "192.168.40.100",
        "services": {
            "MySQL/MariaDB": 3306,
            "SSH": 22
        }
    },
    "Firewall-Yonetim": {
        "ip": "192.168.20.1",
        "services": {
            "HTTPS (GUI)": 443,
            "SSH": 22
        }
    }
}

def check_ping(ip):
    param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    command = ['ping', param, '-W 2', ip]
    try:
        response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        return response.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def check_service(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1) 
            s.connect((ip, port))
            return "Running"
    except (socket.timeout, ConnectionRefusedError):
        return "Not Running"

if __name__ == "__main__":
    print("-" * 60)
    print("Starting Full Network and Service Health Check...")
    print("-" * 60)

    for name, details in SERVERS.items():
        ip = details["ip"]
        ping_status = "UP" if check_ping(ip) else "DOWN"
        
        service_info = []
        if ping_status == "UP":
            for service_name, port in details.get("services", {}).items():
                service_status = check_service(ip, port)
                service_info.append(f"{service_name}: {service_status}")

        print(f"Server: {name:<20} | IP: {ip:<15} | Ping Status: {ping_status:<4}")
        if service_info:
            print(f" -> Services: {', '.join(service_info)}")

    print("-" * 60)