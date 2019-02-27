game = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]
winner = {0}
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
print(winner)
