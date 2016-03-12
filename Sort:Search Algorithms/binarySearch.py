"""
Binary search program that returns index of item user selects in list.
Works with any list that is sorted from least to greatest.
"""

while True:
    library = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    find = input("What number would u like to find? \n")
    print library


    def findHalf(list):
        if len(library) == 1:
            return library[0]
        elif len(library) % 2 == 1:
            half = (int(len(list) / 2) + 1)
            return half
        else:
            half = int(len(list) / 2)
            return half


    def removeFront(length):
        for i in range(length):
            del library[0]


    def removeBack(length):
        half = findHalf(library)
        for i in range(length + 1):
            del library[len(library) - 1]


    print findHalf(library)

    while len(library) > 1:
        if library[findHalf(library)] < find:
            removeFront(findHalf(library))
        elif library[findHalf(library)] > find:
            removeBack(findHalf(library))
        elif library[findHalf(library)] == find:
            print str(find) + " is at index " + str(findHalf(library))
            print 'Done!'
            break
