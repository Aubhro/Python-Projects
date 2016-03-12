

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

string = ''

for j in range(length):
        if j == 0:
                string = str(list[0])
        else:
                string = string + ',' + str(list[j])

print(string)
