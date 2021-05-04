def f(number):
    total = 0
    if isinstance(number, int) == True:
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number > 1:
            sequence = [1,1]
            for x in range(1,number-1):
                sequence.append(sequence[-1]+sequence[-2])
            return sequence[-1]
        else:
            return "Function requires a positive integer"

    else:
        return "Function requires a positive integer"
