#! python3

#   all python programs for OSs should start with Shebang line
#   Windows (version check but not required in general): #! python3
#   OS X: #! /usr/bin/env python3
#   Linux: #! /usr/bin/python3

import sys  # used to add command arguments and execute in .py via .bat


print('Hello there!')
print(sys.argv)

#   works in pair with batch file
#   batch 'hello.bat' content:

#   @py c:\users\Seven\PycharmProjects\AutomatePython\ScriptHello.py %*
#   @pause

#   @pause make it possible to see terminal window before it closes.
#   @pyw - will run program windowless
#   %* - used to path any arguments stored in argv

#   to run batches instantly from RUN AS we have to add their location to the PATH
#   Control panel > System > Advanced > Advanced > Environment Variables and add
#   batch 'hello' will start with simply hello entered into RUN AS
#   for utility of sys.argv type exp. 'hello arg1 arg2 arg3'
