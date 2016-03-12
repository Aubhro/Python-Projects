

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

index = input('Index: \n')
index = int(index) 

if index > length or index < 1:
        print('The index ' + str(index) + ' is out of bounds for a list of length '+str(length))
else:
        print('The item at index ' + str(index) + ' is '+str(list[index-1])) 
