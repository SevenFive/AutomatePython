#pyperclip - build in function for 3rd party modules installations

import pyperclip
a = str()
pyperclip.copy('Hello world!')
a = pyperclip.paste()
print(a)

#result - 'Hello world!