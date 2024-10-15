prime=True
cost=20
age=18
consent=False
#if(prime==True or cost >=25) and (age >= 18 or consent==True):
if prime:
    if age >=18:
        print("free shipping applied")
    elif consent:
        print("you got shipping child")
    else:
        print("nope shipp")

        #decide if e need an umbrella
        # you need an umbrella if its raining and u going outside
        rain=input("is it raining outside?")
        outside = input("do you plan on going out?")
        if rain.lower()=="yes":
            print("bring")
