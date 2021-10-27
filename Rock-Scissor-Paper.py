while True:
    print("Welcome to Rock-Paper-Scissors game")
    player1 = input("Enter choice for player1: ")
    player2 = input("Enter choice for player2: ")
    if player1 == "rock":
        if player2 == "scissors":
            print("Congratulations, Player1. You are the WINNER!")
        elif player2 == "paper":
            print("Congratulations, Player2. You are the WINNER!")
        else:
            print("Same choices, Its a DRAW!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Congratulations, Player1. You are the WINNER!")
        elif player2 == "rock":
            print("Congratulations, Player2. You are the WINNER!")
        else:
            print("Same choices, Its a DRAW!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Congratulations, Player1. You are the WINNER!")
        elif player2 == "scissors":
            print("Congratulations, Player2. You are the WINNER!")
        else:
            print("Same choices, Its a DRAW!")
    else:
        print("Enter Valid Choices only...")
    new = input("Do you want to start a new game (y/n)?")
    if new == 'n':
        break

            
