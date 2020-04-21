#local vs global scopes
#local can use global, but cannot use other local variables
#global cannot use local variables
#basically local scope it's a locked black-box performing it's function and returns only the result, wyping all created variables
globalSpam = 66 #will be accessible in any 'local' function
def localFunc():
    global localSpam # 'global' will make variable available on global scope
    localVeriable = 'This is local var'
    localSpam = 88 #won't be usable in global as well as localVeriable which is declared above unless 'global' used
    print(localVeriable)
    print(globalSpam) #since variable is global, it can be used in any function
#from here starts global 'zone' and ends function 'black-box'
localFunc()
localVeriable = 'This is not local var, - it\'s global'
print(localVeriable)
# "print(localSpam)" will create an error since called localSpam does not exist beyond localFunc function
print(localSpam)
