def start_adventure():
    print("made by Mathias Westermeyer\n")
    print("the year is 2360, humanity has taken to the stars, you are captain rex, a solo scavenger and pirate who explores the fringe(space/planets)")
    print("you are offered a contract aboard your ship to explore an abandoned space station for valuable salvage\n")
    print("1. do you accept the contract?\n")
    print("2. or deny the contract and continue the cruise?\n")

    choice = input("> ")
    if choice=="1":
        accept_contract()

    elif choice== "2":
        continue_on()
    else:
        print(" option 1, or 2")    


def continue_on():
    print("you continue on the path, with no rocks your stomach grows hungry and you die")

    answer = input("do you want to restart?\n")
    if answer.lower() == "yes":
        start_adventure()
    else:
        print("story over...")
        exit()

def accept_contract():
    print("you accept the contract, it offers up some good rocks, enough for some chicken alfredo,  you get ready to board the station and face whatever is waiting for you on the other side\n")
    print("as you board and walk around its dark and cold, lights flicker and you can se your breath blow in the light emitting from the cheap flashlight you've had, you feel like something is following you.\n")
    print("1. do you investigate the mysterious presence you feel?\n")
    print("2. Walk back to the ship and fly safely\n")
    print("3. catch the entity and face it head on\n")
     
    choice2=input("> ")
    if choice2=="1":
        print("you walk deeper into the cold space station you hear a mechanical voice, you see it, a 6 foot robot with some remnants of silicone skin representing a muscular build, a huge red eye head that looks like a stop light and a wife beater and joggers\n")
        investigate_bot()
        
     
    elif choice2=="2":
        print("you rush back to the ship, and fly away. you're a bit sad you didn't fulfil the contract, but on the way out you snagged some salvage enough to get you two copper rocks. its enough for now...You continue cruising")
    elif choice2=="3":
        print("you catch the bot and confront it, you hold the blaster tight, the bot grabs you with incredible power and throws you out the airlock, your body freezes as you float in space forever...story OVER")
        continue_on2()
def continue_on2():
    answer = input("Story over, but there's much more you can do..Restart choosing different?\n > ")
    if answer.lower()=="yes":
        start_adventure()
    elif answer.lower()=="no":
        exit()
    else:
        exit()
def investigate_bot():
    print("you come face to face with this mechanical beast. he introduces himself\n")
    print("hello, i am...M.E.E.B.O or the Mechanical, exercise and Emergency.. Battle Operator. how may i assist you?\n") 
    print("the robot is your scavenge, how will you take the bot onboard? its unpredictible\n")
    print("1. Will you nicely convince the bot to come with you?\n")
    print("2. threaten it, maybe it will be convinced by threat\n")
    choice=input(" >")
    if choice=="1":
        print("you explain to the robot he is wanted for further work, work you dont know of but you tell the bot it is better then sitting in the abandoned space station, the bot agrees and follows you aboard")
        print("you set course to, Illo III, a small quiet border planet, to make the exchange\n")
        Illo_III()
    
    elif choice=="2":
        print("you threaten the bot, your blaster held tight and determined you explain, its termination or cooperation, deep down you know you wouldn't shoot the bot")
        print(" just hope it doesn't pick up your bluff..After a few moments the bots speaks.(yes i will accept) you set course to Illo III a small border planet to make the exchange, just hope the bot doesn't kill you before you break atmosphere\n")
        Illo_III2()
    else:
        print("invalid response")

def Illo_III():
    print("as you fly the robot asks you a few personal questions")
    print("will you tell him your story? Yes/no?\n")
    choice=input(" >").lower()
    if choice=="yes":
        print("you tell the Bot your stories of the fringe, the bot feels closer to you, Meebo feels.. Closer you can feel the shift in feelings as its analyzing you. You keep quiet and continue flying, after a while you break atmosphere and meet the contact and ready for exchange you can almost taste the alfredo.. But meebo seems conflicted")
        exchange()
    elif choice=="no":
        print("you tell the robot you're not interested in sharing... the bot stays quiet for the ride..After a while you break atmosphere and meet the contact you can almost taste the alfredo the bot is quiet.. you wonder if telling it off was the right choice..It doesn't matter you just want to see the next day no time for synthetic buddies..")
        exchange_2()
    else:
        print("you remain quiet and continue on route")
        exchange_2()

