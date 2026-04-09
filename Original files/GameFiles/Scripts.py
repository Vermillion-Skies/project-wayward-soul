import os
import sys
import time
import subprocess 
def screenclear(): #function to blank out the terminal window for the game 
    rep = int(0)
    try:
        while rep < 100:
            print("") #Prints a blank line
            rep = rep + 1 #Increments rep by 1
            pass
        pass
    except Exception as e: #Exception catcher
        errorhandle("SC0") #Calls in-house error handler (Should never happen here?)
    pass
def savegame(x): #Function to save a provided list to a file
    activeinput = 1
    while activeinput == 1:
        if os.path.isdir("GameFiles/Saves/"): #Checks if the saves folder exists
            try:
                with open("GameFiles/Saves/save.txt", "w") as f: #Opens and clears the file
                    pass
                with open("GameFiles/Saves/save.txt", "w") as file: #Writes the list to the file, separated with newline characters
                    file.write("\n".join(x))
                    pass
                activeinput = 0
                pass
            except Exception as e: #Exception catcher
                errorhandle("SG0") #Calls in-house error handler
        else:
            try:
                os.mkdir("GameFiles/Saves/") #Creates the save folder and passes to continue the loop
                pass
            except Exception as e: #Exception catcher
                errorhandle("SG1") #Calls in-house error handler
def loadgame(): #Function to load a file and return a list
    if os.path.isdir("GameFiles/Saves/"): #Checks if the saves folder exists
        if os.path.isfile("GameFiles/Saves/save.txt"): #Checks if the save file exists
            try:
                with open("GameFiles/Saves/save.txt", "r") as file: #Attempts to open the file in read-only mode
                    retlist = [line.strip() for line in file] #Writes every line from the file to the list, using strip to remove newline characters
                    return retlist #Returns the list to the process that called it
                    pass
            except Exception as e:
                errorhandle("LG0") #Calls in-house error handler
                pass
        else:
            retlist = ["No"]
            return retlist
            #errorhandle("LG1") #Calls in-house error handler
            pass
    else:
        retlist = ["No"]
        return retlist
        #errorhandle("LG2") #Calls in-house error handler
        pass
    pass
def errorhandle(x): #In-house error handler
    screenclear()
    print("AN ERROR HAS OCCURED AND THE GAME HAS CRASHED")
    print("Error code: " + x)
    print("Please consult the error code documentation on github for more information")
    print("")
    answer = str(input("Please close the program"))
def statcheck(x, y): #Stat check where X is the minimum stat and Y is the stat to check
    x = int(x) #Attempts to convert X to an integer
    y = int(y) #Attempts to convert Y into an integer
    try: #Loop to check if the stat is at or above minimum needed value
        if x > y:
            return("Fail")
        elif x < y:
            return("Pass")
        elif x == y:
            return("Pass")
    except Exception as e: #Exception handler just in case
        errorhandle("SC1")
def checkcache(x): #Check line x of the cache
    try:
        with open("GameFiles/Saves/cachelocal.txt", "r") as file: #Attempts to load the cache file into a list
            loadcache = file.read().splitlines()
            pass
        pass
    except Exception as e: #Exception catcher
        errorhandle("CC0")
    return str(loadcache[x]) #Returns the first value of the cache
    pass
def writecache(x, y): #Write value y to line x of the cache
    try:
        with open("GameFiles/Saves/cachelocal.txt", "r") as file: #Attempts to load the cache into a list
            loadcache = [line.strip() for line in file]
            pass
        pass
    except Exception as e:
        errorhandle("WC0")
        pass
    loadcache[x] = y
    try:
        with open("GameFiles/Saves/cachelocal.txt", "w") as file: #Opens and clears the cache
            pass
        with open("GameFiles/Saves/cachelocal.txt", "w") as file: #Attempts to write the new cache to the file
            file.write("\n".join(loadcache))
            pass
        pass
    except Exception as e:
        errorhandle("WC1")
        pass
def sprint(x): #Special print function to print each character one at a time
    for c in x:
        sys.stdout.write(c)
        sys.stdout.flush() #Forces immediate output
        if c == str(".") or c == str(",") or c == str("?") or c == str("!") or c == str(":"):
            time.sleep(0.15)
            pass
        else:
            time.sleep(0.05) #Small delay before typing next character
            pass

    time.sleep(0.5) #Delay between next text line
    print() #Prints a newline character
    pass
def gameover(): #Text that will display upon a game over
    screenclear()
    sprint("THE VOICE: So it seems you couldn't follow the path until the end...")
    sprint("THE VOICE: Such a pity, we had so much faith in you.")
    sprint("THE VOICE: Seems it was purely unfounded.")
    sprint("THE VOICE: Return then, to the Plane Of Souls.")
    sprint("THE VOICE: Forevermore.")
    print("")
    sprint("You have died.")
    sprint("You can reload your save upon restarting the game.")
    sprint("Don't keep us waiting.")
    unkill = 10
    while unkill == 10: #Literally just an unkillable loop to force a restart of the game
        time.sleep(1)
    pass
