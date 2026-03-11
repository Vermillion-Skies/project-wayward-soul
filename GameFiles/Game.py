import subprocess #Imports the subprocess library to launch the game files
import os #Imports the OS library to check and load files
import Scripts #Imports custom script library

Scripts.screenclear() #the initial game logic that runs at the start
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
subprocess.run(["python", "ChapterOne.py"]) #Loads the chapter 1 python file. This will not work in VSC for some reason, but it does when you just run the file normally. Idk why