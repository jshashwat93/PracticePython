import random


def initiate_game():
    actual_number = []
    for eachItem in range(4):
        actual_number.append(random.randint(0, 9))
    if len(actual_number) == len(set(actual_number)):
        return actual_number
    else:
        return initiate_game()


def play_game(actual_number):
    guess = input("Enter a 4-digit number with no repeats: ")
    attempt = 0
    while True:
        guess_list = []
        for eachItem in guess:
            guess_list.append(int(eachItem))
        cow = 0
        bull = 0
        attempt += 1
        for each in range(4):
            if guess_list[each] == actual_number[each]:
                cow += 1
            else:
                if guess_list[each] in actual_number:
                    bull += 1
        if cow == 4:
            print("You won in", attempt, "guesses")
            break
        else:
            print(cow, "cows and", bull, "bulls")
            guess = input("Enter a 4-digit number with no repeats: ")


if __name__ == "__main__":
    my_number = initiate_game()
    play_game(my_number)

