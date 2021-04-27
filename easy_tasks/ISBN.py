code = input("Please enter the 12 digit code ")

def check(book_code):
    y = 0
    for i in range(0,len(code)):
        x = code[i]
        if i%2 == 0:
            y = y + int(x)
        else:
            y = y + 3*int(x)
    z = y%10
    check = 10 - z
    return z

print(check(code))
