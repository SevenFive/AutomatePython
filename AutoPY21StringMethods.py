# String Methods
# isalpha() - letters only
# isalnum() - letters and number only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only

# ".upper" ".lower" methods
spam = 'Hello there!'
print(spam)  # output: Hello there!
print(spam.upper())  # output: HELLO THERE!
# use case prompting input 'yes' but user can type 'YES' or 'yes'
print('Would you like to start a new game?')
userInput = input()
if userInput.lower() == 'yes':  #adding .lower method so any YES input will be acceptable
    print('Input received successfully')
else:
    print('Until next time then.')
print('=======================')
# ".isupper" ".islower" methods
print(spam.islower())   # output: False  -- since it has one upper case 'H'
spam = "h" + spam[1:11] # making str correction so it fits all lower case check
print(spam.islower())   # output: True -- changed H to h
print('=======================')
# using methods instantly
print('HELLO'.islower())    # output: False
print('Hello'.lower().islower())    # output: True
