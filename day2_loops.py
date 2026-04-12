# ============================================
# Day 2 - Loops
# Author: Stephen
# Goal: Learn for loops, while loops, range()
# ============================================

# ---- FOR LOOP - loop through a list ----
ports = [80, 443, 143, 3348]
for port in ports:
    print("port scanner:", port)

# ---- RANGE() - loop through a range of numbers ----
# range(start, stop) - stop is NOT included!
# Your mistake: you used range(70,80) → prints 70 to 79
# To include 80 → use range(70, 81)
for port in range(70, 80):
    print("scanning port:", port)

# ---- WHILE LOOP - repeat until condition is false ----
# Real world use: brute force protection!
attempts = 5
while attempts > 0:
    print("login attempts remaining:", attempts)
    attempts -= 1   # attempts = attempts - 1
print("account locked")

# ---- FOR LOOP + CONDITIONS combined ----
# This is the logic inside real tools like nmap!
for i in range(20, 25):
    if i == 20:
        print("FTP data port")
    elif i == 21:
        print("FTP control port")
    elif i == 22:
        print("SSH port - remote access!")
    elif i == 23:
        print("Telnet - very insecure!")
    else:
        print("Unknown port")

# ---- NESTED LOOPS - loop inside a loop ----
# Scans multiple targets across multiple ports
targets = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]
ports = [80, 443, 22]

for ip in targets:
    print("--- Scanning", ip, "---")
    for port in ports:
        print(ip, ":", port)

# ============================================
# KEY LESSONS:
# for loop   → use when you know how many times
# while loop → use when you don't know how many times
# range()    → generates numbers automatically
# nested loop → loop inside loop = scan multiple targets
# ============================================
