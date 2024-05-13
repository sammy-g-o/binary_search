"""binary search"""

print('enter values for the list')

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

list_of_num = (range(int(input()),int(input()))) #type is generator object
search(arrays=list_of_num, key=int(input('Enter key: ')))
