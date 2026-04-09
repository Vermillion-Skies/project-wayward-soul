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
    if x == 6:
        part = str(1)
        chapter = str("2")
        pass
    else:
        part = str(x)
        chapter = str("1")
        pass
    print("")
    answer = str(input("Would you like to save the game? (y/n) ")) #Asks user to confirm the save
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed), str(gender)] #Sets varlist to all variables needed for a save
        Scripts.savegame(varlist) #Calls savegame with the varlist as an argument
        pass
    else:
        pass
    if chapter == str("1"):
        if part == str("1"):
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
        elif part == str("5"):
            part5()
            pass
        else:
            Scripts.errorhandle("C11")
            pass
        pass
    elif chapter == str("2"):
        Scripts.loadchapter(str("2"))
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
    global gender
    Scripts.screenclear()
    Scripts.sprint("*You have wandered the Plane Of Souls for quite some time.")
    Scripts.sprint("*At least, you think you have.")
    Scripts.sprint("*It is a realm without time, without days nor nights.")
    Scripts.sprint("*A realm without true form, a realm without Voice.")
    Scripts.sprint("*And yet, you now remain still in this formless flow.")
    Scripts.sprint("*And a voice, almost ethereal, reaches out to you.")
    Scripts.sprint("The Voice: You are a wayward soul.")
    Scripts.sprint("The Voice: One without path, without purpose.")
    Scripts.sprint("The Voice: A blank slate, both in past and in future.")
    Scripts.sprint("The Voice: However, even a blank slate can be written upon, sculpted anew.")
    Scripts.sprint("The Voice: And such a process begins with knowing Yourself.")
    Scripts.sprint("The Voice: Who are you?")
    try:
        name = str(input("(enter your name) "))
    except Exception as e:
        Scripts.errorhandle("C12")
    Scripts.sprint("The Voice: " + name + "...")
    Scripts.sprint("The Voice: A name most uncommon in this world, and yet not an unwelcome one.")
    Scripts.sprint("The Voice: And how do you wish to be formed?")
    activeinput = 1
    while activeinput == 1:
        print("0) Non-binary / other (they/them pronouns)")
        print("1) Male (he/him pronouns)")
        print("2) Female (she/her pronouns)")
        print("3) Ambiguous (no pronouns)")
        answer = str(input("(Enter your gender)"))
        if answer == str("0"):
            Scripts.sprint("The Voice: Ah, a soul with a form that defies gender.")
            Scripts.sprint("The Voice: Admittedly a refreshing change.")
            Scripts.sprint("The Voice: Very well then, " + name + ".")
            gender = str("0")
            activeinput = 0
            pass
        elif answer == str("1"):
            Scripts.sprint("The Voice: A soul with the body of a man, hm?")
            Scripts.sprint("The Voice: I expected as much from that name, I'm quite pleased to be corect.")
            Scripts.sprint("The Voice: Very well, sir " + name + ".")
            gender = str("1")
            activeinput = 0
            pass
        elif answer == str("2"):
            Scripts.sprint("The Voice: Ah, the body of a fair lady then?")
            Scripts.sprint("The Voice: Certainly matches the soul, as both will be equally beautiful.")
            Scripts.sprint("The Voice: Hope you enjoy your new form, miss " + name + ".")
            gender = str("2")
            activeinput = 0
            pass
        elif answer == str("3"):
            Scripts.sprint("The Voice: Oh, is that right?")
            Scripts.sprint("The Voice: You wish to simply be you, then?")
            Scripts.sprint("The Voice: How noble indeed, "+ name + ".")
            gender = str("3")
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, try again.")
            pass
        pass
    Scripts.sprint("The Voice: So, a " + str(Scripts.gendercheck(gender, 0, 0, name)) + " named " + name + ".")
    Scripts.sprint("The Voice: A new name upon this plane.")
    Scripts.sprint("The Voice: Although, I could swear I've heard it before...")
    Scripts.sprint("The Voice: Ah, an unimportant detail.")
    Scripts.sprint("The Voice: We shall now see how exactly the world wishes to build your form...")
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
    Scripts.sprint("The Voice: Interesting... Most interesting...")
    Scripts.sprint("The Voice: It seems the stars above may have a path planned for you after all, " + name + ".")
    Scripts.sprint("The Voice: Until you reach the end of the path, try not to die.")
    print("")
    Scripts.sprint("*as the voice says this, you feel a light shining in front of you.")
    Scripts.sprint("*You shouldn't feel this. You haven't felt anything before.")
    Scripts.sprint("*Not since you awoke on The Plane.")
    Scripts.sprint("*And yet, you feel the instinct to go toward it.")
    answer = str(input("(Press enter to step towards this light)"))
    print("")
    Scripts.sprint("*The light grows brighter as you step toward it. Every inch enveloping your form further in radiance.")
    Scripts.sprint("*As you take one final step, you feel your vision go dark as you protect yourself from the beams of light.")
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
    global gender
    Scripts.screenclear()
    Scripts.sprint("*When you finally come to, you slowly open your eyes.")
    Scripts.sprint("*You did not have eyes before, you don't believe you ever have.")
    Scripts.sprint("*Your eyes slowly adjust to the light, and you become aware of your surroundings.")
    Scripts.sprint("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you.")
    Scripts.sprint("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast.")
    Scripts.sprint("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    Scripts.sprint("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    Scripts.sprint("*You speak softly to yourself, growing more used to this voice.")
    Scripts.sprint(name + ": ...suppose I could look around.")
    print("")
    activeinput = 1
    inputcond1 = 0
    while activeinput == 1:
        print("1) Look left")
        print("2) Look right")
        print("3) Look to the sky")
        print("4) Stop looking and stand up")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            Scripts.linebreak()
            Scripts.sprint("*As you look to your left, you see a large pond of sorts.")
            Scripts.sprint("*Many animals are drinking from the pond, and wild flora seem to be growing plentifully around it's crystal blue waters.")
            Scripts.sprint("*You can't quite explain it, but somehow this puts your mind at ease.")
            print("")
            Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint("*To your right, you notice a sprawling forest of emerald green trees and bushes.")
            Scripts.sprint("*You can't quite see into it, but based on the outside it must be full of life.")
            Scripts.sprint("*As you admire it, you notice birds flying off from the trees, moving in a triangular formation.")
            Scripts.sprint("*And yet... something about it makes you shudder. But why?")
            print("")
            Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("3"):
            if inputcond1 == 0:
                Scripts.linebreak()
                Scripts.sprint("*You turn your head up to the sky, squinting your eyes as the sun shines upon you.")
                Scripts.sprint("*As the clouds slowly move to envelop the sun's light, your vision becomes clearer.")
                Scripts.sprint("*This moment of quiet contemplation clears your mind, you feel more wise!")
                wisdom = int(wisdom) + int(1)
                inputcond1 = 1
                print("(Wisdom increased to " + wisdom + " !)")
                print("")
                Scripts.sprint("*You turn your head back to the ground beneath you, contemplating your next choice.")
                pass
            elif inputcond1 == 1:
                linebreak()
                Scripts.sprint("*You stare into the clouds oncemore, but it seems rather unproductive.")
                print("")
                pass
            else:
                Scripts.errorhandle("C14")
            pass
        elif answer == str("4"):
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    Scripts.sprint("*As you stand up, you notice something ahead of you, something you're shocked you didn't notice before.")
    Scripts.sprint("*A small town, seemingly unpopulated and abandoned.")
    Scripts.sprint("*Just looking at it sends a chill down your spine as you wonder what could've happened there to leave it entirely void of life.")
    Scripts.sprint("*Just staring at it makes your skin feel cold and uncomfortable.")
    Scripts.sprint("*Just as the discomfort begins to subside, you suddenly feel something.")
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
    global gender
    Scripts.screenclear()
    Scripts.sprint("*As you register the hand that grabbed you, you can feel your heart racing uncontrollably.")
    Scripts.sprint("*However, you need to swallow your fear and make a decision before it's too late...")
    activeinput = 1
    while activeinput == 1: #Choice loop 3-1
        print("")
        print("1) Slowly turn your head")
        print("2) Ask the creature what it is without turning")
        print("3) (WIS) Analyze the hand")
        print("(required WIS: 6. Your WIS: " + str(wisdom) + ")")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            Scripts.linebreak()
            Scripts.sprint("*Despite it all, your resolve remains firm.")
            Scripts.sprint("*Despite the fear in your heart, you turn your head to face whatever awaits you.")
            print("")
            activeinput = 0
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint("*You slowly open your mouth, you can feel your lips quivering as you speak.")
            Scripts.sprint(name + ": Who or what are you?")
            Scripts.sprint("*The creature stays silent for a moment, before you slowly hear their lips part.")
            Scripts.sprint("???: Bit of an odd question, don't you think?")
            Scripts.sprint("???: I'm human, as I suspect you are, no?")
            Scripts.sprint("*You aren't quite sure if you are human, or what you are. But the fact the individual claims some similarities to you puts you at ease.")
            Scripts.sprint("*As your guard lowers, you slowly turn your head to face them.")
            print("")
            activeinput = 0
            pass
        elif answer == str("3"):
            result = Scripts.statcheck(6, wisdom)
            if result == "Pass":
                Scripts.linebreak()
                Scripts.sprint("*You take a close look at the hand.")
                Scripts.sprint("*While unfamiliar with this world, you can piece together that the hand looks slightly similar to your own.")
                Scripts.sprint("*Perhaps this individual is the same species as you, and such potentially friendly.")
                Scripts.sprint("*You decide you're likely safe to face them, and so you turn to do so.")
                print("")
                activeinput = 0
                pass
            elif result == "Fail":
                Scripts.linebreak()
                Scripts.sprint("*You try to look at the hand, but you can't quite make out what it is.")
                Scripts.sprint("*Looking any further seems pointless.")
                print("")
                pass
            pass
        else:
            Scripts.sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    Scripts.sprint("*As you turn your head to face them, you are greeted by an unassuming looking person.")
    Scripts.sprint("*Upon quick examination, there seems to be no danger.")
    Scripts.sprint("???: My, sorry to have spooked you, stranger!")
    Scripts.sprint("*They're smiling, looking at you like a long lost friend.")
    Scripts.sprint("*You feel a sort of familiarity you can't quite put your finger on...")
    Scripts.sprint("???: What're you doing all the way out here, stranger?")
    Scripts.sprint("???: Nobody's roamed these plains in quite some time.")
    activeinput = 1
    while activeinput == 1: #Choice loop 3-2
        print("")
        print("1) Answer honestly")
        print("2) Lie")
        print("3) Stay silent")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            Scripts.linebreak()
            Scripts.sprint(name + ": I woke up here after a voice told me something about a path?")
            Scripts.sprint("*Even you think you sound crazy saying this.")
            Scripts.sprint("*The stranger looks at you with concern.")
            Scripts.sprint("???: Did you hit your head or something, pal?")
            Scripts.sprint("*They clearly don't believe you. Not unexpected.")
            Scripts.sprint("???: Well, no matter!")
            Scripts.sprint("*The individual's expression changes almost instantly.")
            activeinput = 0
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint(name + ": I'm uh... a traveller from a far off land.")
            Scripts.sprint("*You don't even sound convinced of yourself.")
            Scripts.sprint("???: A traveller, huh? Well, that's wonderful!")
            Scripts.sprint("*Somehow the stranger entirely buys the lie.")
            Scripts.sprint("???: After all...")
            activeinput = 0
            pass
        elif answer == str("3"):
            Scripts.linebreak()
            Scripts.sprint("*You remain silent, not answering their question.")
            Scripts.sprint("*They look... almost saddened by this.")
            Scripts.sprint("???: Not much of a talker, huh?")
            Scripts.sprint("*Then suddenly, they perk up once more.")
            Scripts.sprint("???: No matter! I'm not going to make you talk if you don't want to!")
            Scripts.sprint("*They put their hand gently on your shoulder.")
            Scripts.sprint("*It feels warm, comforting even.")
            maxhealth = int(maxhealth) + 10
            health = maxhealth
            Scripts.sprint("(Max health increased to " + str(maxhealth) +" !)")
            Scripts.sprint("???: I don't need to know anything about you to know...")
            activeinput = 0
            pass
        else:
            print("Invalid input, please try again")
            pass
        pass
    Scripts.sprint("???: No matter what led you here...")
    Scripts.sprint("*They somehow smile wider. It's almost eerie.")
    Scripts.sprint("???: The house of Gen welcomes all!")
    Scripts.sprint(name + ": ...house of Gen?")
    Scripts.sprint("*They look at you confused before breaking into light laughter.")
    Scripts.sprint("???: How silly of me, I never told you that was my name!")
    Scripts.sprint("Gen: Name's Gen, nice to meet you...")
    Scripts.sprint("Gen: What was your name again?")
    Scripts.sprint("*Might as well tell them your name, no harm in that.")
    Scripts.sprint(name + ": ..." + name)
    Scripts.sprint("Gen: Well then, " + name + ", you look absolutely beat. How about you come stay at my place in Viper Village for a bit?")
    Scripts.sprint(name + ": Viper Village?")
    Scripts.sprint("Gen: Yeah, the town over there, I'm sure you saw it right?")
    Scripts.sprint("*Gen points at the seemingly abandoned town at the edge of the field.")
    Scripts.sprint("*It should be safe to stay there if you're with someone.")
    Scripts.sprint("*Not that there seems to be another option.")
    Scripts.sprint("*With a slightly hesitant nod, you get up, with help from Gen, and make your way to Viper Village.")
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
    global gender
    Scripts.screenclear()
    Scripts.sprint("*Gen leads you into town, and it's just as barren as you thought.")
    Scripts.sprint("*Homes are empty, windows are smashed, and there's not a single sign of life outside of you and Gen.")
    Scripts.sprint("Gen: Quite a sight, huh?")
    Scripts.sprint("Gen: Big village like this, all taken out and destroyed.")
    Scripts.sprint("*You see Gen clench a fist. Whether it's in anger or in fear, you have no idea.")
    activeinput = 1
    while activeinput == 1:
        print("")
        print("1) Ask what happened")
        print("2) Ask how far until you get to Gen's house")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            Scripts.linebreak()
            Scripts.sprint("*You walk a little faster to catch up to Gen.")
            Scripts.sprint(name + ": What the hell happened here, Gen?")
            Scripts.sprint("*Gen looks shocked you asked.")
            Scripts.sprint("Gen: I'd rather explain when we're inside, if that's alright...")
            Scripts.sprint("*You choose not to force the issue, you'll ask them later.")
            Scripts.sprint("*You simply nod and keep walking.")
            c1p4v1 = str("y")
            activeinput = 0
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint("*You get impatient walking around this ghost town.")
            Scripts.sprint(name + ": How long until we get to the House Of Gen you mentioned?")
            Scripts.sprint("*Gen looks back at you, their smile faltering.")
            Scripts.sprint("*You can't help but feel like a bit of an asshole.")
            Scripts.sprint("Gen: Ah, we aren't much further, " + name + "!")
            Scripts.sprint("*...")
            Scripts.sprint("*You take the rest of the walk in silence.")
            Scripts.sprint("*It's almost uncomfortable.")
            c1p4v1 = str("n")
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, please try again.")
            pass
        pass
    print("")
    Scripts.sprint("*As you walk with Gen, you start to hear rustling in a nearby bush.")
    Scripts.sprint("*Gen holds their hand out, signalling you to stop.")
    Scripts.sprint(name + ": What is it?")
    Scripts.sprint("*Gen reaches for a small knife at their belt.")
    Scripts.sprint("Gen: Either a monster or a thief.")
    Scripts.sprint("*Not but a second later, a spider hops out of the bush.")
    Scripts.sprint("*The creature is huge, about half as tall as you.")
    Scripts.sprint("Gen: Shit! That's the largest I've seen here!")
    Scripts.sprint("*Gen holds their knife up in a fighting stance.")
    Scripts.sprint("Gen: " + name + ", get the hell out of here! You can't fight!")
    Scripts.sprint("*Gen points ahead at a house with a blue roof, its vibrance contrasting the dark town.")
    Scripts.sprint("Gen: That's my house! Go, now!")
    Scripts.sprint("*Going to the house would be the safest option.")
    Scripts.sprint("*But...")
    Scripts.sprint("*Something within you is telling you that you can't leave.")
    Scripts.sprint("*You can't just let Gen die, but you don't wish for death either.")
    activeinput = 1
    while activeinput == 1:
        print("")
        print("1) (STR) Fight")
        print("(STR needed: 6, your STR: " + str(strength) + ")")
        print("2) Run like hell")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            result = Scripts.statcheck(6, strength)
            if result == str("Pass"):
                Scripts.linebreak()
                Scripts.sprint("*You dash forward, clenching your fist tight.")
                Scripts.sprint("*The spider is purely focused on Gen, so you're able to land a solid blow.")
                Scripts.sprint("*As your fist slams into its head, it squeals out in pain as it bleeds.")
                Scripts.sprint("*Before it has any time to react further, Gen slashes it on the body, drawing more blood and squeals.")
                Scripts.sprint("*The spider quickly retreats, and you exit your fighting stance.")
                Scripts.sprint("*You and Gen look at each other and nod. It's far past time to get into the house.")
                c1p4v2 = str("1")
                activeinput = 0
                pass
            elif result == str("Fail"):
                Scripts.linebreak()
                Scripts.sprint("*You run forward to fight, but as you leap in to attack...")
                Scripts.sprint("*The spider lunges forward, sinking it's large fangs into your arm.")
                health = int(health) - random.randint(10, 30)
                if health < 1:
                    Scripts.sprint("*You can feel venom pouring out of its fangs.")
                    Scripts.sprint("*No matter how much you squirm, you can't break free.")
                    Scripts.sprint("*You feel your vision fading as your body succumbs to the venom.")
                    Scripts.sprint("*You can barely make out Gen screaming out your name before you finally fade.")
                    Scripts.gameover()
                    pass
                elif health > 0:
                    Scripts.sprint("*You groan out in pain and rip your arm away before any venom can dispense.")
                    Scripts.sprint("*Your arm is open and bloody, but you'll live.")
                    Scripts.sprint("Gen: " + name + "!!!")
                    Scripts.sprint("*Suddenly, Gen leaps forward and plunges their knife deep into the creature's head.")
                    Scripts.sprint("*The creature squeals out in pain before falling to the ground.")
                    Scripts.sprint("*It isn't dead, but you can't afford to stay here.")
                    Scripts.sprint("*Gen quickly puts their arm under yours and helps you the rest of the way to their house.")
                    c1p4v2 = str("2")
                    activeinput = 0
                    pass
                pass
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint("*You hesitate, but ultimately agree.")
            Scripts.sprint("*You quickly take off, leaving Gen to fight.")
            Scripts.sprint("*You hope they can survive, but you can't worry about that too much.")
            c1p4v2 = str("3")
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, please try again.")
            pass
        pass
    if c1p4v2 == str("1"): # STR check pass
        Scripts.sprint("*You slowly open the door to Gen's house and step inside.")
        Scripts.sprint("*Gen gestures to a table in the middle of the room, inviting you to sit with them.")
        pass
    elif c1p4v2 == str("2"): # STR check fail
        Scripts.sprint("*You and Gen stumble through the door, both breathing heavily.")
        Scripts.sprint("*Gen slowly lowers you onto a chair at the table in the center of the room.")
        Scripts.sprint("Gen: You alright?")
        Scripts.sprint(name + ": ...been better.")
        Scripts.sprint("Gen: Fair, but at least we're alive...")
        Scripts.sprint("*Gen sighs, sitting down across from you.")
        Scripts.sprint("Gen: Sorry about that... mess.")
        Scripts.sprint("*You get the feeling this happens a lot here.")
        pass
    elif c1p4v2 == str("3"): # You ran
        Scripts.sprint("*You slam your body into the door, opening it with a violent thud before closing it even more violently.")
        Scripts.sprint("*You collapse against the door, panting rapidly.")
        Scripts.sprint("*Was it really the right move to abandon Gen...?")
        Scripts.sprint("*As you think about this, you hear a knock at the door.")
        Scripts.sprint("Gen: Hey! " + name + "! I got it!")
        Scripts.sprint("*You breathe a sigh of relief. Gen survived after all.")
        Scripts.sprint("*You open the door for them, and they walk in.")
        Scripts.sprint("*Their knife is stained with spider blood, but they seem unharmed.")
        Scripts.sprint("*You both sit down at the table in the center of the room.")
        pass
    Scripts.sprint("*You feel now is as good a time as any to talk to them.")
    if c1p4v1 == str("y"):
        Scripts.sprint("*You remember that they offered to talk about the story behind this place.")
        pass
    c1p4v3 = str("n")
    #Probably a good idea to smooth transfer into the table scene here
    #Start it with dialog choices "What was that", something asking about Gen's home, and then a check for c1p4v1 where they explain what happened to this town
    activeinput = 1
    while activeinput == 1:
        print("1) Ask what that creature was")
        print("2) Look around Gen's home")
        if c1p4v1 == str("y"):
            print("3) Ask about what happened to this town")
            pass
        print("4) Allow the silence to stay")
        answer = str(input("Make your choice "))
        if answer == str("1"):
            Scripts.linebreak()
            Scripts.sprint(name + ": So just what the hell was that thing?")
            Scripts.sprint("Gen: Oh, that was a crawler.")
            Scripts.sprint(name + ": Crawler...?")
            Scripts.sprint("Gen: Yeah, crawlers. Ten legged spider freaks that have enough venom to kill you if you look at them wrong.")
            Scripts.sprint("Gen: They're easy enough to kill, but still dangerous and honestly just annoying.")
            Scripts.sprint(name + ": I see...")
            Scripts.sprint("*You count yourself lucky to be alive.")
            pass
        elif answer == str("2"):
            Scripts.linebreak()
            Scripts.sprint("*You look around Gen's house.")
            Scripts.sprint("*It's fairly basic. Small kitchen, a singular window, and...")
            Scripts.sprint("*Two beds...?")
            Scripts.sprint("*Why would they need multiple beds...?")
            activeinput2 = 1
            while activeinput2 == 1:
                print("1) Ask about it")
                print("2) Leave it be")
                answer2 = str(input("Make your choice "))
                if answer2 == str("1"):
                    Scripts.linebreak()
                    Scripts.sprint(name + ": Hey, Gen?")
                    Scripts.sprint("*Gen turns to face you.")
                    Scripts.sprint(name + ": The beds... You used to live here with someone else, didn't you?")
                    Scripts.sprint("*You see Gen freeze up a little.")
                    Scripts.sprint("Gen: It's... a long story...")
                    Scripts.sprint("*It seems Gen won't answer readily.")
                    Scripts.sprint("*Best not to push it. Not your business anyway.")
                    activeinput2 = 0
                    pass
                elif answer2 == str("2"):
                    Scripts.linebreak()
                    Scripts.sprint("*You decide to leave it be, probably a touchy subject")
                    activeinput2 = 0
                    pass
                else:
                    Scripts.sprint("Invalid input, try again.")
                    pass
                pass
            pass
        elif answer == str("3"):
            if c1p4v1 == str("y"):
                Scripts.linebreak()
                Scripts.sprint(name + ": So Gen... What the hell happened in this town?")
                Scripts.sprint("Gen: I figured you'd ask at some point.")
                Scripts.sprint("*Gen reaches down and grabs two drinks, tossing you one.")
                Scripts.sprint("*You open the lid and take a sip.")
                Scripts.sprint("*It tastes sweet, and very nice.")
                Scripts.sprint("*Gen takes a deep sip before continuing.")
                Scripts.sprint("Gen: It was a day like any other... Kids playing, the miners were returning from the caves, the hunters returned with food...")
                Scripts.sprint("Gen: I was sitting on the porch enjoying a drink with...")
                Scripts.sprint(name + ": With...?")
                Scripts.sprint("*Gen takes a deep, almost pained sigh.")
                Scripts.sprint("Gen: Matilda. My... My wife.")
                Scripts.sprint("*You take a breath. This is going to be a painful story.")
                Scripts.sprint("Gen: We were sitting there, watching our kids play in the yard, when we heard screams.")
                Scripts.sprint("Gen: I told Matilda to wait on the porch while I went to the source, but by the time I went inside to grab my knife... it was too late.")
                Scripts.sprint("Gen: When I came back out, the whole village was in flames. And the smell of blood and ash was intense.")
                Scripts.sprint("Gen: My wife laid dead on the porch, my kids charred and collapsed in the yard.")
                Scripts.sprint("Gen: And at the center of it all... The Black Flame.")
                Scripts.sprint(name + ": Black Flame?")
                Scripts.sprint("Gen: A band of criminals who use magic to steal from villages and leave them dead and demolished.")
                Scripts.sprint("Gen: We never stood a chance...")
                Scripts.sprint("Gen: I ended up passing out from the shock of it all, and when I came to they were gone.")
                Scripts.sprint("Gen: I swear, one day I will find them. And I will have no mercy until their blood stains my blade.")
                Scripts.sprint(name + ": I'm sorry, I never knew...")
                Scripts.sprint("*Somehow, Gen smiles once more.")
                Scripts.sprint("Gen: It's quite alright, " + name + ". You couldn't have known, could you?")
                Scripts.sprint("*Gen takes a sip of their drink, returning the room to silence.")
                c1p4v3 = str("y")
                pass
            else:
                Scripts.sprint("Invalid input, try again.")
                pass
            pass
        elif answer == str("4"):
            Scripts.linebreak()
            Scripts.sprint("*You decide to just let the silence remain, until Gen breaks it.")
            activeinput = 0
            pass
        else:
            Scripts.sprint("Invalid input, try again.")
            pass
        pass
    Scripts.sprint("Gen: Well, it's getting late. What say we get some rest, huh " + name + "?")
    Scripts.sprint("*You can't help but agree. Your body is exhausted.")
    Scripts.sprint(name + ": ...yeah.")
    Scripts.sprint("*Gen directs you to a second bed, not far from theirs.")
    if c1p4v3 == str("y"):
        Scripts.sprint("*You get the feeling this belonged to their wife, Matilda.")
        pass
    elif c1p4v3 == str("n"):
        Scripts.sprint("*You wonder why they have two beds, but it's probably too late to ask that now.")
        pass
    Scripts.sprint("*As you lay down, your eyes feel heavy almost immediately...")
    Scripts.sprint("*You slowly drift off into a gentle slumber...")
    makesave(5)
    pass
def part5():
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
    Scripts.sprint("The Voice: My, my. What a day you've had, huh " + name + "?")
    Scripts.sprint("*You bolt up, awoken by a familiar voice.")
    Scripts.sprint("*You are most definitely not in Gen's house anymore.")
    Scripts.sprint("*You float alone on a flat plane of crystal, in a sky of bright blues and greens.")
    Scripts.sprint("*Just how did you get here?")
    Scripts.sprint("The Voice: Ah, awake at last.")
    Scripts.sprint("*That voice again... From the Plane Of Souls.")
    Scripts.sprint("The Voice: I'm sure you have many questions, don't you Chosen One?")
    Scripts.sprint(name + ": Chosen one?")
    Scripts.sprint("The Voice: The one chosen by the light to dispel the darkness, handed the power of the Divine Ones.")
    Scripts.sprint(name + ": Hold on, hold on. Chosen One? Divine Ones? You're dropping a lot on me for a stranger.")
    Scripts.sprint(name + ": Hell, you told me everything up until now without giving me your name!")
    Scripts.sprint("The Voice: Ah, I suppose I have. How silly of me.")
    Scripts.sprint("The Voice: You may call me... Wayland.")
    Scripts.sprint("Wayland: Now, " + name + ", I'm sure you noticed what happened to parts of this world, no?")
    Scripts.sprint("Wayland: They're desolate, ravished, demolished. A sorry sight after how hard I worked.")
    Scripts.sprint("Wayland: It is your job to restore order to this land, one step at a time.")
    Scripts.sprint(name + ": Okay, how am I supposed to do that?")
    Scripts.sprint("Wayland: For starters, you need to restore the Core Of Roses within the Serpentine Forest.")
    Scripts.sprint("Wayland: Gen should be able to show you the way there.")
    Scripts.sprint(name + ": Wait, Gen is in on this?")
    Scripts.sprint("Wayland: Oh no, they just know the area.")
    Scripts.sprint("Wayland: With that, I send you on your way, " + name + ".")
    Scripts.sprint("Wayland: Best of luck to you, and once again try to stay alive.")
    Scripts.sprint(name + ": Wait-!")
    Scripts.sprint("*Before you can say anything, a blinding light overwhelms your vision.")
    Scripts.sprint("*You're now back in Gen's house.")
    Scripts.sprint(name + ": Dammit!")
    Scripts.sprint("Gen: " + name + "...?")
    Scripts.sprint(name + ": Sorry, bad dream.")
    Scripts.sprint("*You get up out of bed and grab your belongings, of which there's not much.")
    Scripts.sprint("Gen: " + name + " where are you going?")
    Scripts.sprint(name + ": The Serpentine Forest. I have something to do there.")
    Scripts.sprint("Gen: Oh hell no, not alone you don't.")
    Scripts.sprint("*Gen proceeds to also get out of bed, grabbing their stuff.")
    Scripts.sprint("Gen: You think you can just up and leave without me? I ain't gonna let you die alone, you know.")
    Scripts.sprint("*Despite the seriousness of what they said, they're still smiling.")
    Scripts.sprint("*They would be good help in the journey.")
    Scripts.sprint(name + ": I suppose I wouldn't mind the company.")
    Scripts.sprint("Gen: Hell yeah! Come on then, I'll lead the way!")
    Scripts.sprint("*As you follow Gen out of the house, you get the feeling this will be quite the interesting journey.")
    Scripts.sprint("*Just as long as Wayland actually fills you in on what the hell is going on.")
    answer = str(input("Press enter to continue. "))
    makesave(6)
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
        elif varlist[1] == str("5"):
            varinit()
            part5()
            pass
elif toload == str("n"):
    part1()
