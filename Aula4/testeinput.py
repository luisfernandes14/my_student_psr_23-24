#!/usr/bin/env python3

import readchar

num_letters = 5  # Change this to the desired number of letters

user_input = ""

print(f"Enter exactly {num_letters} letters:",end="",flush=True)

while len(user_input) < num_letters:
    char = readchar.readchar()
    user_input += char
    print(char, end='',flush=True)
print()    
if user_input == "cinco":
    
    print("bem jogado")
else:
    print("burro")


 # Print a newline to move to the next line
print(f"You entered: {user_input}")
