x = input('Please enter numbers seperated by spaces')
x = x.split(' ')
print(x)
if x.isdigit() == True:
    pass
else:
    print("They weren't all numbers")