# ============================================
# Day 2 - Functions
# Author: Stephen
# Goal: Learn to create and use functions
# ============================================

# ---- BASIC FUNCTION - no input, no output ----
def greet():
    print("Hello Hacker!")

greet()  # call the function

# ---- FUNCTION WITH INPUT ----
def greet_hacker(name, tool):
    return "Hacker " + name + " is using " + tool

# input() value passed to function!
hacker_name = input("Enter your name: ")
hacker_tool = input("Enter your tool: ")
result = greet_hacker(hacker_name, hacker_tool)
print(result)

# ---- FUNCTION WITH RETURN ----
# YOUR DOUBT: return vs print
# print → shows value ONCE, value is LOST forever
# return → SAVES value so you can use it anywhere!

def check_password(password):
    length = len(password)
    if length >= 12:
        return "STRONG password"
    elif length >= 8:
        return "MEDIUM password"
    else:
        return "WEAK password"

# return lets you use result multiple times!
result = check_password("stephen123")
print(result)                        # use it here
print("Password check:", result)     # use it again
print("Saving to log:", result)      # use it anywhere!

# ---- FUNCTION + LOOP combined ----
# Write function ONCE - use it for ALL scores!
def risk_level(score):
    if score >= 9:
        return "CRITICAL"
    elif score >= 7:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    else:
        return "LOW"

scores = [9.5, 7.5, 5.0, 2.0]
for score in scores:
    result = risk_level(score)
    print("Score", score, "→", result)

# ---- FUNCTION WITH TWO PARAMETERS ----
# YOUR DOUBT: how to pass input() to function
# Step 1 → get value from user
# Step 2 → save in variable
# Step 3 → pass variable to function

def scan_target(ip, port):
    if port == 80:
        return "HTTP open"
    elif port == 443:
        return "HTTPS open"
    elif port == 22:
        return "SSH open"
    else:
        return "Unknown port"

ip = input("Enter target IP: ")   # Step 1 & 2
ports = [80, 443, 22, 8080]
for port in ports:
    result = scan_target(ip, port)  # Step 3
    print(ip, ":", port, "→", result)

# ============================================
# KEY LESSONS:
# def        → creates a function (write ONCE)
# name()     → calls a function (use ANYWHERE)
# parameters → inputs you give the function
# return     → saves value so you can reuse it
# print      → shows value but loses it forever
# input()    → save in variable first, then pass to function
# ============================================
