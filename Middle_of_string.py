x = input('Enter a long string')
l = len(x)
if l >= 7 and l%2 == 1:
    y = int(l/2)
    print(x[y-1:y+2])
    if x.isalpha() == True:
        print(f'{x[:y-1].lower()}{x[y-1:y+2].upper()}{x[y+2:].lower()}')
    else:
        print('Not all  elements are letters')
else: 
    print('String is not long enough or not odd')

