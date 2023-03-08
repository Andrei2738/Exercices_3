def ex1():                                            #Reverse a string
    string = input("Input string:")
    print (string[::-1])

def ex2():                                            #Check if a number is even or odd
    nr = int(input("Input number:"))
    if nr % 2 == 0:
        print("Number is even")
    else: print("Number is odd")

def ex3():                                            #Find the largest number in a list
    numbers = [2,8,14,631,53]
    print (max(numbers))

def ex4():                                            #Find the smallest number in a list
    numbers = [2,8,14,631,53]
    print (min(numbers))

def ex5():                                            #Check if a number is divisible by another number
    firstNumber = int(input("Input first number:"))
    secondNumber = int(input("Input second number:"))
    if firstNumber % secondNumber == 0:
        print("The first number is divisible by the second number")
    else:
        print("The first number is not divisible by the second number")