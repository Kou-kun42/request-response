from flask import Flask
import random


app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It\'s me, Ducky!"


@app.route("/penguins")
def pengiunpage():
    return "Penguins are cute!"


@app.route("/panda")
def pandapage():
    return "Pandas are cool!"


@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    """
    Display a message to the user that changes based
     on their favorite animal.
    """
    return f"Wow, {users_animal} is my favorite animal, too!"


@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    return f"The {adjective} {noun} caught my eye from the corner of the room."


@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1) * int(number2)}."
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"


@app.route("/sayntimes/<word>/<n>")
def sayntimes(word, n):
    msg = "Invalid input. Please try again by entering a word and a number!"
    if n.isdigit():
        return f"{word} " * int(n)
    else:
        return msg


@app.route("/reverse/<word>")
def reverse(word):
    reverse_word = "".join(reversed(word))
    return reverse_word


@app.route("/strangecaps/<word>")
def strangecaps(word):
    new_word = ""
    counter = 0
    for letter in word:
        if counter % 2 == 0:
            new_word += letter.lower()
        else:
            new_word += letter.upper()
        counter += 1
    return f"{new_word}"


@app.route("/dicegame")
def dicegame():
    rand_int = random.randint(1, 6)
    won = "lost"
    if rand_int == 6:
        won = "won"
    return f"You rolled a {rand_int}. You {won}!"


if __name__ == "__main__":
    app.run(debug=True)
