import os
def screenclear(): #function to blank out the terminal window for the game
    rep = int(0)
    while rep < 50:
        print("")
        rep = rep + 1
        pass
    pass
def savegame(x): #Function to save a provided list to a file
    activeinput = 1
    while activeinput == 1:
        if os.path.isdir("Saves/"): #Checks if the saves folder exists
            try:
                with open("Saves/save.txt", "w") as f: #Opens and clears the file
                    pass
                with open("Saves/save.txt", "w") as file: #Writes the list to the file, separated with newline characters
                    file.write("\n".join(x))
                    pass
                activeinput = 0
                pass
            except Exception as e: #Exception catcher
                errorhandle("SS0") #Calls in-house error handler
        else:
            try:
                os.mkdir("Saves/") #Creates the save folder and passes to continue the loop
                pass
            except Exception as e: #Exception catcher
                errorhandle("SS1") #Calls in-house error handler
def loadgame(): #Function to load a file and return a list
    if os.path.isdir("Saves/"): #Checks if the saves folder exists
        if os.path.isfile("Saves/save.txt"): #Checks if the save file exists
            try:
                with open("Saves/save.txt", "r") as file: #Attempts to open the file in read-only mode
                    retlist = [line.strip() for line in file] #Writes every line from the file to the list, using strip to remove newline characters
                    return retlist #Returns the list to the process that called it
                    pass
            except Exception as e:
                errorhandle("SL0") #Calls in-house error handler
                pass
        else:
            errorhandle("SL1") #Calls in-house error handler
            pass
    else:
        errorhandle("SL2") #Calls in-house error handler
        pass
    pass
def errorhandle(x): #In-house error handler
    screenclear()
    print("AN ERROR HAS OCCURED AND THE GAME HAS CRASHED")
    print("Error code: " + x)
    print("Please consult the error code documentation on github for more information")
    print("")
    answer = str(input("Press enter to close the program."))
    quit()