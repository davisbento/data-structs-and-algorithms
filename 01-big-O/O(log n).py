# create a binary search and return the index of the element
def binary_search(list, numberToFind):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == numberToFind:
            return mid
        if guess > numberToFind:
            high = mid - 1
        else:
            low = mid + 1
    return 'Not found'


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberToFind = 11

print('index found:', binary_search(list, numberToFind))
