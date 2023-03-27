"""
A game of Craps wrote in Python for my PP3
"""
# To import the dice art from dice_art.py
from dice_art import DICE_ART

# To import the random module
import random

# To import the time module
# Slows down the Terminal output
import time

# To Import the colorama module
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Global varibles
# Tracks the player roll
player_roll = 0

# Shows the game is not over can be changed to True to end the game.
game_over = False

# Tracks the last roll
last_roll = 0


def introduction():
    """
    Introduction welcoming you to the game and asks
    do you know how to play which leads to the
    intructions or starts the game.
    """
    print(Fore.RED + "\n======================================")
    time.sleep(1)
    print(Fore.BLUE + "█░█ █▀▀ █░░ █░░ █▀█   ▄▀█ █▄░█ █▀▄")
    print(Fore.BLUE + "█▀█ ██▄ █▄▄ █▄▄ █▄█   █▀█ █░▀█ █▄▀\n")
    print(Fore.BLUE + "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█")
    print(Fore.BLUE + "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█\n")
    print(Fore.BLUE + "▀█▀ █▀▀ █▀█ █▀▄▀█ █ █▄░█ ▄▀█ █░░   █▀▄ █ █▀▀ █▀▀")
    print(Fore.BLUE + "░█░ ██▄ █▀▄ █░▀░█ █ █░▀█ █▀█ █▄▄   █▄▀ █ █▄▄ ██▄\n")
    time.sleep(2)
    print(Fore.BLUE + "Do you want to practice your skills before you hit\n")
    print(Fore.BLUE + "▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀ █ █▄░█ █▀█")
    print(Fore.BLUE + "░█░ █▀█ ██▄   █▄▄ █▀█ ▄█ █ █░▀█ █▄█\n")
    print(Fore.BLUE + "If so you have came to the right place")
    print(Fore.RED + "=========================================")
    time.sleep(3.5)
    player_name()
    while True:  # Loop to ask the same question if there is a error
        response = input(Fore.CYAN + "Do you know how to play? (y/n)\n")
        if response == "y":
            print(Fore.GREEN + "Get ready your game is comming right up....\n")
            time.sleep(2)
            roll_dice()
        elif response == "n":
            print(Fore.GREEN + "\nLoading instructions....\n")
            time.sleep(1.5)
            how_to_play()
        else:
            print(Fore.GREEN + "\nPlease enter 'y' or 'n'\nTry again\n")


def how_to_play():
    """
    Explains how to play the game and starts or exits
    the game depending on the players choice
    """
    print(Fore.YELLOW + "The player rolls the dice.\n")
    print(Fore.YELLOW + "And adds the numbers together.\n")
    print(Fore.YELLOW + "If the total is 7 or 11 the player wins.\n")
    time.sleep(3)
    print(Fore.YELLOW + "If the total is 2, 3, or 12, the player loses.\n")
    time.sleep(2)
    print(Fore.YELLOW + "If the total is any other number.\n")
    print(Fore.YELLOW + "(4, 5, 6, 8, 9, or 10)\n")
    time.sleep(2)
    print(Fore.YELLOW + "That number becomes the 'point'.\n")
    print(Fore.YELLOW + "The player then continues.\n")
    print(Fore.YELLOW + "To roll the dice until they,\n")
    print(Fore.YELLOW + "Either roll the 'point' again and win,\n")
    print(Fore.YELLOW + "or they roll a 2, 3, 7, 11 or 12 and lose.\n")
    while True:  # Loop to ask the same question if there is a error
        response = input(Fore.CYAN + "\nDo you want to start the game?(y/n)\n")
        if response == "y":
            print(Fore.GREEN + "Best of luck your game is coming right up..\n")
            time.sleep(2)
            roll_dice()
            break
        elif response == "n":
            print(Fore.RED + "Maybe next time....\n")
            print(Fore.RED + "Exiting game...\n")
            restart()
            break
        else:
            print(Fore.RED + "\nPlease enter 'y' or 'n'.\n")


def player_name():
    """
    Asks the player for their name and logs the name
    """
    print(Fore.BLUE + "------------------")
    name = input(Fore.CYAN + "What is your name?\n")
    print(Fore.BLUE + "------------------")
    print(f"{Fore.GREEN}\nWelcome to the game {name}\n")
    player_age()


