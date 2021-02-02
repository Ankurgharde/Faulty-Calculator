First_Number=int(input('Enter an First Number:'))
Second_Number=int(input('Enter an Second Number:'))
Operator=input("Choose Operator:")
if (Operator=='+') and (First_Number==56) and ( Second_Number==9):
    print('Addition of Two Number is:',77)
elif (Operator == '*') and (First_Number == 45) and (Second_Number == 3):
    print('Multiplication of Two Number is:',555)
elif (Operator == '/') and (First_Number == 56) and (Second_Number == 6):
    print('Division of Two Number is:',4)
elif Operator==('+'):
    print('Addition of Two Number is', First_Number + Second_Number)
elif Operator == ('*'):
    print('Multiplication of Two Number is',First_Number*Second_Number)
elif Operator==('/'):
    print('Division of Two Number is', First_Number / Second_Number)
else:
    print("Invalid")