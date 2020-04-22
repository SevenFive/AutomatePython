# guess random number game program

import random
print('Hello! What\'s your name?')
playerName = input()
print('Welcome ' + playerName + '! Let\'s play a guess game.')
randomNum = random.randint(0, 10)
print('I am thinking about number between 0 and 10. You have 5 attempts. Try to guess which one. Check you intuition ;)')
guessOne = input()
i = 0
while randomNum != guessOne and i < 5:
    print('Nope')
print('That is correct! Brilliant. You are mindreader or rather memory reader!')
exit()
