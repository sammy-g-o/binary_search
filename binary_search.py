"""This is a binary search algorithm

It will accept a range of two values
Then searches through it to find the key
"""


# code by Giwa Abdulsamad


def search(arrays, key):
    """
    it goes through the given list and searches for the given key

    Args:
        arrays (list): range of integers
        key (int): target number
    """
    beg = 0
    end = len(arrays) - 1
    midd = int((beg + end)/2)
    while beg < end and arrays[midd] != key:
        if key > arrays[midd]:
            beg = midd + 1
            midd = int((beg + end)/2)
            if arrays[midd] == key:
                print(f"{key} is in index {midd}")
                break
        elif arrays[midd] == key:
            print(f"{key} is in index {midd}")
            break
        elif key < arrays[midd]:
            end = midd - 1
            midd = int((beg + end)/2)
            if arrays[midd] == key:
                print(f"{key} is in index {midd}")
                break
        elif arrays[midd] == key:
            print(f"{key} is in index {midd}")
            break
