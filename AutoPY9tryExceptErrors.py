#try and except statement - errors handling

def devide40by(devider):
    try:
        return 40 / devider
    except ZeroDivisionError:
        print('division by zero is resrticted')
    except:
        print('make sure that entered value is numerical')
print(devide40by(5))
print(devide40by(4))
print(devide40by(2))
print(devide40by(0))    #will create ZeroDivisionError: division by zero - which has to be handled by try/except
print(devide40by(1))
print(devide40by(-5))
