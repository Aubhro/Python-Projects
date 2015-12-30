
string = input('String: \n')
list = string.split()
contain = True

for i in range(len(list)):
    if str(list[i]) == 'hello':
        print("The string " + string +  " does contain 'hello'")
        contain = False
        break


if contain == True:
    print("The string " + string +  " does not contain 'hello'")
    
