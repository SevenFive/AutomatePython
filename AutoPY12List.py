# list data type

span = [1, 2, 3, 4, 5]
bacon = ['egg', 'oil', 'salt', 'carrot', 'sugar', 'milk']
print(span)
print(span[0])
print(bacon[-3])
del bacon[3]
print(bacon)
doubleSpan = span * 2
print(doubleSpan)
intStrList = span + bacon
print(intStrList)
if '3' in intStrList:
    print(True)
else:
    print(False)
# here we can see that list can contain both int and str items
if 3 and 'egg' in intStrList:
    print(True)
else:
    print(False)
# can take a range of items in the list using 'slice'
print(intStrList[2:5])
# index 7 will be included
print(intStrList[7:])
# index 4 will be excluded
print(intStrList[:-6])
# last but no the least - 'list' as a data type
print(list('This is a string'))
