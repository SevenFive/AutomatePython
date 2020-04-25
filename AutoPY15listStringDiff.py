# Some differences between string and list data types

# list values are MUTABLE so that they CAN be modified
bacon = ['b', 'a', 'c', 'o', 'n']  # as a string "bacon = 'bacon'" it is not possible to modify by indexes
bacon[2] = 'r'
print(bacon)

# but string values are IMMUTABLE and CANNOT be changed even thought that they can be displayed by index, etc.
egg = 'tomatoes'
print(egg[3])  # but something like egg[3] = 'e' wont work since it's modification

# as a string by copying we create the same but a new copy
spam = 'spam - spam of a spam'
cheese = spam
cheese = 'cheese - not a spam anymore'
print(spam)
print(cheese)

# as a list by copying we do not create a copy, but just a new reference to the same list
salt = ['This', 'is', 'a', 'salt']
sugar = salt
sugar.insert(2, 'still')
print(salt)
print(sugar)  # so modification via new reference changed the list for both references


# this could lead to different issues like the following
def change(name):
    name.append(456789)  # this will affect the list even thought it's in def block


Deniz = [1, 2, 3]
change(Deniz)
print(Deniz)

# to create a complete new copy of the list with a new list which is the same as origin use copy.deepcopy
import copy

pepper = copy.deepcopy(salt)
pepper[1] = 'is not'
pepper.remove('still')
print(salt)
print(pepper)

# Good practise using Line Continuation for big lists
good = ['text',
        'words',
        'spells',
        'integers']
# also optionally "\" to ignore start of new line
great = 'A lot of text here and more than can be fit here in one line without making things look really ugly ' + \
        "and long. So we use \\ sign to fit it visually in editor but still correct in the output"
print(great)
