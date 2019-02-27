num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 4 == 0:
        print("Even and divisible by 4")
    else:
        print("Even Number")
else:
    print("Odd Number")
check = int(input("Enter a number to check divisibility: "))
if num % check == 0:
    print("The original number is divisible by the number you entered")
else:
    print("The original number is not divisible by the number you entered")
