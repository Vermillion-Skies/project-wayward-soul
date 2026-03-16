import random #Imports the random library for use in stat calculations and rolls
import Scripts #Imports the custom script library
import os #Imports os for initial checks
def varinit(): #Initializes all variables to make sure they exist
    global chapter
    global part
    global name
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    global varlist
    try:
        chapter, part, name, health, maxhealth, money, strength, defense, wisdom, speed = varlist
    except Exception as e:
        Scripts.errorhandle("C10")
    pass
def makesave(x): #Function to prep for saving, as well as advancing to the next chapter
    if x == 900: #Change this to whatever the final part in the chapter is
        part = str("1")
        chapter = str("3")
        pass
    else:
        part = str(x)
        chapter = str("2")
        pass
    print("")
    answer = str(input("Would you like to save the game? (y/n) ")) #Asks user to confirm the save
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed)] #Sets varlist to all variables needed for a save
        Scripts.savegame(varlist) #Calls savegame with the varlist as an argument
        pass
    else:
        pass
    if chapter == str("2"): #Add as many conditionals in here as needed (one per part)
        if part == str("1"):
            part1()
            pass
        elif part == str("2"):
            part2()
            pass
        else:
            Scripts.errorhandle("C11")
            pass
        pass
    elif chapter == str("3"):
        Scripts.loadchapter(str("3"))
    pass
def part1():
    global chapter #sets many variables to be global, rather than locked to this function
    global part
    global name 
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    sprint("*After walking for about an hour, you and Gen arrive at the Serpentine Forest.")
    sprint("*The atmosphere around the forest is eerie, to say the least.")
    sprint("Gen: Say, " + name + ", what business do you have in the Serpentine Forest, anyway?")
    sprint("*You knew this question would arise at some point in time, and yet you still didn't prepare an answer.")
    activeinput = 1
    while activeinput == 1:
        print("1) Tell the truth about The Core")
        print("2) Lie and say something about birds")
        print("3) Stay silent")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            print("")
            print("----------")
            sprint("*It's better to be honest, rather than lie.")
            sprint(name + ": I'm here to cure the Core Of Roses and heal the forest.")
            sprint("*Gen looks shocked, more than ever before.")
            sprint("Gen: Wow, you never cease to surprise, huh?")
            sprint("Gen: Such a noble cause, how wonderful!")
            sprint("*Looks like that went well.")
            activeinput = 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            sprint(name + ": I heard there were some neat birds here, wanted to see for myself.")
            sprint("*Gen looks confused.")
            sprint("Gen: You're going to brave the forest and its horrors... for birds?")
            sprint(name + ": Yeah?")
            sprit("*Gen goes silent, then breaks out in laughter.")
            sprint("Gen: Wow, you really are a wild card aren't you?")
            sprint("Gen: Alright then, " + name + ", let's find your birds!")
            sprint("*Somehow, they bought it.")
            activeinput = 0
            pass
        elif answer == str("3"):
            print("")
            print("----------")
            sprint("*You keep your mouth shut, focused on the path ahead.")
            sprint("Gen: Hey wait, I didn't mean to upset you, " + name + ".")
            sprint("Gen: I'll avoid asking again, sorry.")
            sprint("*You feel like a bit of a jerk, but it's still best they don't know all of the nonsense with Wayland.")
            actieinput = 0
            pass
        else:
            sprint("Invalid input, try again.")
            pass
        pass
    sprint("*As you step closer to the forest, you feel a chill down your spine.")
    sprint("Gen: You okay, " + name + "?")
    sprint(name + ": Yeah, the forest just has an unsettling look to it.")
    sprint("Gen: It's worse inside. I will warn you, we'll probably have to do some fighting in there.")
    sprint("Gen: It's not too late to back out, you know.")
    sprint("*As much as you wish that were true, you don't have anywhere else to go but forward.")
    sprint(name + ": I'll be fine. Let's get going.")
    sprint("*Gen nods, and you both take another step toward the forest, when suddenly...")
    sprint("???: WHO DARES TO DISTURB MY FOREST??")
    sprint("*A deep voice speaks out within the trees.")
    sprint("???: THOSE WHO TRESSPASS ON THE GROUNDS OF THIS FOREST SHALL FOREVER BE TIED TO IT'S PATHS!")
    sprint("*As the voice says this, the ground starts shaking beneath you.")
    sprint("Gen: What the hell is going on?!")
    sprint("*The ground forms a pit, and both you and Gen fall into its depths.")
    makesave(2)
    pass
