# String Methods
# isalpha() - letters only
# isalnum() - letters and number only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only (all words in string starts with Upper case)

# ".upper" ".lower" methods
spam = 'Hello there!'
print(spam)  # output: Hello there!
print(spam.upper())  # output: HELLO THERE!
print('=======================')
# ".isupper" ".islower" methods
print(spam.islower())   # output: False  -- since it has one upper case 'H'
spam = "h" + spam[1:11] # making str correction so it fits all lower case check
print(spam.islower())   # output: True -- changed H to h
print('=======================')
# using methods instantly
print('HELLO'.islower())    # output: False
print('Hello'.lower().islower())    # output: True
print('=======================')
# .startswith() .endswith() methods
print('Hello world!'.startswith('He'))  # output: True
print('Hello world!'.endswith('world!'))    # output: True
print('=======================')
# .join() method
print(', '.join(['cats', 'coffee', 'crates']))
print('=======================')
# .split() method does the opposite
print('My name is Simon'.split())   # splits at each ' '
print('My name is Simon'.split('m'))  # splits at each 'm'
print('=======================')
# .rjust() .ljust() .center() and .strip() .lstrip() .rstrip() .replace() methods
print('rjust'.rjust(11))    # by default will be rjusted by ' ' spaces
print('ljust'.rjust(20, "*"))
print('ljust with fifty minus length of string asterisks'.ljust(50, '$'))
print('This is a center'.center(24, '-'))
print('   <-- 3 spaces and 10 spaces -->          '.strip())    # spaces removed
print('   <-- 3 spaces and 10 spaces -->          '.rstrip())
print('   <-- 3 spaces and 3 sap -->sapsapsapsap'.lstrip())
print('Hello my friend Enrico!'.replace('e', '@'))
print('=======================')
# use case of .lower method - prompting input 'yes' but user can type 'YES' or 'yes'
print('Would you like to start a new game?')
userInput = input()
if userInput.lower() == 'yes':  #adding .lower method so any YES input will be acceptable
    print('Input received successfully')
else:
    print('Until next time then.')
