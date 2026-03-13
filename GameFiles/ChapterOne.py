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
    part = str(x)
    chapter = 1
    print("")
    answer = str(input("Would you like to save the game? (y/n) ")) #Asks user to confirm the save
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed)] #Sets varlist to all variables needed for a save
        Scripts.savegame(varlist) #Calls savegame with the varlist as an argument
        pass
    else:
        pass
    if part ==str("1"):
        part1()
        pass
    elif part == str("2"):
        part2()
        pass
    elif part == str("3"):
        part3()
    else:
        Scripts.errorhandle("C11")
    pass
def part1(): #Function for the beginning character creation part of the game (referred to as part 1)
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
    Scripts.sprint("*You have wandered the Plane Of Souls for quite some time")
    Scripts.sprint("*At least, you think you have.")
    Scripts.sprint("*It is a realm without time, without days nor nights")
    Scripts.sprint("*A realm without true form, a realm without Voice")
    Scripts.sprint("*And yet, you now remain still in this formless flow")
    Scripts.sprint("*And a voice, almost ethereal, reaches out to you.")
    Scripts.sprint("???: You are a wayward soul.")
    Scripts.sprint("???: One without path, without purpose")
    Scripts.sprint("???: A blank slate, both in past and in future")
    Scripts.sprint("???: However, even a blank slate can be written upon, sculpted anew")
    Scripts.sprint("???: And such a process begins with knowing Yourself")
    Scripts.sprint("???: Who are you?")
    try:
        name = str(input("(enter your name) "))
    except Exception as e:
        Scripts.errorhandle("C12")
    Scripts.sprint("???: " + name + "...")
    Scripts.sprint("???: A name most uncommon in this world, and yet not an unwelcome one")
    Scripts.sprint("???: Although, I could swear I've heard it before...")
    Scripts.sprint("???: Ah, an unimportant detail")
    Scripts.sprint("???: We shall now see how the world wishes to build you...")
    answer = str(input("(Press enter to roll your stats. It will only be done once.)"))
    try:
        strength = random.randint(1,20)
        defense = random.randint(1,20)
        wisdom = random.randint(1,20)
        speed = random.randint(1,20)
        maxhealth = random.randint(50,145)
        money = random.randint(0,300)
        health = maxhealth
    except Exception as e:
        Scripts.errorhandle("C13")
    print("")
    print("---===STATS ROLLED===---")
    Scripts.sprint("HP: " + str(maxhealth))
    Scripts.sprint("STARTING CASH: " + str(money))
    Scripts.sprint("STR: " + str(strength))
    Scripts.sprint("DEF: " + str(defense))
    Scripts.sprint("WIS: " + str(wisdom))
    Scripts.sprint("SPD: " + str(speed))
    print("----------------------------")
    print("")
    answer = str(input("(Press enter to continue)"))
    print("")
    Scripts.sprint("???: Interesting... Most interesting...")
    Scripts.sprint("???: It seems the stars above may have a path planned for you after all, " + name + ".")
    Scripts.sprint("???: Until you reach the end of the path, try not to die")
    print("")
    Scripts.sprint("*as the voice says this, you feel a light shining in front of you")
    Scripts.sprint("*You shouldn't feel this. You haven't felt anything before.")
    Scripts.sprint("*Not since you awoke on The Plane")
    Scripts.sprint("*And yet, you feel the instinct to go toward it.")
    answer = str(input("(Press enter to step towards this light)"))
    print("")
    Scripts.sprint("*The light grows brighter as you step toward it. Every inch enveloping your form further in radiance.")
    Scripts.sprint("*As you take one final step, you feel your vision go dark as you protect yourself from the beams of light")
    Scripts.sprint("*You have no idea what awaits you.")
    Scripts.sprint("*For the World you knew was demolished long ago.")
    print("")
    answer = str(input("(Press enter to continue)"))
    makesave(2)
    part2()
    pass
