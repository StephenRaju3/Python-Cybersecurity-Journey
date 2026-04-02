# ============================================
# Day 1 - Password Strength Checker
# Author: Stephen
# Goal: Check if a password is strong enough
# ============================================

# Ask the user to enter their password
password = input("enter the password:")

# Count how many characters the password has
# len() counts the characters, int() makes sure it's a whole number
length = int(len(password))

# Check password strength based on length
if length >= 12:
    # 12 or more characters = strong (hard to crack!)
    print("strong password")

elif length >= 8:
    # 8 to 11 characters = medium (okay but could be better)
    print("medium password")

else:
    # less than 8 characters = weak (easy for hackers to crack!)
    print("week password so change the password")
