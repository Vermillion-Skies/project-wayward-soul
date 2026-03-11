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
    chapter, part, name, health, maxhealth, money, strength, defense, wisdom, speed = varlist
    pass
def makesave():
    print("")
    answer = str(input("Would you like to save the game? (y/n) "))
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed)]
        Scripts.savegame(varlist)
        pass
    else:
        pass
    pass
def part1(): #Function for the beginning character creation part of the game
    global chapter
    global part
    global name #sets many variables to be global, rather than locked to this function
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
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
    maxhealth = random.randint(50,145)
    money = random.randint(0,300)
    health = maxhealth
    print("")
    print("---===STATS ROLLED===---")
    print("HP:", maxhealth)
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
    part = 2
    chapter = 1
    makesave()
    part2()
    pass

def part2(): # Function for all logic of the first part of the first chapter of the game
    global name #sets many variables to be global, rather than locked to this function
    global maxhealth
    global health
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    print("*When you finally come to, you slowly open your eyes")
    print("*You did not have eyes before, you don't believe you ever have")
    print("*Your eyes slowly adjust to the light, and you become aware of your surroundings")
    print("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you")
    print("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast")
    print("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    print("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    print("*You speak softly to yourself, growing more used to this voice")
    print(name + ": ...suppose I could look around")
    print("")
    activeinput = 1
    while activeinput == 1:
        print("1) Look left")
        print("2) Look right")
        print("3) Look to the sky")
        print("4) Stop looking and stand up")
        answer = str(input("Enter selection: "))
        if answer == str("1"):
            print("")
            print("----------")
            print("*As you look to your left, you see a large pond of sorts.")
            print("*Many animals are drinking from the pond, and wild flora seem to be growing plentifully around it's crystal blue waters.")
            print("*You can't quite explain it, but somehow this puts your mind at ease.")
            print("----------")
            print("")
            print("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            print("*To your right, you notice a sprawling forest of emerald green trees and bushes")
            print("*You can't quite see into it, but based on the outside it must be full of life")
            print("*As you admire it, you notice birds flying off from the trees, moving in a triangular formation")
            print("*And yet... something about it makes you shudder. But why?")
            print("----------")
            print("")
            print("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("3"):
            print("")
            print("----------")
            print("*You turn your head up to the sky, squinting your eyes as the sun shines upon you")
            print("*As the clouds slowly move to envelop the sun's light, your vision becomes clearer")
            print("*This moment of quiet contemplation clears your mind, you feel more wise!")
            wisdom = wisdom + int(1)
            print("(Wisdom increased to", wisdom, "!)")
            print("----------")
            print("")
            print("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("4"):
            activeinput = 0
            pass
        else:
            print("Invalid input, please try again")
            pass
        pass
    print("")


Scripts.screenclear() #the initial game logic that runs at the start
varlist = Scripts.loadgame()
if varlist[0] == str("No"):
    part1()
else:
    if varlist[1] == str("2"):
        varinit()
        part2()