def part2():
    global chapter #sets many variables to be global, rather than locked to this function
    global part
    global name 
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    sprint("???: ...ey.")
    sprint("*...?")
    sprint("???: ...hey!")
    sprint("*A voice...? Am I dead again?")
    sprint("???: Hey sleepyhead, wake up!!")
    sprint("*You slowly open your eyes.")
    sprint("*You seem to be somewhere in the forest.")
    sprint("???: Finally! I thought you were a goner, you know!")
    sprint("*You look to your right to see a woman in a white dress, adorned with leaves. She has a bright red rose in her flowing, emerald green hair.")
    sprint(name + ": What happened...?")
    sprint("???: Oh shoot, did you hit your head or something?")
    sprint("*Your head does feel some slight pain.")
    sprint("???: Here, let me help you up.")
    sprint("*The woman puts her arm under yours, lifting you with ease.")
    sprint("???: I'm Pea, by the way.")
    sprint(name + ": ..." + name)
    sprint("Pea: Oh that's a relief, you at least remember your name.")
    sprint("*Pea walks you over to a small camp, where another woman sits waiting.")
    sprint("*She has similarly long hair, but rather than Pea's green, hers is a bright crimson red.")
    sprint("*She's wearing a sports bra and jean shorts with black leggings.")
    sprint("???: Oh, Pea! Welcome back honey!")
    sprint("*You see Pea smile as this woman speaks to her.")
    sprint("Pea: Hey Pepper. Found the source of that crashing noise.")
    sprint("*Seems that woman is named Pepper. And these two are... friends of some sort?")
    sprint("*Pea lays you down and walks over to Pepper.")
    sprint("Pea: Missed you, sweetie.")
    sprint("*Pea kisses Pepper on her cheek. Definitely not friends.")
    sprint("Pepper: You really are too kind, my little snap pea.")
    sprint("*As much as you enjoy seeing a loving couple, you do want to figure some stuff out.")
    activeinput = 1
    c2p2v1 = 0
    c2p2v2 = 0
    c2p2v3 = 0
    while activeinput == 1:
        print("1) Ask who they are")
        print("2) Ask where they are")
        print("3) Ask what happened")
        if c2p2v1 == 1:
            if c2p2v2 == 1:
                if c2p2v3 == 1:
                    print("4) Ask where Gen is.")
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        answer = str(input("Make your choice "))
        if answer == str("1"):
            pass
        elif answer == str("2"):
            pass
        elif answer == str("3"):
            pass
        elif answer == str("4"):
            if c2p2v1 == 1:
                if c2p2v2 == 1:
                    if c2p2v3 == 1:
                        sprint("*You ask them where Gen is.")
                        activeinput = 0
                        pass
                    else:
                        pass
                    pass
                else:
                    pass
                pass
            else:
                sprint("Invalid input, try again.")
        else:
            sprint("Invalid input, try again.")
            pass
        pass
    sprint("Pea: ...Gen?")
Scripts.screenclear() #the initial game logic that runs at the start
toload = Scripts.checkcache(0)
if toload ==str("y"):
    varlist = Scripts.loadgame() #Loads variables from a save file to a local varlist
    if varlist[0] == str("No"):
        part1()
    else:
        if varlist[1] == str("1"):
            varinit()
            part1()
            pass
        elif varlist[1] == str("2"):
            varinit()
            part2()
            pass
        pass
    pass
elif toload == str("n"):
    part1()
