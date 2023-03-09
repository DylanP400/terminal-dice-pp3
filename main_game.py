from dice_art import DICE_ART
import random


def print_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    for i in range(5):
        print(DICE_ART[dice1][i], "    ", DICE_ART[dice2][i])

def roll_dice():
    """
    To ask the player if they want to roll the dice
    """
    while True:
        response = input("Please use 'r' to roll your dice\n")
        if response == "r":
            print("Dice Rolling....")
            print_dice()
            break
        else:
            print("You have to enter 'r' to roll your dice/nTry again!")


def introduction():
    """
    Introduction asking if you need istructions or not
    """
    print()
    print("Hello and welcome to Dice in the Terminal\n")
    print("Do you want to practice your skills before you hit the casino?\n")
    print("If so you have came to the right place\n")
    player_name()
    response = input("Do you know how to play? (yes/no)\n")
    if response == "yes":
        print("Get ready your Game is comming right up.....\n")
        roll_dice()
    elif response == "no":
        print("\nLoading instructions....\n")
        how_to_play()
    else:
        print("\nPlease enter 'yes' or 'no'\nTry again\n")
        introduction()


def how_to_play():
    """
    Shows you how to play the game and starts or resets
    the game depending on the answer
    """
    print("The player rolls the dice and adds the numbers together.\n")
    print("If the total is 7 or 11, the player wins.\n")
    print("If the total is 2, 3, or 12, the player loses.\n")
    print("If the total is any other number (4, 5, 6, 8, 9, or 10),\n")
    print("that number becomes the 'point'.\n")
    print("The player then continues to roll the dice until they\n")
    print("either roll the'point' again and win, or they roll a 7 and lose.\n")
    while True:  # Loop to ask the same question if there is a error
        response = input("\nDo you want to start the game? (yes/no)\n")
        if response == "yes":
            print("Best of luck your Game is coming right up.....\n")
            roll_dice()
            break
        elif response == "no":
            print("You just want to watch the world burn...Restarting game\n")
            restart()
            break
        else:
            print("\nPlease enter 'yes' or 'no'.\n")


def player_name():
    """
    For setting the players name.
    """
    print("------------------\n")
    name = input("What is your name?\n\n------------------\n")
    print(f"\nWelcome to the game {name}\n")


def restart():
    """
    For restarting the game
    """
    response = input("Do you know how to play? 'yes' or 'no'\n")
    if response == "yes":
        print("Get ready your Game is comming right up.....\n")
    elif response == "no":
        print("\nLoading instructions....\n")
        how_to_play()
    else:
        print("\nPlease enter yes or no\nTry again\n")
        introduction()


introduction()  


"""
I need to put the roll dice inside a funtion that asks you to roll the dice 
"""