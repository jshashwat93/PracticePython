def horizontal():
    print(" ---", end="")


def vertical():
    print("|   ", end="")


if __name__ == '__main__':
    size = int(input("Enter the game board size: "))
    for time in range(size):
        for time in range(size):
                horizontal()
        print()
        for time in range(size + 1):
                vertical()
        print()
    for time in range(size):
        horizontal()
