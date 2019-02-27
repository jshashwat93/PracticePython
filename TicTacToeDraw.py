game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
squares = 0
player = 1
while squares < 9:
    for eachLine in game:
        print(eachLine)
    output_str = "Player " + str(player) + " enter location you want to select (x,y): "
    user_input = input(output_str)
    user_input = user_input.split(",")
    user_input = [int(x) for x in user_input]
    if game[user_input[0] - 1][user_input[1] - 1] == 0:
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
        print("Spot already take")
