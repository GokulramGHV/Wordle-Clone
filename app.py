from rich import print as printt
from rich.markdown import Markdown
import random
import os

MARKDOWN = """
# Wordle CLI    
"""
title = Markdown(MARKDOWN)


GREEN = "white on dark_green"
YELLOW = "white on gold3"
GREY = "white on grey39"
BLACK = "white on grey27"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_row(string=" "*5, colors=(BLACK,)*5):
    string = string.upper()
    print()
    for i, char in enumerate(string):
        printt(f"[{colors[i]}]       [/]", end="  ")
    print()

    for i, char in enumerate(string):
        printt(f"[{colors[i]}]   {char}   [/]", end="  ")
    print()

    for i, char in enumerate(string):
        printt(f"[{colors[i]}]       [/]", end="  ")
    print()

def display_empty_board(n):
    printt(title)
    for i in range(n):
        display_row()

def display_board():
    printt(title)
    colors = (BLACK,) * 5
    for row in BOARD:
        if row == [0,]*5:
            display_row()
        else:
            colors = [tup[1] for tup in row]
            string = ''.join(tup[0] for tup in row)
            display_row(string, colors)
    return colors

file = open("word_list.txt", "r")
WORDS = [w.rstrip('\n') for w in file.readlines()]

WORD = random.choice(WORDS)

no_of_tries = 6

BOARD = [[0 for i in range(5)] for j in range(6)]
error = ""

clear_screen()
display_board()

while no_of_tries > 0:
    print()
    printt(error)
    error = ""
    current_word = input("Enter a word: ").lower()  

    if len(current_word) != 5:
        error = "[bold italic red]Please enter a word that has 5 letters![/]"
        clear_screen()
        display_board()
        continue
    elif current_word not in WORDS:
        error = "[bold italic yellow]Word not in list![/]"
        clear_screen()
        display_board()
        continue

    board_letters = ""
    for i in range(5):
        char = current_word[i]
        board_letters += char
        if char == WORD[i]:
            BOARD[6-no_of_tries][i] = (char, GREEN)
        elif char in WORD:
            if current_word.count(char) > 1 and board_letters.count(char) > WORD.count(char):
                BOARD[6-no_of_tries][i] = (char, GREY)
            else:
                BOARD[6-no_of_tries][i] = (char, YELLOW)
        else:
            BOARD[6-no_of_tries][i] = (char, GREY)    

    no_of_tries -= 1

    clear_screen()

    colors = display_board()
    
    if colors == [GREEN,]*5:
        printt("\nYou've found the word! Impressive!")
        break

if no_of_tries == 0:
    printt()
    printt("[white]Sorry! You couldn't guess the word...[/]")
    printt(f"The word is [bright_green bold]\"{WORD}\"[/]")
