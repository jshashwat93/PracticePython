import random

# Quick search using pre-built python functions


def normal_search(my_list, element):
    if element in my_list:
        return True
    else:
        return False

# Recursive Binary Search


def recursive_binary_search(data, number, start, end):
    mid = start + (end-start)//2
    if start > end:
        return False
    if number == data[mid]:
        return True
    elif number < data[mid]:
        return recursive_binary_search(data, number, start, mid - 1)
    else:
        return recursive_binary_search(data, number, mid + 1, end)

# Iterative Binary Search


def iterative_binary_search(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == "__main__":
    a = [random.randrange(100) for eachItem in range(49)]
    a.sort()
    print(a)
    b = int(input("Enter a number to find in the list: "))
    print(normal_search(a, b))
    print(recursive_binary_search(a, b, 0, len(a) - 1))
    print(iterative_binary_search(a, b))
