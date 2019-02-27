import json


with open('birthday.json', 'r') as f:
    birthday_dict = json.load(f)
print('Welcome to the birthday dictionary. We know the birthdays of:')
for key, value in birthday_dict.items():
    print(key)
while True:
    lookup = input('Who''s birthday do you want to look up? (0 to exit): ')
    if lookup == '0':
        break
    print(birthday_dict.get(lookup, "Name not found."))
while True:
    add = input("Do you want to add a birthday? (Y/N): ")
    if add == 'Y':
        name = input("Enter name: ")
        birthday = input("Enter birthday (MM/DD/YYYY): ")
        birthday_dict[name] = birthday
    else:
        break
with open('birthday.json', 'w') as f:
    birthday_dict = json.dump(birthday_dict, f)
