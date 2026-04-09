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
    global gender
    global varlist
    try:
        chapter, part, name, health, maxhealth, money, strength, defense, wisdom, speed, gender = varlist
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
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed), str(gender)] #Sets varlist to all variables needed for a save
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
        elif part == str("3"):
            part3()
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
    global gender
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
    answer = str(input("Press enter to continue."))
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
    global gender
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
            if c2p2v1 == 1:
                Scripts.linebreak()
                sprint(name + ": So, who are you two?")
                sprint("*Pea and Pepper both look at you.")
                sprint("Pepper: We... Just explained it?")
                sprint("Pea: Are you sure you didn't hit your head, darling?")
                sprint("*You did already ask them this.")
                sprint("*You decide to ask something else")
                pass
            elif c2p2v1 == 0:
                Scripts.linebreak()
                sprint(name + ": So, who are you two?")
                sprint("Pea: Well, I'm Pea and this is Pepper.")
                sprint("*Pepper waves.")
                sprint("Pea: We live together in this forest, and have for a long time.")
                sprint("Pepper: And it's been really nice up until recently, when that weird voice showed up and threw you in here.")
                sprint("*Pepper stops.")
                sprint("Pepper: Not to say we aren't happy to have you, of course! We just don't know what that voice is.")
                sprint(name + ": And you two are friends? Roommates?")
                sprint("*Pea giggles lightheartedly.")
                sprint("Pea: Moreso lovers than friends.")
                sprint("Pepper: Yep! And I couldn't be happier with my darling snappea!")
                sprint("*You smile happily, they seem like they belong together.")
                c2p2v1 = 1
                pass
            pass
        elif answer == str("2"):
            if c2p2v2 == 1:
                Scripts.linebreak()
                sprint(name + ": So, where are we?")
                sprint("*Pea and Pepper both turn and stare at you.")
                sprint("Pepper: Pea, you didn't drop " + name + " did you?")
                sprint("Pea: I thought I didn't but I am now starting to get concerned...")
                sprint("*You did already ask this question.")
                sprint("*You decide to ask something else.")
                pass
            elif c2p2v2 == 0:
                Scripts.linebreak()
                sprint(name + ": So, where exactly are we?")
                sprint("Pea: Well, we're in the middle of the Serpentine Forest.")
                sprint("Pepper: Yeah, we've lived here for a couple of years now. Our cabin isn't too far from here, we just wanted to camp out here for a bit.")
                sprint("Pea: The view of the stars from this spot is phenomenal at night. My Pepper here loves staring into them.")
                sprint("*You see Pepper turn red and elbow Pea.")
                sprint("Pepper: You don't need to go around spreading my secrets to every single " + str(Scripts.gendercheck(gender, 0, 0, name)) + " you meet, you know.")
                sprint("Pea: Oh, but you're so cute when you're embarassed like this.")
                sprint("*You see Pepper turn an even brighter shade of red, you didn't think it was possible to get that red.")
                sprint("Pea: But yes, that's where we are, " + name + ".")
                sprint("*You feel relieved that the conversation ended there.")
                sprint("*Pepper almost looks like she's on fire.")
                c2p2v2 = 1
                pass
            pass
        elif answer == str("3"):
            if c2p2v3 == 1:
                sprint(name + ": So, what happened exactly?")
                sprint("*They both look at you with concern.")
                sprint("Pea: Are you sure you're feeling okay, " + name + "?")
                sprint("Pepper: You were probably too rough carrying " + str(Scripts.gendercheck(gender, 2, 0, name)) + " back, Pea.")
                sprint("Pea: I promise I treated " + str(Scripts.gendercheck(gender, 2, 0, name)) + " with the utmost care, Pepper.")
                sprint("*You did already ask this question.")
                sprint("*You should ask something else.")
                pass
            elif c2p2v3 == 0:
                sprint(name + ": So, what happened?")
                sprint("Pepper: Your guess is as good as ours. Me and Pea were just sitting here drinking tea when we heard a loud crash.")
                sprint("Pea: When I went over to investigate, that's when I found you laying in a crater, " + name + ".")
                sprint(name + ": Is that all you have?")
                sprint("Pepper: Yeah, sorry. We have just as much info as you do.")
                c2p2v3 = 1
                pass
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
    sprint(name + ": I was exploring this area with Gen when the voice came and took us.")
    sprint("Pea: Sorry, I didn't see them with you...")
    sprint("Pepper: Hold on, Pea. When you left to go get " + str(Scripts.gendercheck(gender, 2, 0, name)) + ", there was another crash.")
    sprint("*Pea looks at pepper, as do you.")
    sprint("Pea: Are you sure, love?")
    sprint("*Pepper nods.")
    sprint("Pepper: Yeah. It didn't sound too far from here, we can take " + name + " with us!")
    sprint("Pea: It would be best to make sure this Gen person is safe.")
    sprint("*Both women turn to face you.")
    sprint("Pepper: Come on, " + name + ", let's go get your friend!")
    answer = str(input("Press enter to continue."))
    makesave(3)
    pass
def part3():
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
    global gender
    Scripts.screenclear()
    sprint("Part 3 is currently under development.")
    sprint("Check back later once I'm done!")
    answer = str(input("Please close the game."))
    pass
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
        elif varlist[1] == str("3"):
            varinit()
            part3()
            pass
        pass
    pass
elif toload == str("n"):
    part1()
