x = int(input('Enter a number'))

print('With elif Statements')

def grade(score):
    if score > 85:
        result = 'This is a distinction'
    elif score <= 85 and x >= 65:
        result = 'This is a pass'
    else:
        result = 'This is a fail'
    return result

print(grade(x))

print('\nWithout elif statements')

def grades(score):
    if x > 85: results = 'This is a distinction'
    if x <= 85 and x >= 65: results = 'This is a pass'
    if x < 65: results = 'This is a fail'
    return results

print(grades(x))