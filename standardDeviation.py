import math
mainList = [0, 3, 5, 7, 2, 6, 1, 9, 12, 37, 42]


def avg(data):
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    average = total / len(data)
    return average


def deviation(data, average):
    difference = []
    for i in range(len(data)):
        difference.append((average - data[i])**2)
    return math.sqrt(avg(data))


def find(data):
    average = avg(data)
    return deviation(data, average)


print find(mainList)