def player_age():
    """
    To check if the player is old enough to play
    if te player is over 21 the game starts if 
    the player is not over 21 the game restarts
    """
    try:
        age = int(input(Fore.CYAN + "What age are you?\n\n"))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid age.")
        player_age()
        return
    if age >= 21:
        print(Fore.GREEN + "You meet the age requirements\n")
    else:
        print(Fore.RED + "I am sorry but you are not old enough to play\n")
        time.sleep(1.5)
        print(Fore.RED + "Error...Restarting Terminal Dice\n")
        time.sleep(1.5)
        introduction()


def print_dice(first_dice, second_dice):
    """
    To print the Dice art to the terminal
    I used this line of code from this video
    https://www.youtube.com/watch?v=x-Ag2_bJ40Y&t=308s
    """
    for i in range(5):
        print(DICE_ART[first_dice][i], " ", DICE_ART[second_dice][i])


def roll_dice():
    """
    To ask the player if they want to roll the dice and adds
    the total once the dice have been printed.
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    while True:  # Loop to ask the same question if there is a error
        response = input(Fore.CYAN + "Please use 'r' to roll your dice\n")
        if response == "r":
            print(Fore.YELLOW + "Dice Rolling....\n")
            time.sleep(1.5)
            print_dice(dice1, dice2)
            time.sleep(.5)
            print(f"{Fore.YELLOW}you rolled a total of {total}\n")
            game_logic(total)
            break
        else:
            print(Fore.YELLOW + "You have to enter 'r' to roll your dice\n")
            print(Fore.YELLOW + "Try Again!\n")


def game_logic(total):
    """
    This is for the logic to make the game work.
    If you roll a 7 or 11 on your first turn you win.
    If you roll a 2, 3 or 11 on your first turn you lose.
    If you roll a 4, 5, 6, 8, 9, 10 on your first go you have hit the point.
    You need to roll the point again to win the game
    if you dont win on your first go.
    If you are on your second turn which is your point
    and you roll 2, 3, 7, 11 or 12 you lose.
    You have to win on your first turn or hit your point twice in a row to win.

    This function has 2 of the global varibles seen at the top.
    It checks if a user hit their point on their second roll if not
    then it check if the player is on the first roll and has won or not.
    It implements the player roll by one everytime you win or hit your point.
    If you lose it resets and restarts the game
    """
    global last_roll
    global player_roll
    if total == last_roll:
        print(Fore.GREEN + "You hit your point again and Won!\n")
        player_roll += 1
        time.sleep(2)
        reset_game()
        restart()
    elif total in (4, 5, 6, 8, 9, 10):
        print(Fore.CYAN + "You have hit your point\n")
        player_roll += 1
        last_roll = total
        roll_dice()
    elif total in (7, 11) and player_roll == 0:
        print(Fore.GREEN + "player wins\n")
        time.sleep(1.5)
        reset_game()
        restart()
    elif total in (2, 3, 12):
        print(Fore.RED + "player loses\n")
        time.sleep(1.5)
        reset_game()
        restart()
    elif total in (7, 11) and player_roll != 0:
        print(Fore.RED + "player loses\n")
        time.sleep(1.5)
        reset_game()
        restart()
    else:
        print("Invalid roll\n")
        time.sleep(1)
        reset_game()
        restart()


def restart():
    """
    For restarting the game and exiting the game.
    """
    response = input(Fore.CYAN + "Do you want to play again? 'y' or 'n')\n")
    if response == "y":
        print(Fore.GREEN + "Get ready your Game is coming right up.....\n")
        time.sleep(1.5)
        roll_dice()
    elif response == "n":
        time.sleep(2)
        print(Fore.RED + "-----------------------")
        print(Fore.RED + "Exiting the game now!")
        print(Fore.RED + "------------------------")
        print(Fore.GREEN + "========================")
        print(Fore.BLUE + "Thank you for playing!!!")
        print(Fore.GREEN + "========================")
        time.sleep(5)
        introduction()
    else:
        print(Fore.GREEN + "\nPlease enter 'y' or 'n'\nTry again\n")
        restart()


def main_game():
    """
    Main game function to start the game once called
    it leads into the introduction.
    """
    introduction()


def reset_game():
    """
    Resets the game and the global varibles.
    """
    global last_roll
    global player_roll
    global game_over
    player_roll = 0
    last_roll = 0
    game_over = False


main_game()