def Illo_III2():
    print("your a bit nervous the force was a bit unnecessary but you keep quiet and fly, the bot sits quietly in the co-pilot seat gazing at the distant stars. You make ready to break atmosphere and meet the contact, you can almost taste the alfredo and rocks to keep you going for another week\n")
    exchange_2()

def exchange_2():
    print("you finally come to see your contact waiting just outside the space port")
    print("the bot is quiet as you step out,  your quick to get the bot to move to the contact but it simply doesn't move")
    print("the contact is getting furious")
    print("1.Force the bot to move\n")
    print("2.Call the deal off and keep the rusted bot for yourself, who knows it might be useful but you don't have the best relationship to begin with..\n")
    choice=input(" >")
    if choice=="1":
        print("you kick the robot and even push but to no effort it doesn't move but simply turns around and attacks you, the contact tries to help you but also gets attacked by the hulking metal, You die a horrible fate at the hands of a rouge robot..\n")
        continue_on2()
    elif choice=="2":
        print("you call the deal off, you feel there is something special about the robot, maybe the worth is more then a few copper rocks and could be better in your hands, you say the bots worth more then some salvage its special")
        print("the contact gets angry and draws a blaster as he shoots Meebo stands in front tanking the shot meebo grabs him by the neck and holds him up\n")
        contact_death()
    
def contact_death():
    print("Meebo asks a simple question as the contact struggles to free himself from Meebos grip")
    print("shall i terminate..captain?\n")
    choice=input(" >").lower()
    if choice=="yes":
        print("meebo crushes the contact and before you know it your arrested by the F.F.F or the Free fringe Federation")
        print("they shock Meebo with an EMP making him motionless and slap you in handcuffs your sent to the F.F.F galactic penitentiary a huge Prison on a moving astroid through the void of space\n")
        Galactic_prison()
    elif choice=="no":
         print("you tell meebo to spare the man, Meebo drops him but the F.F.F guards see the comotion and rush to arrest you and Meebo")
         print("before you know it your arrested by the F.F.F or the Free fringe Federation")
         print("they shock Meebo with an EMP making him motionless and slap you in handcuffs your sent to the F.F.F galactic penitentiary a huge Prison on a moving astroid through the void of space\n")
         Galactic_prison()
    else:
        print("before you make up your mind Meebo crushes the contact")
        print("before you know it your arrested by the F.F.F or the Free fringe Federation")
        print("hey shock Meebo with an EMP making him motionless and slap you in handcuffs your sent to the F.F.F galactic penitentiary a huge Prison on a moving astroid through the void of space\n")
        Galactic_prison()





def exchange():
    print("you finally come see your contact waiting just outside the space port")
    print("meebo steps out as well facing the contact")
    print("the contact is happy to see the bot in good condition, right as your about to hand meebo over he says")
    print("im not ready to leave your side...Captain")
    print("the contact is mad and holds you hostage")
    print("meebo grabs the contact and smashes him into the ground and before you know it your being arrested by the F.F.F or the Free fringe Federation, they ask you if you own the bot, but before you respond meebo confirms your his owner")
    print("they shock Meebo with an EMP making him motionless and slap you in handcuffs your sent to the F.F.F galactic penitentiary a huge Prison on a moving astroid through the void of space\n")
    Galactic_prison()

def Galactic_prison(): 
    print("your taken to the Galactic penitentiary")
    print("your mugshots are taken you give a blank stare at the camera as you move on Meebo gives a thumbs up")
    print("you think what is with this robot..He got you in jail") 
    print("as your let in you and Meebo look around many different species of aliens, some big and small")
    print("the main area has seemingly endless rows of tables, on the tables are people arm wrestling gambling and eating")
    print("you look and it seems the prison cells go forever, a prison break would be catastrophic, but nobody has ever escaped and your hopes die\n")
    print("meebo looks at you and asks if your mad\n")
    choice=input(" > ").lower()
    if choice=="yes":
        print("meebo says in a almost sad tone,")
        print("sorry i let you down captain, i'll find a way to get us out")
        twins()
    elif choice=="no":
        print("meebo says in a hopeful tone")
        print("thanks for not being disappointed in me much..I'm trying to..Calibrate to you..")
        print("whatever this meant you say nothing but that doesn't mean your mind races with questions\n")
        twins()

