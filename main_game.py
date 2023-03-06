def introduction():
    print("Hello and welcome to Dice in the Terminal")
    print("Do you want to practice your skills before you hit the casino?\nIf so you have came to the right place")
    response = input("Do you know how to play? (yes/no)")
    if response == "yes":
        print("Get ready your Game is comming right up.....")
    elif response == "no":
        print("Loading instructions")
    else:
        print("\nPlease enter yes or no\nTry again\n")
        introduction()
    


introduction()