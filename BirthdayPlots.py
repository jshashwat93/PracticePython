from bokeh.plotting import figure, show, output_file
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
x = []
y = []
output_file("plot.html")
x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                "November", "December"]
for item, value in c.items():
    x.append(item)
    y.append(value)
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)
