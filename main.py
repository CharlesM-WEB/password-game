import requests
import json
import time 
import random 



pokeman = requests.get("https://pokeapi.co/api/v2/type/11").json()["pokemon"]
pokemonnames = []
for p in pokeman:
    pokemonnames.append(p["pokemon"]["name"])
numbers = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
day= weekdays[time.localtime().tm_wday]

full_list = requests.get("https://opentdb.com/api.php?amount=50&category=12&difficulty=easy&type=multiple").json()["results"]
q = 0
trivia  = full_list[q]

while True:
    trivia["question"] = trivia["question"].replace("&quot;","'")
    
    for letter in trivia["correct_answer"].lower():
        if letter not in numbers and letter not in letters:
            break
    else:
        break 
    q += 1
    trivia = full_list[q]
answers = [trivia["correct_answer"]] + trivia["incorrect_answers"]
random.shuffle(answers)
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
    
    for pokemon in pokemonnames:
        if pokemon in password.lower():
            break
    else:
        print("rule 5. password must include a water type pokemon")
        continue
    
    if trivia["correct_answer"].lower().strip() not in password.lower():
        print("rule 6. password must contan the answer to the trivia question " + trivia["question"])
        print(f"{answers[0]},{answers[1]},{answers[2]},{answers[3]}")
        continue 
    
    