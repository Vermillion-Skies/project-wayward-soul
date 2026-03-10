import random #Imports the random library for use in stat calculations and rolls

def screenclear(): #function to blank out the terminal window for the game
    rep = int(0)
    while rep < 50:
        print("")
        rep = rep + 1
        pass
    pass
pass


def charactermake(): #Function for the beginning character creation part of the game
    global name #sets many variables to be global, rather than locked to this function
    global health
    global money
    global strength
    global defense
    global wisdom
    global speed
    screenclear()
    print("You are a wayward soul.")
    print("One without path, without purpose")
    print("A blank slate, both in past and in future")
    print("However, even a blank slate can be written upon, sculpted anew")
    print("And such a process begins with knowing Yourself")
    name = str(input("How shall the world know you? (enter your name) "))
    print(name + "...")
    print("A name most uncommon in this world, and yet not an unwelcome one")
    print("Although, I could swear I've heard it before...")
    print("Ah, an unimportant detail")
    print("We shall now see how the world wishes to build you...")
    answer = str(input("(Press enter to roll your stats. It will only be done once.)"))
    strength = random.randint(1,20)
    defense = random.randint(1,20)
    wisdom = random.randint(1,20)
    speed = random.randint(1,20)
    health = random.randint(50,145)
    money = random.randint(0,300)
    print("")
    print("---===STATS ROLLED===---")
    print("HP:", health)
    print("STARTING CASH:", money)
    print("STR:", strength)
    print("DEF:", defense)
    print("WIS:", wisdom)
    print("SPD:", speed)
    print("----------------------------")
    print("")
    answer = str(input("(Press enter to continue)"))
    print("")
    print("Interesting... Most interesting...")
    print("It seems the stars above have a very specific path planned for you.")
    print("Until you reach the end of the path, try not to die")
    print("")
    print("*as the voice says this, you feel a light shining in front of you")
    answer = str(input("(Press enter to step towards this light)"))
    print("")
    print("*The light grows brighter as you step toward it. Every inch enveloping your body further in radiance.")
    print("*As you take one final step, you feel your vision go dark as you protect yourself from the beams of light")
    print("")
    answer = str(input("(Press enter to continue)"))
    chapter1p1()
    pass

def chapter1p1(): # Function for all logic of the first part of the first chapter of the game
    global name #sets many variables to be global, rather than locked to this function
    global health
    global money
    global strength
    global defense
    global wisdom
    global speed
    screenclear()
    print("*When you finally come to, you slowly open your eyes")
    print("*You did not have eyes before, you don't believe you ever have")
    print("*Your eyes slowly adjust to the light, and you become aware of your surroundings")
    print("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you")
    print("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast")
    print("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    print("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    print("*You speak softly to yourself, growing more used to this voice")
    print(name + ": ...suppose I could look around")
    

screenclear() #the initial game logic that runs at the start
print("Welcome, adventurer, to the game")
print("This game is a work of fiction. Any resemblences to any person, living or dead, is completely coincidental")
print("Only by agreeing to these rules will you be allowed to continue into the game.")
activeinput = 1
while activeinput == 1:
    answer = str(input("Do you agree to the rules? (y/n) "))
    if answer == str("y"):
        print("Good. Very, very good.")
        activeinput = 0
        pass
    elif answer == str("n"):
        print("I see. Such a pity.")
        print("No point in letting this go on any further then.")
        print("Hasta le vista.")
        quit()
    else:
        print("Hm. Not sure you read the instructions correctly.")
        print("Let's try again, shall we?")
        pass
    pass
print("")
print("The contract has been signed")
print("As such, the journey may begin.")
print("Best of luck, oh wandering soul")
answer = str(input("(press enter to continue)"))
charactermake()
