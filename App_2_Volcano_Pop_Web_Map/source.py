import mysql.connector
from difflib import get_close_matches

def translate(word):
    word = word.lower()
    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        return results
    else:
        query = cursor.execute("SELECT Expression FROM Dictionary")
        words = cursor.fetchall()
        words = [w[0] for w in words]
        closest = get_close_matches(word, words)[0]
        confirm_word = input(f"Sorry could not find {word}, did you mean {closest}? (y or n): ")
        confirm_word = confirm_word.lower()
        if confirm_word == "y":
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % closest)
            results = cursor.fetchall()
            return results
        else:
            return "Sorry word not found"

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter the word: ")

output = translate(word)

if type(output) == list:
    for w in output:
        print(w[0])
else:
    print(output)
