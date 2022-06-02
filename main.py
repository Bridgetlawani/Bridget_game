import random
print("Welcome")
print("starting game. rock:R paper:P scissors:S")

while True:

    choices = ["R", "P", "S"]

    CPU = random.choice(choices)
    player = None

    while player not in choices:
       player = input("Choose your weapon: R, P,or S: ").upper()
        
    if player == CPU:
        print("CPU: ", (CPU))
        print("player: ", (player))
        print("Tie!")

    elif player == "R":
        if CPU == "P":
            print("CPU: ", (CPU))
            print("player: ", (player))
            print("You lose!")
            break
        if CPU == "S":
            print("CPU: ", ((CPU)))
            print("player: ", (player))
            print("You win!")
    elif player == "S":
        if CPU == "R":
            print("CPU: ", (CPU))
            print("player: ", (player))
            print("You lose!")
            break
        if CPU == "P":
            print("CPU: ", (CPU))
            print("player: ", (player))
            print("You win!")
            break
    elif player == "P":
        if CPU == "S":
            print("CPU:", (CPU))
            print("player:", (player))
            print("You lose!")
            break
        if CPU == "R":
            print("CPU:", (CPU))
            print("player:", (player))
            print("You win!")
            break

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break
print("End game")
