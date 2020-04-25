# Dictionaries which include key-value pairs (like items in lists) and keys as indexes in lists
# Dictionaries are MUTABLE (var are refer) and UNORDERED (no first key-value pair)

myPC = {'type': 'laptop', 'CPU': 'Intel', 'color': 'black', 'Producer': 'Dell'}
print(myPC)
print('I own a ' + myPC['Producer'] + ' ' + myPC['type'] + ' which is ' + myPC['color'] + ' color.')

# methods for dictionaries
# keys, values, items,
print(list(myPC.keys()))
print(list(myPC.values()))
print(list(myPC.items()))

# alternatively using for loop to print the same
for i in myPC.keys():
    print(i)

for v, w in myPC.items():
    print(v, w)
# the same can be done with on variable for items
for a in myPC.items():
    print(a)

# to check if values, keys are stored
laptopBoolean = 'laptop' in myPC.values()
print(laptopBoolean)
colorBoolean = 'color' in myPC.keys()
print(colorBoolean)

# to check the same way but with custom result if the object does not exist
checkGet = myPC.get('size', 'None exist')
print(checkGet)
# "get()" method can be used in many ways like bellow
pcNum = {'desktop': 3, 'laptop': 1}
print('I currently have available ' + str(pcNum.get('desktop', 0)) + ' PCs and ' \
      + str(pcNum.get('monoblock', 0)) + ' monoblocks.')

# "setdefault()" method can be used to only assign value if it's not already exist
pcNum.setdefault('server', 10)  # key-value pair will be added if it doesn't exist already
print(pcNum)
pcNum.setdefault('desktop', 45)  # if the value and the key already exist nothing will be changes
print(pcNum)
# the same thing in a old way
if 'datafarm' not in pcNum:
    pcNum['datafarm'] = 32
print(pcNum)
