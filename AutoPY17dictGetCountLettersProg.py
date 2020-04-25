# program to count the amount of symbols in any text given

import pprint   # using pprint module to display better


text = 'A practical programming course for office workers who want to improve their productivity.'
textCounter = {}

for symbol in text.upper(): # " .upper()" method used to convert all letters to upper case so we can have sum of all upper and lower case letters
    textCounter.setdefault(symbol, 0)
    textCounter[symbol] = textCounter[symbol] + 1
print(textCounter)
# to display in a better way with pprint module we imported earlier above
pprint.pprint(textCounter)
# the same but saved in var output as a string data type
output = pprint.pformat(textCounter)
print(output)
