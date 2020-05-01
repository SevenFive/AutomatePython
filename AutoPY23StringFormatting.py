# String Formatting or just making inserted information look better

name = 'Azula'
time = 'Tomorrow'
place = 'Imperial palace arena of Fire Lord'
activity = 'Agni Kai'

print('Attention nation of fire! ' + time + ' there will be ' + activity + ' between heir to the throne prince Zuko and princess ' + name + ' in ' + place + '!')

# alternative and better way to do that is the following
print('Attention nation of fire! %s there will be %s between heir to the throne prince Zuko and princess %s in %s!' % (time, activity, name, place))
