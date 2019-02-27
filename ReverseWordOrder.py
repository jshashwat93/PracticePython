def reverse_sentence(my_string):
    my_string = my_string.split()[::-1]
    my_string = " ".join(my_string)
    return my_string


user_string = input("Enter a string: ")
print(reverse_sentence(user_string))
