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
        pass
    elif part == str("4"):
        part4()
        pass
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
    sprint("*You have wandered the Plane Of Souls for quite some time.")
    sprint("*At least, you think you have.")
    sprint("*It is a realm without time, without days nor nights.")
    sprint("*A realm without true form, a realm without Voice.")
    sprint("*And yet, you now remain still in this formless flow.")
    sprint("*And a voice, almost ethereal, reaches out to you.")
    sprint("The Voice: You are a wayward soul.")
    sprint("The Voice: One without path, without purpose.")
    sprint("The Voice: A blank slate, both in past and in future.")
    sprint("The Voice: However, even a blank slate can be written upon, sculpted anew.")
    sprint("The Voice: And such a process begins with knowing Yourself.")
    sprint("The Voice: Who are you?")
    try:
        name = str(input("(enter your name) "))
    except Exception as e:
        Scripts.errorhandle("C12")
    sprint("The Voice: " + name + "...")
    sprint("The Voice: A name most uncommon in this world, and yet not an unwelcome one.")
    sprint("The Voice: Although, I could swear I've heard it before...")
    sprint("The Voice: Ah, an unimportant detail.")
    sprint("The Voice: We shall now see how the world wishes to build you...")
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
    sprint("HP: " + str(maxhealth))
    sprint("STARTING CASH: " + str(money))
    sprint("STR: " + str(strength))
    sprint("DEF: " + str(defense))
    sprint("WIS: " + str(wisdom))
    sprint("SPD: " + str(speed))
    print("----------------------------")
    print("")
    answer = str(input("(Press enter to continue)"))
    print("")
    sprint("The Voice: Interesting... Most interesting...")
    sprint("The Voice: It seems the stars above may have a path planned for you after all, " + name + ".")
    sprint("The Voice: Until you reach the end of the path, try not to die.")
    print("")
    sprint("*as the voice says this, you feel a light shining in front of you.")
    sprint("*You shouldn't feel this. You haven't felt anything before.")
    sprint("*Not since you awoke on The Plane.")
    sprint("*And yet, you feel the instinct to go toward it.")
    answer = str(input("(Press enter to step towards this light)"))
    print("")
    sprint("*The light grows brighter as you step toward it. Every inch enveloping your form further in radiance.")
    sprint("*As you take one final step, you feel your vision go dark as you protect yourself from the beams of light.")
    sprint("*You have no idea what awaits you.")
    sprint("*For the World you knew was demolished long ago.")
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
    sprint("*When you finally come to, you slowly open your eyes.")
    sprint("*You did not have eyes before, you don't believe you ever have.")
    sprint("*Your eyes slowly adjust to the light, and you become aware of your surroundings.")
    sprint("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you.")
    sprint("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast.")
    sprint("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    sprint("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    sprint("*You speak softly to yourself, growing more used to this voice.")
    sprint(name + ": ...suppose I could look around.")
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
            sprint("*As you look to your left, you see a large pond of sorts.")
            sprint("*Many animals are drinking from the pond, and wild flora seem to be growing plentifully around it's crystal blue waters.")
            sprint("*You can't quite explain it, but somehow this puts your mind at ease.")
            print("----------")
            print("")
            sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            sprint("*To your right, you notice a sprawling forest of emerald green trees and bushes.")
            sprint("*You can't quite see into it, but based on the outside it must be full of life.")
            sprint("*As you admire it, you notice birds flying off from the trees, moving in a triangular formation.")
            sprint("*And yet... something about it makes you shudder. But why?")
            print("----------")
            print("")
            sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("3"):
            if inputcond1 == 0:
                print("")
                print("----------")
                sprint("*You turn your head up to the sky, squinting your eyes as the sun shines upon you.")
                sprint("*As the clouds slowly move to envelop the sun's light, your vision becomes clearer.")
                sprint("*This moment of quiet contemplation clears your mind, you feel more wise!")
                wisdom = int(wisdom) + int(1)
                inputcond1 = 1
                print("(Wisdom increased to " + wisdom + " !)")
                print("----------")
                print("")
                sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
                pass
            elif inputcond1 == 1:
                print("")
                print("----------")
                sprint("*You stare into the clouds oncemore, but it seems rather unproductive.")
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
            sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    sprint("*As you stand up, you notice something ahead of you, something you're shocked you didn't notice before.")
    sprint("*A small town, seemingly unpopulated and abandoned.")
    sprint("*Just looking at it sends a chill down your spine as you wonder what could've happened there to leave it entirely void of life.")
    sprint("*Just staring at it makes your skin feel cold and uncomfortable.")
    sprint("*Just as the discomfort begins to subside, you suddenly feel something.")
    print("")
    sprint("*A hand on your shoulder.")
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
    sprint("*As you register the hand that grabbed you, you can feel your heart racing uncontrollably.")
    sprint("*However, you need to swallow your fear and make a decision before it's too late...")
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
            sprint("*Despite it all, your resolve remains firm.")
            sprint("*Despite the fear in your heart, you turn your head to face whatever awaits you.")
            print("----------")
            print("")
            activeinput = 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            sprint("*You slowly open your mouth, you can feel your lips quivering as you speak.")
            sprint(name + ": Who or what are you?")
            sprint("*The creature stays silent for a moment, before you slowly hear their lips part.")
            sprint("???: Bit of an odd question, don't you think?")
            sprint("???: I'm human, as I suspect you are, no?")
            sprint("*You aren't quite sure if you are human, or what you are. But the fact the individual claims some similarities to you puts you at ease.")
            sprint("*As your guard lowers, you slowly turn your head to face them.")
            print("----------")
            print("")
            activeinput = 0
            pass
        elif answer == str("3"):
            result = Scripts.statcheck(6, wisdom)
            if result == "Pass":
                print("")
                print("----------")
                sprint("*You take a close look at the hand.")
                sprint("*While unfamiliar with this world, you can piece together that the hand looks slightly similar to your own.")
                sprint("*Perhaps this individual is the same species as you, and such potentially friendly.")
                sprint("*You decide you're likely safe to face them, and so you turn to do so.")
                print("----------")
                print("")
                activeinput = 0
                pass
            elif result == "Fail":
                print("")
                print("----------")
                sprint("*You try to look at the hand, but you can't quite make out what it is.")
                sprint("*Looking any further seems pointless.")
                print("----------")
                print("")
                pass
            pass
        else:
            sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    sprint("*As you turn your head to face them, you are greeted by an unassuming looking person.")
    sprint("*Upon quick examination, there seems to be no danger.")
    sprint("???: My, sorry to have spooked you, stranger!")
    sprint("*They're smiling, looking at you like a long lost friend.")
    sprint("*You feel a sort of familiarity you can't quite put your finger on...")
    sprint("???: What're you doing all the way out here, stranger?")
    sprint("???: Nobody's roamed these plains in quite some time.")
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
            sprint(name + ": I woke up here after a voice told me something about a path?")
            sprint("*Even you think you sound crazy saying this.")
            sprint("*The stranger looks at you with concern.")
            sprint("???: Did you hit your head or something, pal?")
            sprint("*They clearly don't believe you. Not unexpected.")
            sprint("???: Well, no matter!")
            sprint("*The individual's expression changes almost instantly.")
            activeinput = 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            sprint(name + ": I'm uh... a traveller from a far off land.")
            sprint("*You don't even sound convinced of yourself.")
            sprint("???: A traveller, huh? Well, that's wonderful!")
            sprint("*Somehow the stranger entirely buys the lie.")
            sprint("???: After all...")
            activeinput = 0
            pass
        elif answer == str("3"):
            print("")
            print("----------")
            sprint("*You remain silent, not answering their question.")
            sprint("*They look... almost saddened by this.")
            sprint("???: Not much of a talker, huh?")
            sprint("*Then suddenly, they perk up once more.")
            sprint("???: No matter! I'm not going to make you talk if you don't want to!")
            sprint("*They put their hand gently on your shoulder.")
            sprint("*It feels warm, comforting even.")
            maxhealth = int(maxhealth) + 10
            health = maxhealth
            sprint("(Max health increased to " + str(maxhealth) +" !)")
            sprint("???: I don't need to know anything about you to know...")
            activeinput = 0
            pass
        else:
            print("Invalid input, please try again")
            pass
        pass
    sprint("???: No matter what led you here...")
    sprint("*They somehow smile wider. It's almost eerie.")
    sprint("???: The house of Gen welcomes all!")
    sprint(name + ": ...house of Gen?")
    sprint("*They look at you confused before breaking into light laughter.")
    sprint("???: How silly of me, I never told you that was my name!")
    sprint("Gen: Name's Gen, nice to meet you...")
    sprint("Gen: What was your name again?")
    sprint("*Might as well tell them your name, no harm in that.")
    sprint(name + ": ..." + name)
    sprint("Gen: Well then, " + name + ", you look absolutely beat. How about you come stay at my place in Viper Village for a bit?")
    sprint(name + ": Viper Village?")
    sprint("Gen: Yeah, the town over there, I'm sure you saw it right?")
    sprint("*Gen points at the seemingly abandoned town at the edge of the field.")
    sprint("*It should be safe to stay there if you're with someone.")
    sprint("*Not that there seems to be another option.")
    sprint("*With a slightly hesitant nod, you get up, with help from Gen, and make your way to Viper Village.")
    answer = str(input("(Press enter to continue)"))
    makesave(4)
    pass
def part4():
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
    sprint("*Gen leads you into town, and it's just as barren as you thought.")
    sprint("*Homes are empty, windows are smashed, and there's not a single sign of life outside of you and Gen.")
    sprint("Gen: Quite a sight, huh?")
    sprint("Gen: Big village like this, all taken out and destroyed.")
    sprint("*You see Gen clench a fist. Whether it's in anger or in fear, you have no idea.")
    activeinput = 1
    while activeinput == 1:
        print("")
        print("1) Ask what happened")
        print("2) Ask how far until you get to Gen's house")
        answer = str(input("Make your choice"))
        if answer == str("1"):
            print("")
            print("----------")
            sprint("*You walk a little faster to catch up to Gen.")
            sprint(name + ": What the hell happened here, Gen?")
            sprint("*Gen looks shocked you asked.")
            sprint("Gen: I'd rather explain when we're inside, if that's alright...")
            sprint("*You choose not to force the issue, you'll ask them later.")
            sprint("*You simply nod and keep walking.")
            c1p4v1 = str("y")
            activeinput = 0
            pass
        if answer == str("2"):
            print("")
            print("----------")
            sprint("*You get impatient walking around this ghost town.")
            sprint(name + ": How long until we get to the House Of Gen you mentioned?")
            sprint("*Gen looks back at you, their smile faltering.")
            sprint("*You can't help but feel like a bit of an asshole.")
            sprint("Gen: Ah, we aren't much further, " + name + "!")
            sprint("*...")
            sprint("*You take the rest of the walk in silence.")
            sprint("*It's almost uncomfortable.")
            c1p4v1 = str("n")
            activeinput = 0
            pass
        else:
            sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    sprint("*As you walk with Gen, you start to hear rustling in a nearby bush.")
    sprint("*Gen holds their hand out, signalling you to stop.")
    sprint(name + ": What is it?")
    sprint("*Gen reaches for a small knife at their belt.")
    sprint("Gen: Either a monster or a thief.")
    sprint("*Not but a second later, a spider hops out of the bush.")
    sprint("*The creature is huge, about half as tall as you.")
    sprint("Gen: Shit! That's the largest I've seen here!")
    sprint("*Gen holds their knife up in a fighting stance.")
    sprint("Gen: " + name + ", get the hell out of here! You can't fight!")
    sprint("*Gen points ahead at a house with a blue roof, its vibrance contrasting the dark town.")
    sprint("Gen: That's my house! Go, now!")
    sprint("*Going to the house would be the safest option.")
    sprint("*But...")
    sprint("*Something within you is telling you that you can't leave.")
    sprint("*You can't just let Gen die, but you don't wish for death either.")
    activeinput = 1
    while activeinput == 1:
        print("")
        print("1) (STR) Fight")
        print("(STR needed: 6, your STR: " + str(strength) + ")")
        print("2) Run like hell")
        answer = str(input("Make your choice"))
        if answer == str("1"):
            result = Scripts.statcheck(6, strength)
            if result == str("Pass"):
                print("")
                print("----------")
                sprint("*You dash forward, clenching your fist tight.")
                sprint("*The spider is purely focused on Gen, so you're able to land a solid blow.")
                sprint("*As your fist slams into its head, it squeals out in pain as it bleeds.")
                sprint("*Before it has any time to react further, Gen slashes it on the body, drawing more blood and squeals.")
                sprint("*The spider quickly retreats, and you exit your fighting stance.")
                sprint("*You and Gen look at each other and nod. It's far past time to get into the house.")
                c1p4v2 = str("1")
                activeinput = 0
                pass
            elif result == str("Fail"):
                print("")
                print("----------")
                sprint("*You run forward to fight, but as you leap in to attack...")
                sprint("*The spider lunges forward, sinking it's large fangs into your arm.")
                health = int(health) - random.randint(10, 30)
                if health < 1:
                    sprint("*You can feel venom pouring out of its fangs.")
                    sprint("*No matter how much you squirm, you can't break free.")
                    sprint("*You feel your vision fading as your body succumbs to the venom.")
                    sprint("*You can barely make out Gen screaming out your name before you finally fade.")
                    Scripts.gameover()
                    pass
                elif health > 0:
                    sprint("*You groan out in pain and rip your arm away before any venom can dispense.")
                    sprint("*Your arm is open and bloody, but you'll live.")
                    sprint("Gen: " + name + "!!!")
                    sprint("*Suddenly, Gen leaps forward and plunges their knife deep into the creature's head.")
                    sprint("*The creature squeals out in pain before falling to the ground.")
                    sprint("*It isn't dead, but you can't afford to stay here.")
                    sprint("*Gen quickly puts their arm under yours and helps you the rest of the way to their house.")
                    c1p4v2 = str("2")
                    activeinput = 0
                    pass
                pass
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            sprint("*You hesitate, but ultimately agree.")
            sprint("*You quickly take off, leaving Gen to fight.")
            sprint("*You hope they can survive, but you can't worry about that too much.")
            c1p4v2 = str("3")
            activeinput = 0
            pass
        else:
            sprint("Invalid input, please try again.")
            pass
        pass
    if c1p4v2 == str("1"): # STR check pass
        pass
    elif c1p4v2 == str("2"): # STR check fail
        sprint("*You and Gen stumble through the door, both breathing heavily.")
        sprint("*Gen slowly lowers you onto a chair at the table in the center of the room.")
        sprint("Gen: You alright?")
        sprint(name + ": ...been better.")
        sprint("Gen: Fair, but at least we're alive...")
        sprint("*Gen sighs, sitting down across from you.")
    elif c1p4v2 == str("3"): # You ran
        sprint("*You slam your body into the door, opening it with a violent thud before closing it even more violently.")
        sprint("*You collapse against the door, panting rapidly.")
        sprint("*Was it really the right move to abandon Gen...?")
        sprint("*As you think about this, you hear a knock at the door")
        sprint("Gen: Hey! " + name + "! I got it!")
        sprint("*You breathe a sigh of relief. Gen survived after all.")
        sprint("*You open the door for them, and they walk in.")
        sprint("*Their knife is stained with spider blood, but they seem unharmed.")
        sprint("*You both sit down at the table in the center of the room")
        pass
    #Probably a good idea to smooth transfer into the table scene here
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
            pass
        elif varlist[1] == str("4"):
            varinit()
            part4()
            pass
elif toload == str("n"):
    part1()
