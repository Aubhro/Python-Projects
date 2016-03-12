"""
Finds standard deviation of numerical data inputted by
the user. Data input ends when user types "done".
"""
import math
# mainList = [0, 3, 5, 7, 2, 6, 1, 9, 12, 37, 42]


def avg(data):
    total = 0.0
    for i in range(len(data)):
        total = total + data[i]
    average = (total / (len(data)))
    return average


def deviation(data, average):
    difference = []
    for i in range(len(data)):
        difference.append((average - data[i])**2)
    return math.sqrt(avg(difference))


def find(data):
    average = avg(data)
    return deviation(data, average)
mainList = []
print("Enter list one number at a time, when you are finished, type done")
while True:
    item = raw_input("Item ")
    if item == "done":
        break
    try:
        mainList.append(int(item))
    except ValueError:
        print ("Invalid item")
print "Average is: " + str(avg(mainList))
print "Population Standard Deviation is: " + str(find(mainList))
