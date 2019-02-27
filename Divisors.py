num = int(input("Enter a number to find its divisors: "))
divisors = []
for eachItem in range(1, num + 1):
    if num % eachItem == 0:
        divisors.append(eachItem)
print(divisors)
