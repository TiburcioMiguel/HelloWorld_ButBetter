#!/usr/bin/env python3
import time

def hello_world():
    alphabet = ["a","b","c","d","e","f","g","H",
                "i","j","k","l","m","n","o","p",
                "q","r","s","t","u","v","W","x",
                "y","z"," ","!"]
    message = "Hello World!"
    correct_letters = ""

   ## Checking every letter in the message "Hello World!"
    for letter in message:
        ## Checking against every letter in alphabet
        for char in alphabet:
            if char == letter:
                correct_letters += letter
                ## adding delay so that it is more satisfying to watch
                time.sleep(.0625)
                print(correct_letters)
                break
            else:
                time.sleep(.0625)
                print(correct_letters + char)
            
            
            



hello_world()
    
    