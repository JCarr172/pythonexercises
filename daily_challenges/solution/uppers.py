def upper_letter(string):
    if isinstance(string, str) == True:
        capitals = []
        for i in range(0,len(string)):
            if string[i].isupper() == True:
                capitals.append((string[i],i))

        return capitals
    else:
        return "Not a string"
