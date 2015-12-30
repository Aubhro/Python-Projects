

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

index = input('Index: \n')
index = int(index) 
sum = 0

if index > length or index < 1:
        print('The index ' + str(index) + ' is out of bounds for a list of length '+str(length))
else:
        for j in range(1, index+1):
                sum = sum + list[j - 1]

print('The sum of the first the list ' + str(index) + ' is the list '  +str(list) + ' is ' + str(sum))
