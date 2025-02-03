# Implement hangman game through intelligent agent. 
# Two players are playing. Player one is issuing the letter to the word. 
# Player two is arranging the letter in the word.
# Conditions: 
# 1. For every right guess, removal of the body part from the figure.
# 2. For every wrong guess, addition of the body part to the figure.
# 3. If word is completed or total body parts are completed, one of the player wins the game.

import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "ximenia", "yellow", "zucchini"]

def print_part(part):
    if part == "head":
        print("  O")
    elif part == "left arm":
        print(" /", end="")
    elif part == "right arm":
        print("\\")
    elif part == "body":
        print("|", end="")
    elif part == "left leg":
        print(" /", end="")
    elif part == "right leg":
        print(" \\")

def start_game():
    word = words[random.randint(0, len(words) - 1)]
    chars = list(word)
    guess = []
    shuffled = random.sample(chars, len(chars)) # Shuffle the word
    body_parts = ["head", "left arm", "body", "right arm", "left leg", "right leg"]
    body_parts.reverse()
    figure = []
    print()
    for(i, char) in enumerate(shuffled):
        shouldGuess = True
        while shouldGuess: 
            print("Letter: ", char,end="\n\n")
            for(part) in figure:
                print_part(part)
            for(j) in range(len(word)):
                if(j in guess):
                    print(word[j], end=" ")
                else:
                    print("_", end=" ")
            print(end="\n\n")
            input_char = int(input("Guess the position: ")) - 1
            if input_char > len(word) - 1 or input_char < 0:
                print("Invalid position!")
                continue
            if(char == word[input_char]):
                print("Correct!")
                guess.append(input_char)
                print(chr(27) + "[2J")
                if len(guess) == len(word):
                    print("You win!")
                    shouldGuess = False
                    exit(0)
                if len(figure) > 0:
                    body_parts.append(figure.pop())
                shouldGuess = False
            else:
                print("Wrong!")
                print(chr(27) + "[2J")
                if len(body_parts) > 0:
                    figure.append(body_parts.pop())
                else: 
                    print("You lose!")
                    shouldGuess = False
                    exit(0)

start_game()