def twins():
    print("as you and Meebo walk around you bump into two Polixtan twins aliens with a dark red skin color and a giant eye and a thing for fancy wear")
    print("you've seen there wanted posters before these two are up to no good")
    print("the Shorter one lexon, introduces herself")
    print("the taller one Nexon introduces himself also")
    print("they explain their last con job that got busted, they have been trapped here for a few months")
    print("they ask your story\n")
    print("1.open and passive\n")
    print("2.defensive and reserved\n")
    choice=input(" > ")
    if choice=="1":
        print("your open about your past. You explain the station and the contract and how it went south and give them your name")
        print("the twins appreciate your openness nexon says nice to meet you rex, we will come in contact soon but my sister and i must..be elsewhere now'")
        print("you don't think too much of it, at least your making friends right? meebo gives you a thumbs up in aproval\n")
        nice_twins()
    
    elif choice=="2":
        print(" your defensive about your past and how you ended up in prison with a weird robot")
        print("nexon says well i guess someone wants to act tough whatever...we don't need you' they walk away in the crowd of inmates\n")
        mean_twins()
    
    else:
        print("Lexon says what's wrong? cat got your tongue? we will come for you when we need you.. maybe you can share with us later' lexon turns around she walks away and Nexon follows")
        print("meebo looks at you confused as to why you chose to be silent..it doesn't matter anymore\n")
        nice_twins()

def nice_twins():
    print("after a few hours you and Meebo are in your cell during the quiet hours you wake up to a knock on the cell")
    print("'psst...Hey Rex!")
    print("lexon calls your name she stands out the cell holding a key card and nexon soon appears from the dark")
    print("'we are here to ask for your help..we know you want out as badly as we do' nexon explains")
    print("1.Accept the twins offer\n")
    print("2. Refuse the twins offer and make an attempt by yourself later\n")
    print("3. alert the guards and get the troublemakers in trouble makers introuble\n")
    choice=input(" > ")
    if choice=="1":
        print("you accept there help and Lexon lets you and meebo out the Cell.. now or never\n")
        escape()
    elif choice=="2.":
        print("you refuse there help and they look mad..They run and you hear alarms going off.. the next day you hear the twins successfully escaped, maybe you should've went")
        print("you and meebo stay in the Galactic penitentiary for..a long while\n")
        continue_on2()
    elif choice=="3":
        print("Lexon sees you about to alert the guards and she uses her Psychic ability to make you pass out")
        print("after a while meebo awakes you, later you figure out the twins didn't make it out alive.. and your still stuck in prison\n")
        continue_on2()
    else:
        print("lexon says")
        print("'your owners a bit speechless meebo, grab him and let go' ")
        print("meebo grabs you and you snap out of it, it's time to escape..Now or never\n")
        escape()
def mean_twins():
    print("as you lay in your cell you think you might have came a bit aggressive to the twins")
    print("soon you see lexon standing out the cell with a keycard")
    print("she explains you where a bit mean but she's willing to forgive if you accept to help")
    print("'please help my brother and I escape, we need your help'")
    print("nexon comes out from the shadows and they both await your descision\n")
    print("1.Accept the twins offer\n")
    print("2. Refuse the twins offer and make an attempt by yourself later\n")
    choice=input(">  ")
    if choice=="1":
        print("you accept there help and Lexon lets you and meebo out the Cell.. now or never\n")
        escape()
    elif choice=="2.":
        print("you refuse there help and they look mad..They run and you hear alarms going off.. the next day you hear the twins successfully escaped, maybe you should've went")
        print("you and meebo stay in the Galactic penitentiary for..a long while\n")
        continue_on2()
    else:
        print("lexon says")
        print("'your owners are a bit speechless meebo, grab him and let go' ")
        print("meebo grabs you and you snap out of it, it's time to escape..Now or never\n")
        escape()


