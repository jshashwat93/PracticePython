my_dict = {}
with open('nameslist.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in my_dict:
            my_dict[line] += 1
        else:
            my_dict[line] = 1
        line = f.readline()
print(my_dict)

my_dict2 = {}
with open('Training_01.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line[3:line.find('/', 3)] in my_dict2:
            my_dict2[line[3:line.find('/', 3)]] += 1
        else:
            my_dict2[line[3:line.find('/', 3)]] = 1
        line = f.readline()
print(my_dict2)
