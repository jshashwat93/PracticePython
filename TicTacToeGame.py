def check_winner(game):
    winner = [' ']
    if len(set(list((game[0][0], game[0][1], game[0][2])))) == 1:
        winner = set(list((game[0][0], game[0][1], game[0][2])))
    elif len(set(list((game[1][0], game[1][1], game[1][2])))) == 1:
        winner = set(list((game[1][0], game[1][1], game[1][2])))
    elif len(set(list((game[2][0], game[2][1], game[2][2])))) == 1:
        winner = set(list((game[2][0], game[2][1], game[2][2])))
    elif len(set(list((game[0][0], game[1][0], game[2][0])))) == 1:
        winner = set(list((game[0][0], game[1][0], game[2][0])))
    elif len(set(list((game[0][1], game[1][1], game[2][1])))) == 1:
        winner = set(list((game[0][1], game[1][1], game[2][1])))
    elif len(set(list((game[0][2], game[1][2], game[2][2])))) == 1:
        winner = set(list((game[0][2], game[1][2], game[2][2])))
    elif len(set(list((game[0][0], game[1][1], game[2][2])))) == 1:
        winner = set(list((game[0][0], game[1][1], game[2][1])))
    elif len(set(list((game[0][2], game[1][1], game[2][0])))) == 1:
        winner = set(list((game[0][2], game[1][1], game[2][0])))
    winner = list(winner)
    if winner[0] == 'X':
        winner = "Player 1"
    elif winner[0] == 'O':
        winner = "Player 2"
    return winner


def start_game(game):
    squares = 0
    player = 1
    while squares < 9:
        winner = check_winner(game)
        if winner != [' ']:
            draw_game(game)
            print("The winner is:", winner)
            if winner == 'Player 1':
                return 1
            else:
                return 2
        draw_game(game)
        possible_solutions = ['1,1', '1,2', '1,3', '2,1', '2,2', '2,3', '3,1', '3,2', '3,3']
        output_str = "Player " + str(player) + " enter location you want to select (x,y): "
        user_input = input(output_str)
        while user_input not in possible_solutions:
            print("Invalid Input. Try Again.")
            draw_game(game)
            user_input = input(output_str)
        user_input = user_input.split(",")
        user_input = [int(x) for x in user_input]
        if game[user_input[0] - 1][user_input[1] - 1] == ' ':
            if player == 1:
                game[user_input[0] - 1][user_input[1] - 1] = 'X'
            else:
                game[user_input[0] - 1][user_input[1] - 1] = 'O'
            if player == 1:
                player = 2
            else:
                player = 1
            squares += 1
        else:
            print("Spot already taken. Try Again.")
    if squares == 9:
        draw_game(game)
        print("It is a draw")


def draw_game(game):
    size = 3
    for time in range(size):
        for times in range(size):
                print(" ---", end="")
        print()
        for times in range(size):
                print("|", game[time][times], "", end="")
        print("|")
    for time in range(size):
        print(" ---", end="")
    print()


if __name__ == '__main__':
    player1 = 0
    player2 = 0
    while True:
        my_game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        a = start_game(my_game)
        if a == 1:
            player1 += 1
        elif a == 2:
            player2 += 1
        again = input("Do you want to play again (Y/N): ")
        if again.lower() == 'n':
            break
    print("Final Score: Player 1 :", player1, "Player 2 :", player2)