def escape():
    print("you, Meebo and the Twins rush out")
    print("lexon says they keep inmates ships in the pound, that's where we are headed you fly us to a planet since we got you out the cell'")
    print("nexon explains they keep the ship access cards in the safe your going to have to find your ship key my sister and i will be waiting for you at the pound in a dumpster, good luck and id be stealthy if i where you..'..\n")
    print("1. Meebo suggests you arm yourself then get the key\n")
    print("2. Nexon suggested stealth is always an option\n")
    print("3. or you could go the rex way..But when has that ever worked..or maybe it can\n")
    choice=input(" >")
    if choice=="1":
        print("you decide to go to the armory to gear up..i mean who knows what you will face in the comming hours of your escape\n")
        armory_branch()

    elif choice=="2":
        print("you decide Nexon is probably right you decide sneaking and grabbing the key and slipping out will most likey give you the best chance\n")
        stealth_branch()
    elif choice=="3":
        print("you decide our way is the best way...whatever that means..\n")
        rex_branch()
    else:
        print("meebo grabs you")
        print("'no time for blanking out captain, my calculations say armory is the best choice'\n")
        armory_branch()
has_gun=False

def armory_branch():
    global has_gun
    print("you take a few sharp turns around cell blocks")
    print("you see all the other inmates looking out you wondering how you got out")
    print("meebo does a good job taking out a few guards on the way to the armory")
    print("you and meebo rush into the armory meebo with no struggle takes two guards with ease")
    print("you struggle with one guard as you both struggle for the nearby rifle\n")
    print("you grab it and point it at him\n")
    print("1. Spare the guard and knock him out\n")
    print("2. Waste the guard.. he could put the station on lockdown if he woke up early and prevent escape\n")
    choice=input(" > ")
    if choice=="1":
        print("you spare the guard he quickly tries to thank you but you knock him out.. you sling the rifle over your shoulder")
        print("meebo and you arm yourself with a few more toys of destruction and move on to retriev the key\n")
        has_gun=True
        key_grab()

    elif choice=="2":
        print("you shoot the guard and he slumps over..a wave of regret rushes your head, but theres no time for that")
        print("meebo and you arm yourself with a few more toys of destruction and move on to retrieve the key\n")
        has_gun=True
        key_grab()

def stealth_branch():
    global has_gun
    print("you take Nexons word for it and decide to get the key nice and sneaky")
    print("you suppress a few guards and so does meebo, few inmates take note of your escape")
    print("meebo tells you that there's a ventilation system that leads into the key room")
    print("so meebo helps you climb through the vents and meebo distracts the guards")
    print("you drop down and start searching for your ship key in the sea of access cards\n")
    print("after searching for a while there's only 3 places to look and the guards have almost apprehended meebo!\n")
    print("1. search box 90_L for your key\n")
    print("2. Search box 12_A for the key\n")
    print("3.search box 68_M for the key\n")
    print("4. assist Meebo first\n")
    choice=input(" > ")
    if choice=="1":
        print(" you search frantically for the key in box 90_L")
        print("no luck, a guard comes in and holds you gunpoint but meebo punches him into the wall.. a key slips out of a nearby box")
        print("your luck its your key! you and meebo rush to the pound to meet the twins\n")
        pound_escape()
    elif choice=="2":
        print(" you search frantically for the key in box 12_A")
        print("no luck, a guard comes in and holds you gunpoint but meebo punches him into the wall.. a key slips out of a nearby box")
        print("your luck its your key! you and meebo rush to the pound to meet the twins\n")
        pound_escape()
    elif choice=="3":
        print("you search frantically for the key in box 68_M")
        print("you find your key and run out but too your surprise meebo has taken care of the guards, he gives you a thumbs up")
        print("you and meebo rush to the pound to meet the twins\n")
        pound_escape()
    elif choice=="4":
        print("you decide to rush out of the key room and assist meebo")
        print("meebo handles two guards and you grab the gun off one guard and shoot him meebo handles the other two")
        print("meebo says'thanks for the assistance captain, this act is stored into my memory..' he gives you a thumbs up")
        print("you walk back in and grab the key and head to the pound to meet the twins for your escape")
        has_gun=True
        pound_escape()
         
