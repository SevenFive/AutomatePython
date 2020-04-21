# custom functions

def helloThere():
    print('Hello there!')


def welcomeHere():
    print('Hey, Welcome Here!')
    print('What is your name?')


def myName(name):
    print('My name is ' + name + '. But WHAT is your name?')


def doubleNum(number):
    double = number * number
    print('Answer is ' + str(double))
    return number - 1


# run functions

helloThere()
welcomeHere()
myName('Sarah')
myName('Sara')
myName('S-A-R-A-H')
myName('S-A-R-A')
# act func
doubleNum(5)
# var act func
minusOne = doubleNum(666)
print(minusOne)

# "None" is a data type which "print()" function returns
#spam print()
#spam == None

# "end" no new line
print('Hello', end='')
print('World')

# "sep" can used to change separation between arguments
print('one','two','three','four',sep='_')
