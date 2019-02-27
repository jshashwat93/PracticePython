from collections import Counter
import json

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

with open('birthday.json', 'r') as f:
    birthday_dict = json.load(f)
birthdays = birthday_dict.values()
birthday_list = []
for value in birthdays:
    value = int(value[0:2])
    birthday_list.append(num_to_string[value])
c = Counter(birthday_list)
print(c)
