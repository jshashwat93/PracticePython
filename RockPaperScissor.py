while True:
    while True:
        player1 = input("Player 1 choose rock, paper or scissor: ")
        player2 = input("Player 2 choose rock, paper or scissor: ")
        valid = ["rock", "paper", "scissor"]
        if player1 and player2 not in valid:
            print("Invalid Input")
        else:
            break
    result = "Player 1 Wins"
    if player1 == player2:
        result = "Draw"
    elif player1 == "rock":
        if player2 == "paper":
            result = "Player 2 Wins"
    elif player1 == "paper":
        if player2 == "scissor":
            result = "Player 2 Wins"
    elif player1 == "scissor":
        if player2 == "rock":
            result = "Player 2 Wins"
    print(result)
    new = input("Start new game? (y/n): ")
    if new == "n":
        break
