import random
from dice_art import DICE_ART


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
        response = input("Please use 'r' to roll your dice\n")
        if response == "r":
            print("Dice Rolling....\n")
            print_dice(dice1, dice2)
            print(f"you rolled a total of {total}\n")
            game_logic(total)
            break
        else:
            print("You have to enter 'r' to roll your dice/nTry again\n!")


def game_logic(total):
    """
    The Logic behind the game
    """
    if total == 7 or total == 11:
        print("You win!\n")
        restart()
    elif total == 2 or total == 3 or total == 12:
        print("You lost!\n")
        restart()
    else:
        print(f"You have hit the Point\nYour point is {total}")
        roll_dice()


# change to instructions
def introduction():
    """
    Introduction asking if you need instructions or not
    """
    print("============================================\n")
    print("█░█ █▀▀ █░░ █░░ █▀█   ▄▀█ █▄░█ █▀▄")
    print("█▀█ ██▄ █▄▄ █▄▄ █▄█   █▀█ █░▀█ █▄▀\n")
    print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█")
    print("▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█\n")
    print("▀█▀ █▀▀ █▀█ █▀▄▀█ █ █▄░█ ▄▀█ █░░   █▀▄ █ █▀▀ █▀▀")
    print("░█░ ██▄ █▀▄ █░▀░█ █ █░▀█ █▀█ █▄▄   █▄▀ █ █▄▄ ██▄\n")
    print("Do you want to practice your skills before you hit the casino?\n")
    print("If so you have came to the right place\n")
    print("============================================\n")
    player_name()
    response = input("Do you know how to play? (yes/no)\n")
    if response == "yes":
        print("Get ready your game is comming right up.....\n")
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
    print("That number becomes the 'point'.\n")
    print("The player then continues to roll the dice until they\n")
    print("Either roll the'point' again and win, or they roll a 7 and lose.\n")
    while True:  # Loop to ask the same question if there is a error
        response = input("\nDo you want to start the game? (yes/no)\n")
        if response == "yes":
            print("Best of luck your game is coming right up.....\n")
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
    name = input("What is your name?\n\n------------------\n\n")
    print(f"\nWelcome to the game {name}\n")
    player_age()


def player_age():
    """
    To check if the player is old enough to play
    """
    age = int(input("What age are you?\n"))
    if age >= 21:
        print("You meet the age requirements\n")
    elif age < 21:
        print("I am sorry but you are not old enough to play\n")
        print("Error...Restarting Terminal Dice\n")
        introduction()
    else:
        print("Please enter your age\n")


def restart():
    """
    For restarting the game
    """
    response = input("Do you want to play again? 'yes' or 'no'\n")
    if response == "yes":
        print("Get ready your Game is comming right up.....\n")
        roll_dice()
    elif response == "no":
        print("\nLoading instructions....\n")
        how_to_play()
    else:
        print("\nPlease enter yes or no\nTry again\n")
        introduction()


def main_game():
    introduction()


main_game()

# make a welcome function that links to intructions
# add art
# maybe add color