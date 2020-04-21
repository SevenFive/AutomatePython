# try/except part 2

print('How many cats do you have?')
try:
    numCats = int(input())
    if numCats >= 4 and numCats < 31:   #optionaly instead of adding int in line 4, can here int - also will move try block
        print('That\'s a lot of cats you have ^^')
    elif numCats > 30 and numCats < 51:
        print('Wow, sounds like a future article in newspaper =)')
    elif numCats > 50 and numCats < 1000:
        print('I think you have a serious \'cat problem\' 0_0')
    elif numCats > 999:
        print('911 - we have an army of cats here! Mayday-mayday! @_@')
    elif numCats >0 and numCats < 4:
        print('That\'s not that many cats -_-')
    elif numCats == 0:
        print('None? Do you want to buy one? Only today -50% discount! And if you buy two dis... Wait! Just listen!')
    elif numCats < 0:
        print('What do you meant by negative number? Did you ate that many cats? 0_0')
except ValueError:
    print('Please enter digits only -_- srsly')
except:
    print('Oopsie! Somehow you almost broke it!')
