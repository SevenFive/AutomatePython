# pyperclip

# first make sure that it is installed already by going into cmd console
# C:\Users\Seven\AppData\Local\Programs\Python\Python38-32>pip.exe install pyperclip

import pyperclip
pyperclip.copy('Hello! It is supposed to copied to clipboard now!')
print(pyperclip.paste())
