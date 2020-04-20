#while loop + break (to prevent inf loop)

password = ''
while True:
    print('Please enter password: ')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')


# while + continue (to skip once)

i = 0
while i <= 10:
    i = i + 1
    print('i = ' + str(i))
    if i == 3:
        continue
print('Loop is finished without executing at i=3')
