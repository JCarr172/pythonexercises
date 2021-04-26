import dice

def roll2dice():
    x = dice.rolld20()
    y = dice.rolld20()
    return x, y

print(roll2dice())
