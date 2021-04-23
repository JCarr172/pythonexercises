def near(x,y):

    for i in range(0,len(x)):
        z = ''
        if i == 0:
            z = x[1:]
        elif i == len(x)-1:
            z = x[:-1]
        else:
            z = z + x[:i]
            z = z + x[i+1:]
    
    return(z == y)