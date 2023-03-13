import random
from dice_art import DICE_ART
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def print_dice(first_dice, second_dice):
    """
    To print the Dice art to the terminal
    """
    for i in range(5):
        print(DICE_ART[first_dice][i], "    ", DICE_ART[second_dice][i])


def roll_dice():
    """
    To ask the player if they want to roll the dice
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    while True:
        response = input(Fore.CYAN + "Please use 'r' to roll your dice\n")
        if response == "r":
            print(Fore.YELLOW + "Dice Rolling....\n")
            print_dice(dice1, dice2)
            print(f"{Fore.YELLOW}you rolled a total of {total}\n")
            game_logic(total)
            break
        else:
            print(Fore.YELLOW + "You have to enter 'r' to roll your dice")
            print(Fore.YELLOW + "Try Again!\n")


def game_logic(total):
    """
    The Logic behind the game
    """
    if total == 7 or total == 11:
        print(Fore.GREEN + "You win!\n")
        restart()
    elif total == 2 or total == 3 or total == 12:
        print(Fore.RED + "You lost!\n")
        restart()
    else:
        print(f"{Fore.YELLOW}You have hit the Point\nYour point is {total}")
        roll_dice()


# change to instructions
def introduction():
    """
    Introduction asking if you need instructions or not
    """
    print(Fore.BLUE + "\n======================================\n")
    print(Fore.BLUE + "█░█ █▀▀ █░░ █░░ █▀█   ▄▀█ █▄░█ █▀▄")
    print(Fore.RED +  "█▀█ ██▄ █▄▄ █▄▄ █▄█   █▀█ █░▀█ █▄▀\n")
    print(Fore.BLUE + "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█")
    print(Fore.RED +  "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█\n")
    print(Fore.BLUE + "▀█▀ █▀▀ █▀█ █▀▄▀█ █ █▄░█ ▄▀█ █░░   █▀▄ █ █▀▀ █▀▀")
    print(Fore.RED +  "░█░ ██▄ █▀▄ █░▀░█ █ █░▀█ █▀█ █▄▄   █▄▀ █ █▄▄ ██▄\n")
    print(Fore.GREEN + "Do you want to practice your skills before you hit\n")
    print(Fore.BLUE + "▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀ █ █▄░█ █▀█")
    print(Fore.RED +  "░█░ █▀█ ██▄   █▄▄ █▀█ ▄█ █ █░▀█ █▄█\n")
    print(Fore.GREEN + "If so you have came to the right place\n")
    print(Fore.BLUE + "==========================================\n")
    player_name()
    response = input(Fore.CYAN + "Do you know how to play? (yes/no)\n")
    if response == "yes":
        print(Fore.GREEN + "Get ready your game is comming right up.....\n")
        roll_dice()
    elif response == "no":
        print(Fore.GREEN + "\nLoading instructions....\n")
        how_to_play()
    else:
        print(Fore.GREEN + "\nPlease enter 'yes' or 'no'\nTry again\n")
        introduction()


def how_to_play():
    """
    Shows you how to play the game and starts or resets
    the game depending on the answer
    """
    print(Fore.YELLOW + "The player rolls the dice,\n")
    print(Fore.YELLOW + "and adds the numbers together.\n")
    print(Fore.YELLOW + "If the total is 7 or 11 the player wins.\n")
    print(Fore.YELLOW + "If the total is 2, 3, or 12, the player loses.\n")
    print(Fore.YELLOW + "If the total is any other number")
    print(Fore.YELLOW + "(4, 5, 6, 8, 9, or 10),\n")
    print(Fore.YELLOW + "That number becomes the 'point'.\n")
    print(Fore.YELLOW + "The player then continues")
    print(Fore.YELLOW + "to roll the dice until they\n")
    print(Fore.YELLOW + "Either roll the'point' again and win,")
    print(Fore.YELLOW + "or they roll a 7 and lose.\n")
    while True:  # Loop to ask the same question if there is a error
        response = input(Fore.CYAN + "\nDo you want to start the game?(y/n)\n")
        if response == "yes":
            print(Fore.GREEN + "Best of luck your game is coming right up..\n")
            roll_dice()
            break
        elif response == "no":
            print(Fore.GREEN + "You just want to watch the world burn...")
            print(Fore.GREEN + "Restarting game\n")
            restart()
            break
        else:
            print(Fore.RED + "\nPlease enter 'yes' or 'no'.\n")


def player_name():
    """
    For setting the players name.
    """
    print(Fore.BLUE + "------------------\n")
    name = input(Fore.CYAN + "What is your name?\n\n")
    print(Fore.BLUE + "\n------------------\n")
    print(f"{Fore.GREEN}\nWelcome to the game {name}\n")
    player_age()


def player_age():
    """
    To check if the player is old enough to play
    """
    age = int(input(Fore.CYAN + "What age are you?\n\n"))
    if age >= 21:
        print(Fore.GREEN + "You meet the age requirements\n")
    elif age < 21:
        print(Fore.RED + "I am sorry but you are not old enough to play\n")
        print(Fore.RED + "Error...Restarting Terminal Dice\n")
        introduction()
    else:
        print(Fore.GREEN + "Please enter your age\n")


def restart():
    """
    For restarting the game
    """
    response = input(Fore.CYAN + "Do you want to play again? 'yes' or 'no'\n")
    if response == "yes":
        print(Fore.GREEN + "Get ready your Game is comming right up.....\n")
        roll_dice()
    elif response == "no":
        print(Fore.GREEN + "\nLoading instructions....\n")
        how_to_play()
    else:
        print(Fore.GREEN + "\nPlease enter yes or no\nTry again\n")
        introduction()


def main_game():
    introduction()


main_game()

# make a welcome function that links to intructions
# add art
# maybe add color