

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

sum = 0
for count in range(length):
        sum = sum + list[count]

print (sum)


