import socket
import time
from datetime import datetime

def simple_port_scanner():
    # Clear the screen
    print("\n" * 50)
    
    # Enhanced ASCII Art Banner with Port Scanner and Developer Name
    print(r"""
  ____            _      ____                                  
 |  _ \ ___  _ __| |_   / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_) / _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 |  __/ (_) | |  | |_    ___) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__|  |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                               
    """)
    print("\n" + "="*52)
    print("|" + "PORT SCANNER TOOL".center(50) + "|")
    print("|" + "Developed by: MD Farhan Uddin Jibon".center(50) + "|")
    print("="*52 + "\n")
    
    # Get target input
    target = input("Enter target IP or hostname (localhost by default): ") or "localhost"
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved. Exiting.")
        return
    
    print(f"\n[+] Scanning target: {target} ({target_ip})")
    print("[+] Scan started at: " + str(datetime.now()))
    print("[~] Scanning common ports...\n")
    
    # Common ports to scan
    common_ports = {
        20: "FTP (Data)",
        21: "FTP (Control)",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        465: "SMTPS",
        587: "SMTP (Submission)",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP Alt"
    }
    
    # Start scanning
    start_time = time.time()
    
    try:
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} ({service}) is \033[92mopen\033[0m")
            else:
                print(f"[-] Port {port} ({service}) is closed", end="\r")
            
            sock.close()
    
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting.")
        return
    except socket.error:
        print("[!] Could not connect to server. Exiting.")
        return
    
    # Calculate and display scan duration
    end_time = time.time()
    duration = end_time - start_time
    print(f"\n[+] Scan completed in {duration:.2f} seconds")

if __name__ == "__main__":
    simple_port_scanner()