def rex_branch():
    print("you look around thinking about forming a plan...Your egos big but is it worth more then your freedom and life?")
    print("you shake your head and decide to head to stick with meebos plan\n")
    armory_branch()

def key_grab():
    print("you rush to the armory rifle in hand you and meebo make quick work of the guards")
    print("you snag the key and head too the pound to escape with the twins\n")
    pound_escape()

def pound_escape():
    global has_gun
    print("you bang on the dumpster and the twins peak out and smile to your success of the key\n")
    if has_gun:
        print("nexon and lexon notice your guns they smile happily knowing the escape will be easier")
    else:print("nexon and lexon frown seeing you have no weapons, the escape will be more difficult")
    print("the crew rush towards rexs ship, but not before getting surrounded by guards, you drop your weapons")
    if has_gun:
        print("meebo looks at the guards then chucks a grenade that he found in the armory, the explosion makes your ears ring but when you look up the guards are taken care of")
        print("meebo, Nexon, and Lexon and yourself board the ship for a smooth escape")
        smooth_escape()
    else:
        print("the guards move in closer but thats when Nexon rushes in the ship")
        print("lexon follows and so does meebo and yourself")
        print("bullets fly past you some making it into the ship you start the ship and take off..")
        print("this is gonna be a really...Bumpy...Ride\n")
        rough_escape()

def rough_escape():
    print("as you soar through space the prison becoming just a little dot in the distance and slowly getting lost into the stars, a few ships fly up too you")
    print("its the prisons spaceforce\n")
    print("tell them to suck it")
    print("or surrender\n")
    choice=input("  >").lower()
    if choice=="suck it":
        print("the ships engage you and you engage them in a epic firefight, meebo gets on the cyclone")
        print("a round dome on the top of the ship and provides fire from behind")
        print("after a long battle you come out the victor, but at a cost")
        print("the ship is damaged and you need to make an emergency land at the union mining corp station..get the ship repaired with 2 silver rocks and 100 copper bits it should be enough..")
        print("but you cant go there yet because its too far and the closet place to land and recharge is fateth prime a wasteland ice planet")
        fateth_prime()
    elif choice=="surrender":
        print("as you surrender the twins are baffled, all that work for nothing...")
        continue_on2()
    else:
        print("fail to make a choice the guards board the ship..")
        continue_on2()
 
def smooth_escape():
    print("smooth sailing from here you all cheer")
    print("the twins suggest they want to land on Fateth prime, a ice cold planet with a small settlement")
    print("you accept there request and set course for the ice cold planet")
    print("after a few hours you land on the planet, Lexon and Nexon before stepping away decide")
    print("they have had a lot of fun with you and want to stay on your journey through the stars, a pirate and scav could use two con artists")
    fateth_prime()


def fateth_prime(): 
   print("you land on the ice planet")
   print("you decide to get out and explore")
   print("there is a nearby settlement and a old vantage bio tech lab\n")
   print("1. explore town\n")
   print("2. explore facility\n")
   choice=input(". >")
   
   if choice=="1":  
       print("you decide to explore the nearby town, the rest of the crew except meebo stay behind\n")
       town()
   elif choice=="2":
       print("you decide to explore the abandoned outpost\n")
       outpost()
   else:
       print("you didnt decide but meebo suggests you visit the outpost\n")
       outpost()

def outpost():
    print("you arrive at the outpost and explore for a bit")
    print("as you walk you see many fallen scientists")
    print("meebo says it was the work of a groggin")
    print("soon you hear something gurggle")
    print("meebo tosses you a found pistol, only a few bullets left, make them count")
    print("you see two doors, left or right?\n")
    choice=input("  >")
    if choice=="left":
        print("you walk left into a room, you find a piece of paper that says")
        print("'groggins weakness lies in the eye'")
        print("you run out to the sound of thrashing, Meebo is getting attacked by a groggin")
        print("the yeti like monster tosses and throws him, You pull out the gun he gave you and aim\n")
        groggin()
    elif choice=="right":
        print("you walk right, the room is empty, you run back out to the sound of thrashing")
        print("meebo is getting attacked!!")
        print("the yeti like monster tosses and throws him, You pull out the gun he gave you and aim\n")
        groggin()
    else:
        print("before you make a choice, you hear meebo getting thrown around")
        print("the groggin presents its self and atatcks you pull out your gun mebo gave you")
        groggin()
