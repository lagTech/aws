#this function ask two number to user and substract them
nbr1= input("Enter the first number")
nbr2= input("Enter the second number")
def substraction(number1,number2):
    resultat = nbr1 - nbr2
    return resultat 
resultat = substraction(nbr2,nbr2) 
print(f'{nbr1} - {nbr2} = {resultat}')