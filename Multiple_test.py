x = input('Enter a number ')
 
if x.isdigit() == True:
    x = int(x)
    y = x%4
    if y == 0: 
        print('You entered a multipe of 4')
    elif y == 2:
        print ('You entered a multiple of 2')
    else:
        print('You entered a negative number')
else:
    print('You did not enter a number')

x = input('Enter a number ')
y = input('Enter a number ')
 
if x.isdigit() == True and y.isdigit() == True:
    x = int(x)
    y = int(y)
    z = x%y
    if z == 0: 
        print(f'{x} is a multiple of {y}')
    else:
        print(f'{x} is not a multiple of {y}')
else:
    print('You did not enter two numbers')