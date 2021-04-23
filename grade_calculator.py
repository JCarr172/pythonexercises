print('Welcome to Grade Calculator')
m = int(input("Please enter your maths mark "))
c = int(input("Please enter your chemistry mark "))
p = int(input("Please enter your physics mark "))

avg = (m+c+p)/3
print(f"Your percentage score is {avg}%")
if avg >= 70:
    print('You scored a grade of: A')
elif avg >= 60:
    print('You scored a grade of: B')
elif avg >= 50:
    print('You scored a grade of: C')
elif avg >= 40:
    print('You scored a grade of: D')
else:
    print('You failed')