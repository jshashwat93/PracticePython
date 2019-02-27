import random
while True:
    num = random.randrange(1, 10)
    guesses = 0
    guess = input("Enter a number: ")
    if guess != "exit":
        while int(guess) != num:
            if int(guess) > num:
                print("Too high")
                guesses += 1
            elif int(guess) < num:
                print("Too low")
                guesses += 1
            guess = input("Enter a number: ")
            if guess == "exit":
                break
    if guess != "exit":
        guesses += 1
        print("Exactly Right. You took", guesses, "guesses\n")
    else:
        break
