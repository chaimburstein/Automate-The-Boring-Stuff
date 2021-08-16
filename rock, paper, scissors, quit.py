#Rock, Paper, Scissors, QUIT!

# this next bit imports modules that are part of the "standard library"
# random deals with random numbers and sys deals with systems

import random
import sys

print('Rock, Paper, Scissors')

# The following variables track wins/losses/ties
wins=0
losses=0
ties=0

#main game loop

while True:
    print('%s Wins, %s Losses, %s Ties'%(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('a quitter never wins')
            sys.exit()
        if playerMove == 'r' or 'p' or 's':
            break
        print('Type one of r, p, s or q.')

    #show player choice
    if playerMove == 'r':
        print('Rock vs.')
    elif playerMove == 'p':
        print('Paper vs.')
    elif playerMove == 's':
        print('Scissors vs.')

    #show computer choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove= 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #shows record of win/loss/tie
    if playerMove == computerMove:
        print('Tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win')
        wins = wins + 1
    else:
        print('You Lose')
        losses = losses + 1

