#for loop

for number in range(4, 20, 3):
    print(number)
print('End')

#example of Gauss total of sum 1+2+3+4+...+99+100

total = int()  #optional "total = 0"
for number in range(101):  #optional "for number in range(0-101):"
    total = total+number
print('Sum of all numbers from 0 to 100 is ' + str(total))
