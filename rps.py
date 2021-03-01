from random import randint

t = ["rock","paper", "scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    hand = input("rock, paper, scissors? ")

    if hand == computer:
        print("Tie!")
    elif hand == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", hand)
        else:
            print("You Win!", hand, "smashes", computer)
    elif hand == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", hand)
        else:
            print("You Win!", hand, "covers", computer)
    elif hand == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", hand)
        else:
            print("You Win!", hand, "cuts", computer)
    player = False
    computer = t[randint(0,2)]
    #rock beats scissors
    #paper beats rock
    #Scissors beats paper