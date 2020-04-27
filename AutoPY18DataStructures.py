# Data Structures - contains a few dictionaries (list of dictionaries)

# simple dictionary
myPC = {'producer': 'Dell', 'model': 'Latitude', 'CPU': 'Intel Core i9'}

# data structure
allPC = []
allPC.append({'producer': 'Dell', 'model': 'Latitude', 'CPU': 'Intel Core i9'})
allPC.append({'producer': 'Lenovo', 'model': 'Y50', 'CPU': 'Intel Core i7'})
allPC.append({'producer': 'Toshiba', 'model': 'Satellite Pro', 'CPU': 'Intel Core i5'})
allPC.append({'producer': 'HP', 'model': 'Pavilion', 'CPU': 'AMD Ryzen 5'})
print(allPC)

# "type()" can be used to check data type of the var
print(type(23))
print(type('dk43df'))
print(type(3.14))
print(type(theBoard))
