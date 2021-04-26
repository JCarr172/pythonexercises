print('Welcome to Grade Calculator')
m = int(input("Please enter your maths mark "))
c = int(input("Please enter your chemistry mark "))
p = int(input("Please enter your physics mark "))

def average(m,c,p):
    avg = (m+c+p)/3
    if avg >= 70:
        letter = 'A'
    elif avg >= 60:
        letter = 'B'
    elif avg >= 50:
        letter = 'C'
    elif avg >= 40:
        letter = 'D'
    else:
        letter = 'E'
    return avg, letter

score = average(m,c,p)

print(f"Your average grade was {score[0]}% and grade {score[1]}")