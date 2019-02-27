prime = []
happy = []
with open('primenumbers.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        prime.append(int(line))
        line = f.readline()
with open('happynumbers.txt', 'r') as f2:
    line2 = f2.readline()
    while line2:
        line2 = line2.strip()
        happy.append(int(line2))
        line2 = f2.readline()
solution = list(set(prime) & set(happy))
solution.sort()
print(solution)
