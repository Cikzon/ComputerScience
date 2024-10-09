real_pass = "skibidi68" 
input_pass = input("Whats the password?\n>") 
if input_pass == real_pass: print("ACCESS GRANTED") 
else: print("ACCESS DENIED")




#.lower()
#.lower() changes the string to be all lowercase
#.upper() changes the string to be uppercase 
#.capitalize() changes the entire string to title case upper and lower Duhhhh
x=10
if x > 0: #nt every if needs an els
    print("x is a positive number")

    #second buddy is elif (else if)
elif x < 0:
    print("x is a negative number")

else:    # else always needs an if
    print("x is zero")


    #example

    light= input("what color is the light?")
    if light.lower()=="green":
        print("go")
    elif light.lower() == "yellow":
        print("STOP IF SAFE")
    elif light.lower()=="red":
        print("stop")
    else:
        print("yeild")
        
