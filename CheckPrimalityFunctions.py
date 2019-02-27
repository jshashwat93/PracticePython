def check_prime(number):
    count = 0
    for eachItem in range(1, number + 1):
        if number % eachItem == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not A Prime")


while True:
    num = int(input("Enter a number to find if it is a prime number: "))
    if num == 0:
        break
    check_prime(num)
