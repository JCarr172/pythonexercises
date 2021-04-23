for i in range(1,51):
    x = ''
    if i%3 == 0: x = x + 'Fizz'
    if i%5 == 0: x = x + 'Buzz'
    if len(x) == 0: x = i
    print(x)