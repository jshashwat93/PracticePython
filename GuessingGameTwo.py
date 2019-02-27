computer_guess = 50
possible_answers = list(range(1, 101))
print(computer_guess)
user_answer = input("Too low, high or correct? ")
attempts = 1
while True:
    if user_answer == "correct":
        print("Computer answered in", attempts, "attempts")
        break
    attempts += 1
    current_index = possible_answers.index(computer_guess)
    if user_answer == 'low':
        possible_answers = possible_answers[current_index + 1:]
    else:
        possible_answers = possible_answers[:current_index]
    mid = len(possible_answers) // 2
    computer_guess = possible_answers[mid]
    print(computer_guess)
    user_answer = input("Too low, high or correct? ")


