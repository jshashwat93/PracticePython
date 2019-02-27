import random
a = [random.randrange(10) for eachItem in range(random.randrange(10))]
b = [random.randrange(10) for eachItem in range(random.randrange(10))]
# print(list(set([eachItem for eachItem in a if eachItem in b])))
print(list(set(a) & set(b)))
