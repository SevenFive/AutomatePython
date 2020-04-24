# Methods are functions that are 'called on' values.

# For instance methods for list are the following:
#   index() returns the index of an item in the list
#   append() adds a value to the end of a list
#   insert() adds a value anywhere inside a list
#   remove() removes an item, specified by the value, from a list
#   sort() sorts the items in a list
#   sort(reverse=True) keyword argument can sort in reverse order
# Sorting is in ASCII-betical order to bypass it sort(key=str.lower)

countries = ['Spain', 'USA', 'France', 'Austria', 'Canada', 'China', 'Bulgaria']
print(countries)
print(countries.index('Canada'))
countries.append('UAR')
print(countries)
countries.insert(1, 'Bolivia')
print(countries)
countries.remove('Canada')  # if there are a few same items, only the first in the list will be removed
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
