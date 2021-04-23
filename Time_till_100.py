from datetime import date

name = input('Please enter a name')
age = int(input('Please enter your age'))
birthday = input('Have you already had your birthday this year? Y/N ')

x = str(date.today())
x_int = int(x[:4])

if birthday == 'Y':
    print(f"Your name is {name} and you will turn 100 in the year {x_int+100-age}")
elif birthday == 'N':
    print(f"Your name is {name} and you will turn 100 in the year {x_int+99-age}")