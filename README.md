# Faulty-Calculator
1) With the use of faulty calculator we can make some calculation faulty for your own purpose.  
#python code:-
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
    
2) In the above code,you see that only three calculation  wrong, these calculations are :-
  >> Addition of (44 + 5 )= 80, Ans is wrong (But except that problem (44 + 5), you can calculate all the "Addition" problem solve correctly.  
  >> Multiplication of (30 x 7) = 75, Ans is wrong  (But except that problem (30 x 7), you can calculate all the "Multiplication" problem solve correctly.
  >> Division of (66 / 8 = 8), Ans is wrong (But except that problem (66 / 8), you can calculate all the "Division" problem solve correctly.
  
