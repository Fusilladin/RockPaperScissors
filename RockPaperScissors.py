# ROCK PAPER SCISSORS

print("Welcome to Rock, Paper, scissors. A two player game")
while True:

    x = input("PLAYER 1: Choose either Rock, Paper, or Scissors:  ")

    if x.lower() == 'rock':
        pass
    elif x.lower() == 'paper':
        pass
    elif x.lower() == 'scissors':
        pass
    else:
        print('\n>ERROR: Please choose only either "Rock, Paper or Scissors."')
        exit()

    y = input("PLAYER 2: Choose either Rock, Paper, or Scissors:  ")
    if y.lower() == 'rock':
        pass
    elif y.lower() == 'paper':
        pass
    elif y.lower() == 'scissors':
        pass
    else:
        print('\n>ERROR: Please choose only either "Rock, Paper or Scissors."')
        exit()

    while x.lower() == 'rock':
        if (y.lower() == 'scissors'):
            print('\nPLAYER 1 wins.')
            break
        if (y.lower() == 'paper'):
            print('\nPLAYER 2 wins.')
            break
        if (y.lower() == 'rock'):
            print('\nThe game is a tie.')
            break
        else:
            break

    while x.lower() == 'scissors':
        if (y.lower() == 'scissors'):
            print('\nThe game is a tie.')
            break
        if (y.lower() == 'paper'):
            print('\nPLAYER 1 wins.')
            break
        if (y.lower() == 'rock'):
            print('\nPLAYER 2 wins.')
            break
        else:
            break

    while x.lower() == 'paper':
        if (y.lower() == 'scissors'):
            print('\nPLAYER 2 wins.')
            break
        if (y.lower() == 'paper'):
            print('\nThe game is a tie.')
            break
        if (y.lower() == 'rock'):
            print('\nPLAYER 1 wins.')
            break
        else:
            break

    while True:
        z = input('Do you want to start a new game? Y/N  ')
        if z.upper() == 'Y':
            break
        if z.upper() == 'N':
            quit(print('Thanks for playing!'))
        if z.upper() != 'Y' or 'N':
            ((print('Please type only either "Y" or "N."')))
            continue


        # else:
        #     break



# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