def part2(): # Function for all logic of the second part of the first chapter of the game
    global name #sets many variables to be global, rather than locked to this function
    global maxhealth
    global health
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    Scripts.sprint("*When you finally come to, you slowly open your eyes")
    Scripts.sprint("*You did not have eyes before, you don't believe you ever have")
    Scripts.sprint("*Your eyes slowly adjust to the light, and you become aware of your surroundings")
    Scripts.sprint("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you")
    Scripts.sprint("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast")
    Scripts.sprint("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    Scripts.sprint("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    Scripts.sprint("*You speak softly to yourself, growing more used to this voice")
    Scripts.sprint(name + ": ...suppose I could look around")
    print("")
    activeinput = 1
    inputcond1 = 0
    while activeinput == 1:
        print("1) Look left")
        print("2) Look right")
        print("3) Look to the sky")
        print("4) Stop looking and stand up")
        answer = str(input("Enter selection: "))
        if answer == str("1"):
            print("")
            print("----------")
            Scripts.sprint("*As you look to your left, you see a large pond of sorts.")
            Scripts.sprint("*Many animals are drinking from the pond, and wild flora seem to be growing plentifully around it's crystal blue waters.")
            Scripts.sprint("*You can't quite explain it, but somehow this puts your mind at ease.")
            print("----------")
            print("")
            Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            Scripts.sprint("*To your right, you notice a sprawling forest of emerald green trees and bushes")
            Scripts.sprint("*You can't quite see into it, but based on the outside it must be full of life")
            Scripts.sprint("*As you admire it, you notice birds flying off from the trees, moving in a triangular formation")
            Scripts.sprint("*And yet... something about it makes you shudder. But why?")
            print("----------")
            print("")
            Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("3"):
            if inputcond1 == 0:
                print("")
                print("----------")
                Scripts.sprint("*You turn your head up to the sky, squinting your eyes as the sun shines upon you")
                Scripts.sprint("*As the clouds slowly move to envelop the sun's light, your vision becomes clearer")
                Scripts.sprint("*This moment of quiet contemplation clears your mind, you feel more wise!")
                wisdom = int(wisdom) + int(1)
                inputcond1 = 1
                print("(Wisdom increased to", wisdom, "!)")
                print("----------")
                print("")
                Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
                pass
            elif inputcond1 == 1:
                print("")
                print("----------")
                Scripts.sprint("*You stare into the clouds oncemore, but it seems rather unproductive")
                print("----------")
                print("")
                pass
            else:
                Scripts.errorhandle("C14")
            pass
        elif answer == str("4"):
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, please try again")
            pass
        pass
    print("")
    Scripts.sprint("*As you stand up, you notice something ahead of you, something you're shocked you didn't notice before")
    Scripts.sprint("*A small town, seemingly unpopulated and abandoned")
    Scripts.sprint("*Just looking at it sends a chill down your spine as you wonder what could've happened there to leave it entirely void of life")
    Scripts.sprint("*Just staring at it makes your skin feel cold and uncomfortable")
    Scripts.sprint("*Just as the discomfort begins to subside, you suddenly feel something")
    print("")
    Scripts.sprint("*A hand on your shoulder.")
    answer = str(input("(Press enter to continue)"))
    makesave(3) 
def part3(): #Function for all logic for part 3
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
    Scripts.sprint("*As you register the hand that grabbed you, you can feel your heart racing uncontrollably")
    Scripts.sprint("*However, you need to swallow your fear and make a decision before it's too late...")
    activeinput = 1
    while activeinput == 1: #Choice loop 3-1
        print("")
        print("1) Slowly turn your head")
        print("2) Ask the creature what it is without turning")
        print("3) (WIS) Analyze the hand")
        print("(required WIS: 6. Your WIS: " + str(wisdom) + ")")
        answer = str(input("Make your choice"))
        if answer == str("1"):
            print("")
            print("----------")
            Scripts.sprint("*Despite it all, your resolve remains firm")
            Scripts.sprint("*Despite the fear in your heart, you turn your head to face whatever awaits you.")
            print("----------")
            print("")
            activeinput = 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            Scripts.sprint("*You slowly open your mouth, you can feel your lips quivering as you speak")
            Scripts.sprint(name + ": Who or what are you?")
            Scripts.sprint("*The creature stays silent for a moment, before you slowly hear their lips part")
            Scripts.sprint("???: Bit of an odd question, don't you think?")
            Scripts.sprint("???: I'm human, as I suspect you are, no?")
            Scripts.sprint("*You aren't quite sure if you are human, or what you are. But the fact the individual claims some similarities to you puts you at ease")
            Scripts.sprint("*As your guard lowers, you slowly turn your head to face them")
            print("----------")
            print("")
            activeinput = 0
            pass
        elif answer == str("3"):
            result = Scripts.statcheck(6, wisdom)
            if result == "Pass":
                print("")
                print("----------")
                Scripts.sprint("*You take a close look at the hand")
                Scripts.sprint("*While unfamiliar with this world, you can piece together that the hand looks slightly similar to your own")
                Scripts.sprint("*Perhaps this individual is the same species as you, and such potentially friendly")
                Scripts.sprint("*You decide you're likely safe to face them, and so you turn to do so")
                print("----------")
                print("")
                activeinput = 0
                pass
            elif result == "Fail":
                print("")
                print("----------")
                Scripts.sprint("*You try to look at the hand, but you can't quite make out what it is")
                Scripts.sprint("*Looking any further seems pointless.")
                print("----------")
                print("")
                pass
    print("")
    Scripts.sprint("*As you turn your head to face them, you are greeted by an unassuming looking person")
    Scripts.sprint("*Upon quick examination, there seems to be no danger")
    Scripts.sprint("???: My, sorry to have spooked you, stranger!")
    Scripts.sprint("*They're smiling, looking at you like a long lost friend")
    Scripts.sprint("*You feel a sort of familiarity you can't quite put your finger on...")
    Scripts.sprint("???: What're you doing all the way out here, stranger?")
    Scripts.sprint("???: Nobody's roamed these plains in quite some time.")
    activeinput = 1
    while activeinput == 1: #Choice loop 3-2
        print("")
        print("1) Answer honestly")
        print("2) Lie")
        print("3) Stay silent")
        answer = str(input("(Make your choice)"))
        if answer == str("1"):
            print("")
            print("----------")
            Scripts.sprint(name + ": I woke up here after a voice told me something about a path?")
            Scripts.sprint("*Even you think you sound crazy saying this.")
            Scripts.sprint("*The stranger looks at you with concern")
            Scripts.sprint("???: Did you hit your head or something, pal?")
            Scripts.sprint("*They clearly don't believe you. Not unexpected.")
            Scripts.sprint("???: Well, no matter!")
            Scripts.sprint("*The individual's expression changes almost instantly.")
            activeinput = 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            Scripts.sprint(name + ": I'm uh... a traveller from a far off land")
            Scripts.sprint("*You don't even sound convinced of yourself")
            Scripts.sprint("???: A traveller, huh? Well, that's wonderful!")
            Scripts.sprint("*Somehow the stranger entirely buys the lie")
            Scripts.sprint("???: After all...")
            activeinput = 0
            pass
        elif answer == str("3"):
            print("")
            print("----------")
            Scripts.sprint("*You remain silent, not answering their question")
            Scripts.sprint("*They look... almost saddened by this")
            Scripts.sprint("???: Not much of a talker, huh?")
            Scripts.sprint("*Then suddenly, they perk up once more")
            Scripts.sprint("???: No matter! I'm not going to make you talk if you don't want to!")
            Scripts.sprint("*They put their hand gently on your shoulder")
            Scripts.sprint("*It feels warm, comforting even")
            maxhealth = int(maxhealth) + 10
            health = maxhealth
            Scripts.sprint("(Max health increased to" + str(maxhealth) +"!)")
            Scripts.sprint("???: I don't need to know anything about you to know...")
            activeinput = 0
            pass
        else:
            print("Invalid input, please try again")
            pass
        pass
    Scripts.sprint("???: No matter what led you here...")
    Scripts.sprint("*They somehow smile wider. It's almost eerie")
    Scripts.sprint("???: The home of Gen welcomes all!")
    Scripts.sprint(name + ": ...house of Gen?")
    Scripts.sprint("*They look at you confused before breaking into light laughter")
    Scripts.sprint("???: How silly of me, I never told you that was my name!")
    Scripts.sprint("Gen: Name's Gen, nice to meet you...")
    Scripts.sprint("Gen: What was your name again?")
    Scripts.sprint("*Might as well tell them your name, no harm in that")
    Scripts.sprint(name + ": ..." + name)
    Scripts.sprint("Gen: Well then, " + name + ", you look absolutely beat. How about you come stay at my place in Viper Village for a bit?")
    Scripts.sprint(name + ": Viper Village?")
    Scripts.sprint("Gen: Yeah, the town over there, I'm sure you saw it right?")
    Scripts.sprint("*Gen points at the seemingly abandoned town at the edge of the field")
    Scripts.sprint("*It should be safe to stay there if you're with someone")
    Scripts.sprint("*Not that there seems to be another option")
    Scripts.sprint("*With a slightly hesitant nod, you get up, with help from Gen, and make your way to Viper Village")
    answer = str(input("(Press enter to continue)"))
    makesave(4)
    pass
Scripts.screenclear() #the initial game logic that runs at the start
toload = Scripts.checkcache(0)
if toload ==str("y"):
    varlist = Scripts.loadgame() #Loads variables from a save file to a local varlist
    if varlist[0] == str("No"):
        part1()
    else:
        if varlist[1] == str("2"):
            varinit() #Initializes all needed variables
            part2()
            pass
        elif varlist[1] == str("3"):
            varinit()
            part3()
elif toload == str("n"):
    part1()
