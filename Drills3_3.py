

from random import randint
length = randint(5,10)
list = []

for i in range(0, length):
        list.insert( i, randint(0,10))

print(list)

index = input('Index: \n')
index = int(index) 
list.remove(list[index-1])
print('Removing the item at index ' + str(index) + ' gives '+str(list)) 
