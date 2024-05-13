from binary_search import search

print("This is a binary search algorithm\nIt will accept a range of two values")
list_of_num = (range(int(input("first value:\n")),int(input("second value:\n")))) #type is generator object
search(arrays=list_of_num, key=int(input('Enter key: ')))

