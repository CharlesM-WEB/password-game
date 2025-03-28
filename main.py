import time 
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
day= weekdays[time.localtime().tm_wday]

while True: 
    print("Please choose a password:")
    password = input()

    for letter in password:
        if letter not in letters and letter not in numbers:
            break
    else:
        print(" Rule 1. password must include a special symbol")
        continue 
    for letter in password:
        if letter in numbers:
            break
    else:
        print("Rule 2. password must include a number")
        continue
    
    count = 0
    
    for letter in password:
        if letter in numbers:
            count += int(letter)
    if count != 10:
        print("Rule 3. digits in the password must add up to 10")
        continue
    
    if day.lower() not in password.lower():
        print("rule 4. password must include the current day of the week")
        continue
    
    