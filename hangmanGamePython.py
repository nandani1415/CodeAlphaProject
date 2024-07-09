import random
import os

def run():
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP","C#",
        "LINUX","UNIX","COMPUTER",
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attempts = 6

    while True:
        # os.system("clear")  From Unix/Linux/Mac
        os.system("cls")  # From Windows
        print(IMAGES[6 - attempts])
        for character in spaces:
            print(character, end=" ")
        print("\n")

        letter = input("Choose a letter: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:
            attempts -= 1

        if "_" not in spaces:
            # os.system("clear")   From Unix/Linux/Mac
            os.system("cls")  # From Windows
            print("You've won! The word was:", word)
            break

        if attempts == 0:
            # os.system("clear")   From Unix/Linux/Mac
            os.system("cls")  # From Windows
            print(IMAGES[6])
            print("You have lost! The word was:", word)
            break

if __name__ == "__main__":
    run()
