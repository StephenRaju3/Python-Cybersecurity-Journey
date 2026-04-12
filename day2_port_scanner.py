# ============================================
# Day 2 - Port Scanner Project
# Author: Stephen
# Goal: Scan multiple ports on a target IP
# This is the same logic as nmap - real tool!
# ============================================

# ---- THE SCANNER FUNCTION ----
def scan_target(ip, port):
    # Dictionary stores port information
    # Easy to add new ports - just add one line!
    port_info = {
        80  : "HTTP - unencrypted",
        443 : "HTTPS - encrypted",
        22  : "SSH - remote access",
        23  : "Telnet - insecure!",
        3306: "MySQL database",
        8080: "HTTP alternate"
    }

    # YOUR MISTAKE: you wrote "if port in ports"
    # ports is the LIST outside the function
    # port_info is the DICTIONARY inside the function
    # Always check the DICTIONARY not the LIST!
    if port in port_info:        # ✅ check dictionary
        return port_info[port]   # return the service name
    else:
        return "Unknown port"    # safe fallback

# ---- GET TARGET FROM USER ----
# YOUR DOUBT: input() value passed as parameter
# Save input first → then pass to function
ip = input("Enter target IP: ")

# ---- LIST OF PORTS TO SCAN ----
ports = [80, 443, 22, 23, 3306, 8080]

# ---- SCAN ALL PORTS ----
print("\n--- Starting Port Scan ---")
for port in ports:
    result = scan_target(ip, port)   # ip from input()!
    print(ip, ":", port, "→", result)
print("--- Scan Complete ---")

# ============================================
# HOW IT ALL CONNECTS:
# input()      → gets target IP from user
# dictionary   → stores port information cleanly
# function     → takes ip + port, returns service
# list         → stores all ports to scan
# for loop     → goes through every port
# function()   → called for each port automatically
#
# YOUR MISTAKES TO REMEMBER:
# ❌ port_info()  → wrong! dictionary not a function
# ✅ port_info    → correct! no brackets needed
#
# ❌ if port in ports     → checks list (wrong!)
# ✅ if port in port_info → checks dictionary (right!)
#
# YOUR DOUBTS ANSWERED:
# Q: Can input() value be passed to function?
# A: YES! save in variable first, then pass it!
#    ip = input()        → save
#    scan_target(ip, port) → pass
# ============================================
