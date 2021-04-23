my_list = [1,1,2,3,4,5,13,21,34,55,89]
y = []

for x in my_list:
    if x < 5:
        print(x)
        y.append(x)

print(y)

z = [x for x in my_list if x < 5]
print (z)

n = int(input("Please enter a number"))

for x in my_list:
    if x < n:
        print(x)
        y.append(x)

print (y)