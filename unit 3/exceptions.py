def divide_two_numbers():
 try:
    x = int(input("what us tge first number \n>"))
    y = int(input("what is the second number \n >"))
    print(x / y)
 except: # if anything in the try block creates an error
    # the try block stops immediately
    # the rest of the try block never finishes running, its skipped
    # if try block executes without an error, the except is skipped
    #the only way to get into the except is to "throw" an error

 
    divide_two_numbers()

    
 #if = try
 #else = except