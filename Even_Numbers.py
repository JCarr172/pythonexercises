my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def even_numbers(list):
    y = []
    for x in my_list:
        if x%2 == 0: y.append(x)
    return y

print(even_numbers(my_list))