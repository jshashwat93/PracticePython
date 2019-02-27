import random


def random_word_selector(my_filename):
    word_list = []
    with open(my_filename, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            word_list.append(line)
            line = f.readline()
    print("Random word:", word_list[random.randint(0, len(word_list))])


if __name__ == '__main__':
    filename = 'sowpods.txt'
    random_word_selector(filename)
