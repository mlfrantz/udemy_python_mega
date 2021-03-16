"""Udemy Python Mega Course Application 1 English Thesaurus"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        try:
            closest = get_close_matches(word, data.keys())[0]
            confirm_word = input(f"Sorry could not find {word}, did you mean {closest}? (y or n): ")
            confirm_word = confirm_word.lower()
            if confirm_word == "y":
                return data[closest]
            else:
                return "Sorry please try again"
        except IndexError:
            return f"The word, {word}, doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for w in output:
        print(w)
else:
    print(output)
