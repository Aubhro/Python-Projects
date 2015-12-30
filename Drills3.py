

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

index = input('Index: \n')
index = int(index) 

print('The item at index ' + str(index) + ' is '+str(list[index-1])) 
