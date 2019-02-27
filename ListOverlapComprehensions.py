import random
a = [random.randrange(0, 10) for eachItem in range(random.randrange(1, 11))]
b = [random.randrange(0, 10) for eachItem in range(random.randrange(1, 11))]
print(list(set(a) & set(b)))
