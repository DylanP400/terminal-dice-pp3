def introduction():
    """
    Introduction asking if you need istructions or not
    """
    print("Hello and welcome to Dice in the Terminal")
    print("You can practice your skills before you hit the casino?")
    print("If so you have came to the right place")
    player_name()
    response = input("Do you know how to play? (yes/no)")
    if response == "yes":
        print("Get ready your Game is comming right up.....")
    elif response == "no":
        print("\nLoading instructions\n")
        how_to_play()
    else:
        print("\nPlease enter yes or no\nTry again\n")
        introduction()


def how_to_play():
    """
    Shows you how to play the game and starts or resets
    the game depending on the answer
    """
    print("The player rolls the dice and adds the numbers together.")
    print("If the total is 7 or 11, the player wins.")
    print("If the total is 2, 3, or 12, the player loses.")
    print("If the total is any other number (4, 5, 6, 8, 9, or 10),")
    print("that number becomes the 'point'.")
    print("The player then continues to roll the dice until they")
    print("either roll the'point'again and win, or they roll a 7 and lose.")
    response = input("\nDo you want to start the game? (yes/no)")
    if response == "yes":
        print("Best of luck your Game is comming right up.....")
    elif response == "no":
        print("You just want to watch the world burn...Restarting game\n")
        introduction()
    else:
        print("\n You have to click yes or no\n")
        how_to_play()


def player_name():
    """
    For setting the players name.
    """
    print("------------------")
    name = input("What is your name?\n------------------\n")
    print(f"\nwelcome to the game {name}\n")


introduction()
