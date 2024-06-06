import random
options = ("rock", "paper", "scissors")
run = True
while run:
    player = None
    comp = random.choice(options)
    while player not in options:
        player = input("enter ur option(paper,rock or scissor): ")

        print(f"player: {player}")
        print(f"computer: {comp}")
        if player == comp:
            print("its a tie!!")
        elif player == "rock" and comp == "scissors":
            print("You win!")
        elif player == "paper" and comp == "rock":
            print("You win!")
        elif player == "scissors" and comp == "paper":
            print("You win!")
        else:
            print("you loose,try again!")

        play_again = input("play again? (y/n)").lower()
        if not play_again == "y":
            run = False

print("Thanks for playing!")