import numpy

def even_digits(x,y):
    evendigits = []
    if type(x) == int and type(y) == int:
        for num in range(x,y+1):
            digits = numpy.array([int(digit) for digit in str(num)])
            if all(digits%2 == 0) == True:
                evendigits.append(num)
        return evendigits

    else:
        return 

print(even_digits(10,30))