def groggin():
    print("as you pull out your gun you take aim\n")
    print("1. aim for its face\n")
    print("2.aim for its legs\n")
    print("3.shoot it in its eye\n")
    print("4. shoot it in its chest\n")
    choice=input("  >")
    if choice=="1":
        print("you take aim and fire, but it doesent seem to stop")
        print("it lifts you up and eats you")
        continue_on2()
    elif choice=="2":
        print("you take aim and fire, but it doesent seem to stop")
        print("it lifts you up and eats you")
        continue_on2()
    elif choice=="3":
        print("you take aim and fire at its eye")
        print("it stumbles back and falls down and crys in agony")
        print("a woman runs out from under a desk with a knife and stabs it")
        print("you and meebo look at eachother as the woman butchers the monster")
        print("after her brutal outrage she wipes the monsters blood from her face and extends for a handshake")
        dr_vega()
    elif choice=="4":
        print("you take aim and fire, but it doesent seem to stop")
        print("it lifts you up and eats you\n")
        continue_on2()
    else:
        print("you attempt to take aim but the monster picks you up and eats you!!")
        continue_on2()
def dr_vega():
    print("she extends for a handshake her hands soaked in warm blood")
    print("do you shake her hand and introduce yourself? Yes/No\n")
    choice=input("  >")
    if choice=="yes":
        print("you shake her hand and explain the past few days")
        print("she introduces herself as Dr.Vega a vantage bio tech botonist who came to study")
        print("but her outpost got attacked and all her friends died, shes pressumed KIA so it would hurt to take her aboard")
        print("she then asks if you will bring her aboard your crew?\n")
        vegachoice()
    elif choice=="no":
        print("you say no and she quickly puts her hand away awkardly..")
        print("after an awkard moment of silence she begs to come with you on your adventures")
        vegachoice()
    else:
        print("you look at her awkardly ")
        print("after an awkard moment of silence she begs to come with you on your adventures")
        vegachoice()
def vegachoice():
    print("will you allow vega aboard?? yes/no \n")
    choice=input("  >")
    if choice=="yes":
        print("she thanks your choice, meebo looks at you and displays a happy face")
        print("he then explains hes proud of you being very open to the people of the fringe")
        print("you take vega aboard where she meets the rest of the crew, Nexon walks up to you")
        print("and explains you need to go to union station for some ship repairs")
        print("since the ship is recharged you must head to union station to get repairs\n")
        union_station()
    elif choice=="no":
        print("vega looks at you sadly but then meebo, explains that she can come aboard")
        print("meebo then says, 'just because your harsh captain, doesent mean i should be' you decide not to fight meebos choice")
        print("you take vega aboard where she meets the rest of the crew, Nexon walks up to you")
        print("and explains you need to go to union station for some ship repairs")
        print("since the ship is recharged you must head to union station to get repairs\n")
        union_station()
def town():
    print("you and meebo walk into the town and buy a few things, a vendor")
    print("you buy from tells you about the nearby vantage outpost and how its been quiet there")
    print("for a few days, meebo wants to take a look and you agree and head to the outpost")
    outpost()

def union_station():
    print("you break atmosphere, after a few hours, of the ships humming from damage")
    print("you arrive at the mega corprate station, Union I")
    print("meebo, nexon, lexon, and vega accompany you, on the station\n")
    print("as much as i would love to finish this project, time has been a huge Limiter on this project!")
    print("congrats for making it atleast this far, the crew has so much more to do")
    print("i had plans for a casino heist and two more crew members lance, the mechanic and concordia the assasin")
    print("and if you didnt grab the gun in prison, you go to union station first, and meet lance first, then vega or other way arouund but i simply couldnt get it done wit the time given")
    print(" in the end this project was a lot bigger then i could get out")
    print("but thanks again for trying, i will deffinetly persue this space adventure more in different things")
    print("and i encourage you too make different choices aswell, the branching choices is what made this so time consuming so see how many you can get!")
    


start_adventure()







  
   


    

        
