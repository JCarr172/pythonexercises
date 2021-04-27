

def fizzbuzz(target):
    for i in range(1,target):
        x = ''
        if i%3 == 0: x = x + 'Fizz'
        if i%5 == 0: x = x + 'Buzz'
        if len(x) == 0: x = i
        print(x)
    return

count = int(input("What number do you want to count till? "))
fizzbuzz(count)