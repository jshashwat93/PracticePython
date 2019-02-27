def print_clue(clue_list):
    for eachLetters in clue_list:
        print(eachLetters, end="")
        print(' ', end="")
    print()


if __name__ == '__main__':
    while True:
        count = 0
        incorrect = []
        word = 'EVAPORATE'
        print('Welcome to Hangman!')
        clue = ['_'] * len(word)
        while True:
            if '_' not in clue:
                print_clue(clue)
                print("You Win")
                break
            print_clue(clue)
            guess = input('Guess your letter: ')
            if guess in incorrect:
                print("Letter already guessed. Try Again.")
                continue
            if guess in word:
                if guess not in clue:
                    for eachItem in range(len(word)):
                        if guess == word[eachItem]:
                            clue[eachItem] = guess
                else:
                    print("Letter already guessed. Try Again.")
            else:
                count += 1
                print("You have", 6 - count, "incorrect guesses remaining")
                incorrect.append(guess)
                if count == 6:
                    print("You Lose")
                    break
        again = input("Do you want to play again? (Y/N): ")
        if again == 'N':
            break

