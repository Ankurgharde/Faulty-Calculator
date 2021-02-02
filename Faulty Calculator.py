First_Number=int(input('Enter an First Number:'))
Second_Number=int(input('Enter an Second Number:'))
Operator=input("Choose Operator:")
if (Operator=='+') and (First_Number==44) and ( Second_Number==5):
    print('Addition of Two Number is:',80)
elif (Operator == '*') and (First_Number == 30) and (Second_Number == 7):
    print('Multiplication of Two Number is:',75)
elif (Operator == '/') and (First_Number == 66) and (Second_Number == 8):
    print('Division of Two Number is:',10)
elif Operator==('+'):
    print('Addition of Two Number is', First_Number + Second_Number)
elif Operator == ('*'):
    print('Multiplication of Two Number is',First_Number*Second_Number)
elif Operator==('/'):
    print('Division of Two Number is', First_Number / Second_Number)
else:
    print("Invalid")