def loadchapter(x): #Loads a defined chapter
    if x == str("1"):
        subprocess.run(["python", "GameFiles/ChapterOne.py"])
        pass
    elif x == str("2"):
        subprocess.run(["python", "GameFiles/ChapterTwo.py"])
        pass
    pass
def linebreak(): #Literally just a linebreak for choice loops
    print("")
    print("----------")
    pass
def gendercheck(gender, refcode, capcode, name): # Checks gender and returns the appropriate term for what's requested
    x = int(gender)
    y = int(refcode)
    z = int(capcode)
    a = str(name)
    if x == 0: #Checks for non-binary gender
        if y == 0: #returns "person"
            if z == 0: #lowercase
                return("person")
                pass
            elif z == 1: #Capitalized
                return("Person")
                pass
            elif z == 2: #All caps
                return("PERSON")
                pass
            pass
        elif y == 1: #Returns "they"
            if z == 0: #lowercase
                return("they")
                pass
            elif z == 1: #Capitalized
                return("They")
                pass
            elif z == 2: #All caps
                return("THEY")
                pass
            pass
        elif y == 2: #returns "them"
            if z == 0: #lowercase
                return("them")
                pass
            elif z == 1: #Capitalized
                return("Them")
                pass
            elif z == 2: #All caps
                return("THEM")
                pass
            pass
        elif y == 3: #Returns theirs
            if z == 0: #lowercase
                return("theirs")
                pass
            elif z == 1: #Capitalized
                return("Theirs")
                pass
            elif z == 2: #All caps
                return("THEIRS")
                pass
            pass
        pass
    elif x == 1: #Checks for male gender
        if y == 0: #returns "man"
            if z == 0: #lowercase
                return("man")
                pass
            elif z == 1: #Capitalized
                return("Man")
                pass
            elif z == 2: #All caps
                return("MAN")
                pass
            pass
        elif y == 1: #Returns "he"
            if z == 0: #lowercase
                return("he")
                pass
            elif z == 1: #Capitalized
                return("He")
                pass
            elif z == 2: #All caps
                return("HE")
                pass
            pass
        elif y == 2: #returns "him"
            if z == 0: #lowercase
                return("him")
                pass
            elif z == 1: #Capitalized
                return("Him")
                pass
            elif z == 2: #All caps
                return("HIM")
                pass
            pass
        elif y == 3: #Returns "his"
            if z == 0: #lowercase
                return("his")
                pass
            elif z == 1: #Capitalized
                return("His")
                pass
            elif z == 2: #All caps
                return("HIS")
                pass
            pass
        pass
    elif x == 2: #Checks for female gender
        if y == 0: #returns "woman"
            if z == 0: #lowercase
                return("woman")
                pass
            elif z == 1: #Capitalized
                return("Woman")
                pass
            elif z == 2: #All caps
                return("WOMAN")
                pass
            pass
        elif y == 1: #Returns "she"
            if z == 0: #lowercase
                return("she")
                pass
            elif z == 1: #Capitalized
                return("She")
                pass
            elif z == 2: #All caps
                return("SHE")
                pass
            pass
        elif y == 2: #returns "her"
            if z == 0: #lowercase
                return("her")
                pass
            elif z == 1: #Capitalized
                return("Her")
                pass
            elif z == 2: #All caps
                return("HER")
                pass
            pass
        elif y == 3: #Returns "hers"
            if z == 0: #lowercase
                return("hers")
                pass
            elif z == 1: #Capitalized
                return("Hers")
                pass
            elif z == 2: #All caps
                return("HERS")
                pass
            pass
        pass
    elif x == 2: #Checks for no gender
        if y == 0: #returns "person"
            if z == 0: #lowercase
                return("person")
                pass
            elif z == 1: #Capitalized
                return("Person")
                pass
            elif z == 2: #All caps
                return("PERSON")
                pass
            pass
        elif y == 1: #Returns name
            if z == 0: #lowercase
                return(a)
                pass
            elif z == 1: #Capitalized
                return(a)
                pass
            elif z == 2: #All caps
                return(a)
                pass
            pass
        elif y == 2: #returns name
            if z == 0: #lowercase
                return(a)
                pass
            elif z == 1: #Capitalized
                return(a)
                pass
            elif z == 2: #All caps
                return(a)
                pass
            pass
        elif y == 3: #Returns name's
            if z == 0: #lowercase
                return(a + "'s")
                pass
            elif z == 1: #Capitalized
                return(a + "'s")
                pass
            elif z == 2: #All caps
                return(a + "'s")
                pass
            pass
        pass
    pass