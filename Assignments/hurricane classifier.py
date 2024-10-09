print("lets classify some hurricane levels, Tell me a Specific wind MPH and i can calculate what category it is!")
speed=input("input speed")
if speed <74:
    print("tropical storm")
elif speed <96:
    print("category 1")
elif speed <111:
    print("category 2")
elif speed <130:
    print("category 3")
elif speed <157:
    print("category 4")
elif speed >=157:
    print("category")
else:
    print("toilet skibidy not a valid respinse")
    

