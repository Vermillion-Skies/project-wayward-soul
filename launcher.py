import os
import subprocess

print("Welcome to the Python RPG project (working title)")
print("The game will now check if you have all needed files")
activeinput = 1
retval = 0 #Sets a zeroed out return value. A value of 1 means the operation passed, a value of 2 means there was an error
while activeinput == 1:
    if os.path.isdir("GameFiles/"): #Checks for the presence of game files folder
        if os.path.isfile("GameFiles/Game.py"):
            if os.path.isfile("GameFiles/Scripts.py"):
                if os.path.isfile("GameFiles/ChapterOne.py"):
                    retval = 1
                    activeinput = 0
                    pass
                else:
                    retval = 2
                    activeinput = 0
                    pass
            else:
                retval = 2
                activeinput = 0
                pass
        else:
            retval = 2
            activeinput = 0
            pass
    else:
        retval = 2
        activeinput = 0
        pass
if retval == 2:
    print("You are missing files, and the game is unable to continue. Please redownload the game. If you are absolutely sure you have all files needed, please leave an issue on te github.")
    answer = str(input("Press enter to close the game."))
    quit()
elif retval == 1:
    pass
elif retval == 0:
    print("An unknown error has occured and the game needs to close")
    quit()
print("")
activeinput = 1
while activeinput == 1: #Loop to check if the user wishes to load a file
    answer = str(input("Would you like to load a save? (y/n) "))
    if answer == str("y"):
        if os.path.isdir("GameFiles/Saves/"): #Checks if the saves folder exists
            if os.path.isfile("GameFiles/Saves/save.txt"): #Checks if a save exists
                try:
                    with open("GameFiles/Saves/save.txt", "r") as f: #Attempts to open the save file in read only mode
                        chapter = f.readline().strip() #Reads the first line of the save file, omitting any newline characters
                        activeinput = 0
                        pass
                except Exception as e:
                    print("An error occured loading the save, proceeding with new game")
                    chapter = 0
                    activeinput = 0
                    pass
                pass
            else:
                print("Your save folder exists, but the save file does not. Proceeding as a new game")
                chapter = 0
                activeinput = 0
                pass
            pass
        else:
            print("Your save file directory does not exist. Continuing with a new game.")
            chapter = 0
            activeinput = 0
            pass
        pass
    else:
        chapter = 0
        activeinput = 0
        pass
    pass
if chapter == 0:
    print("Proceeding with a new game")
    answer = str(input("Press enter to continue"))
    subprocess.run(["python", "GameFiles/Game.py"], check=True)
if chapter == 1:
    print("Continuing from Chapter 1")
    answer = str(input("Press enter to continue"))
    subprocess.run(["python", "GameFiles/ChapterOne.py"], check=True)
    