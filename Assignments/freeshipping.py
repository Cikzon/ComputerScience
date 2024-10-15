#make  function called free shipping
# that tells you inf you qualify for free shi
# only get shipping if prime member or order is at least 25$ 
# you are at least 18 18 years old or have a parent consent
# your function should take 4 peramiters 
#pime (boolean) cost (float) age (int) consent (bool)
#you can use more then one logical operator in a condition 
#us () to group if needed


def free_shipping(age,membership):
    age=input("how old are you")
    membership=input("do you have a membership")
    if age>=18 and membership==True:
        print("qualify for shipping")
    elif age<18:
        print("ask for permission child")
    elif membership==False:
        print("you aint nothing but a broke boy broke boyyy")






        

    
    