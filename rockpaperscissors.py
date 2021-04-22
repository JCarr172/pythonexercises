x = input('Rock, Paper or Scissors? ')
y = input('Rock, Paper or Scissors? ')

if x in ('Rock', 'Paper','Scissors') and y in ('Rock', 'Paper','Scissors'):
    if x == y:
        print('It is a draw')
    elif (x == 'Rock' and y == 'Paper') or (x == 'Paper' and y == 'Scissors') or (x == 'Scissors' and y == 'Rock'):
        print('Player 2 wins')
    else:
        print('Player 1 wins')
else:
    print('Not recognised commands')