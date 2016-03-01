"""
Finds factorial using recursion and looping structure.
"""
while True:
    num = input("What number would you like to find the factorial of? \n")


    def while_factorial(num):
        factorial = 1
        for i in range(num - 1):
            factorial = factorial * (num - i)
        return factorial


    def recur_factorial(num):
        if num > 1:
            return num * recur_factorial(num - 1)
        else:
            return num


    print recur_factorial(num)
    print while_factorial(num)
