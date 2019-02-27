from functools import lru_cache


@lru_cache()
def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input("Enter how many fibonacci numbers you want to display: "))
for eachItem in range(1, n + 1):
    print(fibonacci(eachItem))

'''This is the iterative way
    a = 0
    b = 1
    for eachItem in range(num):
        a, b = b, a + b
        print(a)'''
