x = input('Please enter numbers seperated by spaces')
x = x.split(' ')

xint = []
N = 0
for i in range(0,len(x)-1):
    if x[i].isdigit() == True:
        xint.append(int(x[i]))
    else:
        N = 1

if N == 1:
    print('Not everything was a number')
else:
    print(xint[0], xint[-1])
    print(xint + xint)
    print(list(reversed(xint)))
    xint.sort()
    print(list(reversed(xint)))
