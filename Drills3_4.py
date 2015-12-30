

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

for j in range(length):
        print('Item: ' + str(list[j]))
