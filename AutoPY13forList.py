# combining for loop with list

for i in range(4):
    print(i)
# alt 1
for i in [0, 1, 2, 3]:
    print(i)
# alt 2 but cannot start from 0 in this case since it's integer
for i in list(str(1234)):
    print(i)

# using len in combination with range to create big lists
print(list(range(7)))
print(list(range(5, 100, 5)))
# now reverting this
someList = ['pan', 'monitor', 'phone', 'plant', 'table', 'headphones', 'diary', 'gum', 'peer']
for x in range(len(someList)):
    print('Index ' + str(x) + ' contains ' + someList[x])

# multiple assignment
a, b = 1, 100
print(a)
print(b)
a, b = b, a
print(a)
print(b)
# multiple assignment combining with a list
cat = ['black', 'slim', 'superhero']
color = cat[0]
body = cat[1]
occupation = cat[2]
print(color + ' ' + body + ' ' + occupation)
# use case
bat = ['black', 'muscular', 'vigilante']
color2, body2, occupation2 = bat    # instead of listing all items ['black', 'muscular', 'vigilante']
print(color2 + ' ' + body2 + ' ' + occupation2)

# shortcut
spam = 34
spam += 1   # instead of "spam = spam + 1" also works for -= *= /= %=
print(spam)
