# Function to add numbers

def addnumbers(num1, num2):
    summ = num1 + num2
    print('Sum of {} and {} is: {}'.format(num1, num2, summ))

#Declare variables
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
addnumbers(num1,num2)