import subprocess #Imports the subprocess library to launch the game files
import os #Imports the OS library to check and load files
import Scripts #Imports custom script library
#For all intents and purposes, prologue is considered feature complete
Scripts.screenclear() #the initial game logic that runs at the start
Scripts.sprint("Welcome, adventurer, to the game.")
Scripts.sprint("This game is a work of fiction. Any resemblences to any person, living or dead, is completely coincidental.")
Scripts.sprint("Only by agreeing to these rules will you be allowed to continue into the game.")
activeinput = 1
while activeinput == 1:
    answer = str(input("Do you agree to the rules? (y/n) "))
    if answer == str("y"):
        Scripts.sprint("Good. Very, very good.")
        activeinput = 0
        pass
    elif answer == str("n"):
        Scripts.sprint("I see. Such a pity.")
        Scripts.sprint("No point in letting this go on any further then.")
        Scripts.sprint("Hasta le vista.")
        quit()
    else:
        Scripts.sprint("Hm. Not sure you read the instructions correctly.")
        Scripts.sprint("Let's try again, shall we?")
        pass
    pass
print("")
Scripts.sprint("The contract has been signed.")
Scripts.sprint("As such, the journey may begin.")
Scripts.sprint("Best of luck, oh lost one.")
answer = str(input("(press enter to continue)"))
Scripts.loadchapter(str("1")) #Loads the chapter 1 python file. This will not work in VSC for some reason, but it does when you just run the file normally. Idk why