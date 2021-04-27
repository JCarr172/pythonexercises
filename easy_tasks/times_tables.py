def times_table(number):
    for num in range(1, number+1):
        string = (f"{num}")
        for i in range(2, number+1):
            string += (f"\t{num*i}")

        print(string)


times_table(10)