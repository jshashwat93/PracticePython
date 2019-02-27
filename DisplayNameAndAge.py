name = input("Enter name: ")
age = int(input("Enter age: "))
times = int(input("How many times do you want to see the message: "))
for eachTime in range(times):
    print("Hi", name, "you will be 100 in the year", 2019 + 100 - age)
