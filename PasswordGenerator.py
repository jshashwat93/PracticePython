import random
import string


def password_generator(length):
    start = string.printable.find('!')
    end = string.printable.find('~') + 1
    special_chars = string.printable[start:end]
    while True:
        my_password = ''
        for eachItem in range(length):
            my_password += string.printable[random.randint(0, len(string.printable) - 7)]
        if (any(x.isupper() for x in my_password) and any(x.islower() for x in my_password)
                and any(x.isdigit() for x in my_password) and any(map(lambda x: x in special_chars, my_password))):
            return my_password


pass_length = int(input("Enter desired length of password: "))
print(password_generator(pass_length))
