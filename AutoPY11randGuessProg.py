# guess random number game program
# will add error handler a bit later

import random
print('Hello! What\'s your name?')
playerName = input()
print('Welcome ' + playerName + '! Let\'s play a guess game.')
randomNum = random.randint(0, 10)
print('I am thinking about number between 0 and 10. You have 5 attempts. Try to guess which one. Check you intuition ;)')
i = 1   # alternatively replaced by range
while i < 6:    # alternatively "for guessesTaken in range(1, 6):"
    print('Take a guess')
    guessOne = input()  #alt "guessOne = str(input())
    if int(guessOne) == randomNum:  # alternatively move this block out of while loop with correct/incorrect options
        print('You won! Correct! It is numner ' + str(guessOne) + '. You guessed my number in ' + str(i) + ' attempts. Maybe you should try a national lottery?')
        exit(0) # alternatively "break"
    if int(guessOne) < randomNum:
        i = i + 1
        print('Your guess is too low.')
    if int(guessOne) > randomNum:
        i = i + 1
        print('Your guess is too high.')
print('5 attempts were used. But you can try again.')   # alt "if guessOne == randomNum: .... else: print try again.
# alt to display number of attempts just use "print(str(guessesTaken)"
