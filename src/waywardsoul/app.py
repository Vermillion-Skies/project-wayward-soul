import toga
from toga.constants import Direction
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
from toga.constants import Direction
from toga.command import Group
from pathlib import Path
import asyncio
class WaywardSoul(toga.App): # Class with all window logic, file I/O procedures, and app runtime logic
    def startup(self): # Function run at startup of the program
        self.main_box = toga.Box() # Creates a content box
        self.main_window = toga.MainWindow( # Creates the main window
            title=self.formal_name
        )
        prggroup = Group( # Creates a group of functions for the titlebar
            "Game",
            order=40
        )
        cmdsave = toga.Command( # Adds a save command to the function group (IN DEVELOPMENT)
            self.savechk,
            text="Save Game",
            tooltip="Saves your game",
            group=prggroup,
            section=0
        )
        self.commands.add( # Adds commands to the previously defined group
            cmdsave
        )
        self.loadtitlewindow() # Loads the contents of the title screen window
        self.main_window.show() # Shows the window
    def savechk(self, widget): # Function to check if you're at a point where saving is allowed
        cansave = 0 # Defaults value to 0, won't open save window if value is still 0
        if chapter == "n":
            pass
        elif chapter == 0:
            if part == 0:
                if diagID == 3:
                    pass
                elif diagID == 6:
                    pass
                elif diagID == 9:
                    pass
                else:
                    cansave = 1
                    pass
                pass
            pass
        elif chapter == 1:
            if part == 0:
                pass
            pass
        if cansave == 1:
            self.savewindow()
        else:
            pass
    def savewindow(self, widget=None): # Window to save the game (IN DEVELOPMENT)
        global savewin
        savewin = toga.Window( # Makes a new window titled "Save"
            title="Save"
        )
        savewin.content = toga.Box( # Adds content to the newly made window
            direction=COLUMN,
            children=[
                toga.Button( # Adds a close button
                    "Close",
                    on_press=self.closesave
                ),
                toga.Button(
                    "File One",
                    on_press=self.savegame
                ),
                toga.Button(
                    "File Two",
                    on_press=self.savegame
                ),
                toga.Button(
                    "File Three",
                    on_press=self.savegame
                )
            ]
        )
        savewin.show()
    def savegame(self, widget=None): # Function to save variables to a selected save file
        if widget == None:
            path = self.paths.data / "sav00.txt"
        elif widget.text == "File One":
            path = self.paths.data / "sav01.txt"
        elif widget.text == "File Two":
            path = self.paths.data / "sav02.txt"
        elif widget.text == "File Three":
            path = self.paths.data / "sav03.txt"
        savefile = [str(chapter), str(part), str(diagID)]
        with open(path, "w") as file:
            pass
        with open(path, "w") as file:
            file.write("\n".join(savefile))
        if widget == None:
            return "Done"
        else:
            self.closesave()
    def closesave(self, widget=None): # Function to close the save window
        savewin.close()
    def loadtitlewindow(self, widget=None): # Main title window
        global chapter
        chapter = "n" # Sets chapter to an empty value to prevent saving game on title screen
        self.main_box = toga.Box( # Box to contain all contents defined in this function
            flex=0,
        )
        logobox = toga.Box( # Box to contain logo image (Currently placeholder)
            style=Pack(
                flex=0
            )
        )
        titlebox = toga.Box( # Box to contain name of the game
            style=Pack(
                flex=0
            )
        )
        titlebox.add( # Adds a label with the game's nme to the titlebox
            toga.Label(
                "Wayward Soul",
                margin=5,
                flex=0
            )
        )
        uppersplit = toga.SplitContainer( # Creates the upper split container containing logo and title
            content=[
                (logobox, 9),
                (titlebox, 1)
            ],
            direction=Direction.HORIZONTAL,
            flex=1
        )
        mainbuttons = toga.Box( # Box to contain all title screen buttons
            style=Pack(
                flex=0
            ),
            direction=COLUMN
        )
        ngb = toga.Button( # Button to start a new game
            "New Game",
            on_press=self.newgame,
            margin=5,
            flex=0
        )
        lgb = toga.Button( # Button to pull up the load game window
            "Load Game",
            on_press=self.loadgamewindow,
            margin=5,
            flex=0
        )
        cfb = toga.Button( # Button to pull up the config window
            "Config",
            on_press=self.loadconfigwindow,
            margin=5,
            flex=0
        )
        qtb = toga.Button( # Button to quit the game
            "Quit",
            on_press=self.quitgame,
            margin=5,
            flex=0
        )
        mainbuttons.add( # Adds all buttons to the button box
            ngb,
            lgb,
            cfb,
            qtb
        )
        wholesplit = toga.SplitContainer( # Creates the full split container with the upper split and button box
            content=[
                (uppersplit, 9),
                (mainbuttons, 1)
            ],
            direction=Direction.HORIZONTAL,
            flex=1
        )
        self.main_box.add( # Sets the whole split as the content of the main box
            wholesplit
        )
        self.main_window.content = self.main_box # Adds the main box to the window, overwriting any previous window contents if they exist
    def quitgame(self, widget=None): # Function that quits the game
        quit()
    def loadconfigwindow(self, widget=None): # Window with game configuration options (IN DEVELOPMENT)
        self.main_box = toga.Box( # Main box to contain content defined in this function
            flex=0,
            direction=COLUMN
        )
        self.main_box.add( # Adds content to config box
            toga.Button( # Button to reload the title screen
                "Back",
                on_press=self.loadtitlewindow,
                margin=5
            ),
            toga.Button( # Button to load save management window
                "Save Management",
                on_press=self.configbutton,
                margin=5
            ),
            toga.Button( # Button to load development credits
                "Credits",
                on_press=self.configbutton,
                margin=5
            ),
            toga.Button( # Button to load information about current software version
                "Software information",
                on_press=self.configbutton,
                margin=5
            )
        )
        self.main_window.content = self.main_box
    def loadgamewindow(self, widget): # Window where loadable saves are shown
        self.main_box = toga.Box( # Main box to contain save file buttons
            direction=COLUMN
        )
        self.f0b = toga.Button( # f0-3b define buttons for each possible save file, with all being disabled by default
            "Autosave",
            on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f1b = toga.Button(
            "File One",
            on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f2b = toga.Button(
            "File Two",
            on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f3b = toga.Button(
            "File Three",
            on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.main_box.add( # Adds all buttons to the main content box
            toga.Button(
                "Go Back",
                on_press=self.loadtitlewindow,
                margin=5
            ),
            self.f0b,
            self.f1b,
            self.f2b,
            self.f3b
        )
        self.verifysaves() # Verifies existence of save data files
        self.main_window.content = self.main_box # Overwrites main window content with content defined in this function
    def loadsave(self, widget): # Function to read data from a selected save file and save its properties to program variables
        global chapter
        global part
        global diagID
        if widget.text == "Autosave": # Checks contents of the load button widget's text to determine what save file to load
            path = self.paths.data / "sav00.txt"
        elif widget.text == "File One":
            path = self.paths.data / "sav01.txt"
        elif widget.text == "File Two":
            path = self.paths.data / "sav02.txt"
        elif widget.text == "File Three":
            path = self.paths.data / "sav03.txt"
        fout = [] # Defines an empty list for save file contents
        with open(path, "r") as file: # Opens the file in read-only mode
            fout = [line.strip() for line in file] # Saves each line of the save as a different list item
        chapter = int(fout[0]) # Sets chapter, part, and diag ID to their properties in the loaded save
        part = int(fout[1])
        diagID = int(fout[2])
        self.rungame() # Starts the game
    def gamewindowdiag(self, widget=None): # Function to make game window for dialogue scenes
        self.main_box = toga.Box( # Box to contain assets defined in this function
            flex=0
        )
        self.winspeaker = toga.Label( # Speaker label
            self.currsce[0],
            margin=5,
            flex=0
        )
        self.windiag = toga.Label( # Dialogue label
            self.currsce[1],
            margin=5,
            flex=0
        )
        self.diagbox = toga.Box( # Box containing both speaker and dialogue windows
            children=[
                self.winspeaker,
                self.windiag
            ],
            direction=COLUMN
        )
        self.dwb1 = toga.Button( # Default continue button
            "Continue",
            on_press=self.gwbp,
            margin=5
        )
        self.buttonbox = toga.Box( # Box to contain all buttons needed
            children=[
                self.dwb1
            ],
            direction=ROW
        )
        self.gws = toga.SplitContainer( # Split container to hold diagbox and buttonbox in one window
            content=[
                (
                    self.diagbox,
                    9
                ),
                (
                    self.buttonbox,
                    1
                )
            ],
            direction=Direction.HORIZONTAL,
            flex=1
        )
        self.main_box.add( # Adds split container to main content box
            self.gws
        )
        self.main_window.content = self.main_box # Overwrites current window contents with newly defined assets
    def gwbp(self, widget): # Function to handle when a button is pressed during gameplay.
        global chapter
        global part
        global diagID
        if widget.text == "Continue": # Set of code for when the button is the stndard continue button
            diagID += 1 # Increments the diagID by 1
            templist = gamelogic.requestscene() # Fetches new scene data
            if templist[0] == "LN": # If the fetched data is calling for LN (or "load new")
                if templist[1] == "P": # Moves to next part
                    part += 1
                    templist = gamelogic.requestscene()
                    pass
                elif templist[1] == "C": # Moves to next chapter
                    chapter += 1
                    part = 0
                    templist = gamelogic.requestscene()
            else:
                self.buttonbox.remove( # Removes the default continue button from the window
                    self.dwb1
                )
                self.winspeaker.text = templist[0] # Sets the speaker label to the returned speaker name
                self.windiag.text = templist[1] # Sets the dialogue label to the returned dialogue
                try: # Runs this to check if the returned scene data contains buttons
                    if templist[2] == "buttons":
                        bta = 0 # Buttons added
                        bt = templist[3] # Buttons total in the returned list
                        while bta < bt:
                            cur = 4 + bta # Current point in the list
                            self.buttonbox.add( # Adds the button to the dialogue button box
                                toga.Button(
                                    templist[cur], # String contents of point cur in the list
                                    on_press=self.gwbp, # Runs universal button press function on press
                                    margin=5
                                )
                            )
                            bta += 1 # Increments buttons added by 1
                except Exception as e: # Runs if there's no button data returned
                    print(str(e)) # Prints the exception in console just in case it's an unexpected one
                    self.buttonbox.add(
                        self.dwb1 # Adds standard continue button to the button box
                    )
                    pass
        else: # Logic for buttons in each chapter and part
            if chapter == 0: # Chapter 0 buttons
                if part == 0: # Part 0 buttons
                    if widget.text == "Yes": # Yes button from initial agreement
                        diagID = 4 
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear() # Removes all buttons
                        self.winspeaker.text = templist[0] 
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            self.dwb1
                        )
                        pass
                    elif widget.text == "No": # No button from initial agreement
                        diagID = 7
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear()
                        self.winspeaker.text = templist[0]
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            self.dwb1
                        )
                    elif widget.text == "Next Chapter": # Next chapter button from end of chapter 0 (yes button pressed)
                        chapter += 1
                        diagID = 0
                        hold = self.savegame()
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear()
                        self.winspeaker.text = templist[0]
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            self.dwb1
                        )
                    elif widget.text == "Return to Title": # Return to title button from end of chapter 0 (no button pressed)
                        self.loadtitlewindow()
            elif chapter == 1: # Chapter 1 buttons
                if part == 0: # Part 0 buttons
                    if widget.text == "Return to Title": # Return to title button (Will be removed upon further development of the dialogue)
                        self.loadtitlewindow()
    def newgame(self, widget): # Function that sets all progress variables to default values before running rungame()
        global chapter
        global part
        global diagID
        chapter = 0
        part = 0
        diagID = 0
        self.rungame()
    def verifysaves(self): # Function to verify the existence of save files in the saves directory. Upon confirming existence, makes the associated button for the file enabled
        filestocheck = 3
        filechecking = 0
        while filechecking <= filestocheck:
            file = "sav0" + str(filechecking) + ".txt"
            path = self.paths.data / file
            if not path.exists():
                pass
            else:
                if filechecking == 0:
                    self.f0b.enabled = True
                elif filechecking == 1:
                    self.f1b.enabled = True
                elif filechecking == 2:
                    self.f2b.enabled = True
                elif filechecking == 3:
                    self.f3b.enabled = True
            filechecking += 1
            pass
    def rungame(self, widget=None): # Function to fetch the current scene when called (either from a loaded save or a new game) and then loading the game dialogue window
        self.currsce = gamelogic.requestscene()
        self.gamewindowdiag()
    def errwin(self): # Function to show an error window upon a fatal exception, closing the program upon confirming the error
        errd = toga.ErrorDialog(
            "An Error Has Occurred",
            errt
        )
        task = asyncio.create_task(
            self.main_window.dialog(
                errd
            )
        )
        task.add_done_callback(quit)
class gamelogic: # Class containing logic for routing process to the correct chapter for the scene requested
    def requestscene(): # Function to return scene data
        global chapter
        if chapter == 0:
            retlist = chapter0.partch()
        elif chapter == 1:
            retlist = chapter1.partch()
        return retlist
class chapter0: # Class containing logic and dialogue for chapter 0 of the game
    def partch(): # Function to select the right part to grab data from based on global part variable
        global part
        if part == 0:
            toret = chapter0.part0()
        return toret
    def part0(): # Function containing all dialogue info for part 0 of chapter 0
        if diagID == 0:
            diag = ["System", "Welcome, adventurer, to the game."]
        elif diagID == 1:
            diag = ["System", "This game is a work of fiction. Any resemblences to any person, living or dead, is completely concidental."]
        elif diagID == 2:
            diag = ["System", "Only by accepting this will you be allowed to continue into the game."]
        elif diagID == 3:
            diag = ["CHOICE", "Do you accept?", "buttons", 2, "Yes", "No"]
        elif diagID == 4:
            diag = ["System", "Excellent, quite excellent indeed."]
        elif diagID == 5:
            diag = ["System", "Since you agree, then we may continue."]
        elif diagID == 6:
            diag = ["System", "See you on the other side, traveller.", "buttons", 1, "Next Chapter"]
        elif diagID == 7:
            diag = ["System", "...I see then."]
        elif diagID == 8:
            diag = ["System", "Then I see little reason to keep this useless link open."]
        elif diagID == 9:
            diag = ["System", "Return to the plane of souls, traveller.", "buttons", 1, "Return to Title"]
        return diag
class chapter1: # Class containing logic and dialogue for chapter 1 of the game
    def partch(): # Function to select the right part to grab data from based on the global part variable
        global part
        if part == 0:
            toret = chapter1.part0()
        return toret
    def part0(): # Function containing all dialogue info for part 0 of chapter 1
        if diagID == 0:
            diag = ["Notice", "Chapter One of the game is currently being ported to this new engine. \nPlease be patient while it is worked on."]
        elif diagID == 1:
            diag = ["Notice", "Please return to the title now.", "buttons", 1, "Return to Title"]
        return diag
def main(): # Function called by __main__.py that starts running the app
    return WaywardSoul()
