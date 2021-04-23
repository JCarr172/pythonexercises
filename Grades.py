x = int(input('Enter a number'))

print('With elif Statements')

if x > 85:
    print('This is a distinction')
elif x <= 85 and x >= 65:
    print('This is a pass')
else:
    print('This is a fail')

print('\nWithout elif statements')

if x > 85: print('This is a distinction')
if x <= 85 and x >= 65: print('This is a pass')
if x < 85: print('This is a fail')