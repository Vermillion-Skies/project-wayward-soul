import toga
from toga.constants import Direction
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
from toga.constants import Direction
from toga.command import Group
from pathlib import Path
import asyncio
class WaywardSoul(toga.App):
    def startup(self):
        self.main_box = toga.Box()
        self.main_window = toga.MainWindow(title=self.formal_name)
        prggroup = Group(
            "Game",
            order=40
        )
        cmdsave = toga.Command(
            self.savechk,
            text="Save Game (WIP)",
            tooltip="Saves your game",
            group=prggroup,
            section=0
        )
        self.commands.add(
            cmdsave
        )
        self.loadtitlewindow()
        self.main_window.show()
    def savechk(self, widget):
        print("This shit ain't functional yet")
        #self.savewindow()
    def savewindow(self, widget=None):
        global savewin
        savewin = toga.Window(
            title="Save"
        )
        savewin.content = toga.Box(
            direction=COLUMN,
            children=[
                toga.Button(
                    "Close",
                    on_press=self.closesave
                )
            ]
        )
        savewin.show()
    def closesave(self, widget):
        savewin.close()
    def loadtitlewindow(self, widget=None):
        self.main_box = toga.Box(
            flex=0,
        )
        logobox = toga.Box(
            style=Pack(
                flex=0
            )
        )
        titlebox = toga.Box(
            style=Pack(
                flex=0
            )
        )
        titlebox.add(
            toga.Label(
                "Wayward Soul",
                margin=5,
                flex=0
            )
        )
        uppersplit = toga.SplitContainer(
            content=[
                (logobox, 9),
                (titlebox, 1)
            ],
            direction=Direction.HORIZONTAL,
            flex=1
        )
        mainbuttons = toga.Box(
            style=Pack(
                flex=0
            ),
            direction=COLUMN
        )
        ngb = toga.Button(
            "New Game",
            on_press=self.newgame,
            margin=5,
            flex=0
        )
        lgb = toga.Button(
            "Load Game",
            on_press=self.loadgamewindow,
            margin=5,
            flex=0
        )
        cfb = toga.Button(
            "Config",
            on_press=self.loadconfigwindow,
            margin=5,
            flex=0
        )
        qtb = toga.Button(
            "Quit",
            on_press=self.quitgame,
            margin=5,
            flex=0
        )
        mainbuttons.add(
            ngb,
            lgb,
            cfb,
            qtb
        )
        wholesplit = toga.SplitContainer(
            content=[
                (uppersplit, 9),
                (mainbuttons, 1)
            ],
            direction=Direction.HORIZONTAL,
            flex=1
        )
        self.main_box.add(
            wholesplit
        )
        self.main_window.content = self.main_box
    def quitgame(self, widget=None):
        quit()
    def loadconfigwindow(self, widget=None):
        self.main_box = toga.Box(
            flex=0,
            direction=COLUMN
        )
        self.main_box.add(
            toga.Button(
                "Back",
                on_press=self.loadtitlewindow,
                margin=5
            ),
            toga.Label(
                "The config menu is currently in development!",
                margin=5
            )
        )
        self.main_window.content = self.main_box
    def loadgamewindow(self, widget):
        self.main_box = toga.Box(
            direction=COLUMN
        )
        self.f0b = toga.Button(
            "Autosave",
            on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f1b = toga.Button(
            "File One",
            #on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f2b = toga.Button(
            "File Two",
            #on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.f3b = toga.Button(
            "File Three",
            #on_press=self.loadsave,
            enabled=False,
            margin=5
        )
        self.main_box.add(
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
        self.verifysaves()
        self.main_window.content = self.main_box
    def loadsave(self, widget):
        global chapter
        global part
        global diagID
        if widget.text == "Autosave":
            path = self.paths.data / "sav00.txt"
        elif widget.text == "File One":
            path = self.paths.data / "sav01.txt"
        elif widget.text == "File Two":
            path = self.paths.data / "sav02.txt"
        elif widget.text == "File Three":
            path = self.paths.data / "sav03.txt"
        fout = []
        with open(path, "r") as file:
            fout = [line.strip() for line in file]
        chapter = int(fout[0])
        part = int(fout[1])
        diagID = int(fout[2])
        self.rungame()
    def gamewindowdiag(self, widget=None):
        self.main_box = toga.Box(
            flex=0
        )
        self.winspeaker = toga.Label(
            self.currsce[0],
            margin=5,
            flex=0
        )
        self.windiag = toga.Label(
            self.currsce[1],
            margin=5,
            flex=0
        )
        self.diagbox = toga.Box(
            children=[
                self.winspeaker,
                self.windiag
            ],
            direction=COLUMN
        )
        self.dwb1 = toga.Button(
            "Continue",
            on_press=self.gwbp,
            margin=5
        )
        self.buttonbox = toga.Box(
            children=[
                self.dwb1
            ],
            direction=ROW
        )
        self.gws = toga.SplitContainer(
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
        self.main_box.add(
            self.gws
        )
        self.main_window.content = self.main_box
    def gwbp(self, widget):
        global chapter
        global part
        global diagID
        if widget.text == "Continue":
            diagID += 1
            templist = gamelogic.requestscene()
            if templist[0] == "LN":
                if templist[1] == "P":
                    part += 1
                    templist = gamelogic.requestscene()
                    pass
                elif templist[1] == "C":
                    chapter += 1
                    part = 0
                    templist = gamelogic.requestscene()
            else:
                self.buttonbox.remove(
                    self.dwb1
                )
                self.winspeaker.text = templist[0]
                self.windiag.text = templist[1]
                try:
                    if templist[2] == "buttons":
                        bta = 0
                        bt = templist[3]
                        while bta < bt:
                            cur = 4 + bta
                            self.buttonbox.add(
                                toga.Button(
                                    templist[cur],
                                    on_press=self.gwbp,
                                    margin=5
                                )
                            )
                            bta += 1
                except Exception as e:
                    print(str(e))
                    self.buttonbox.add(
                        self.dwb1
                    )
                    pass
        else:
            if chapter == 0:
                if part == 0:
                    if widget.text == "Yes":
                        diagID = 4
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear()
                        self.winspeaker.text = templist[0]
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            self.dwb1
                        )
                        pass
                    elif widget.text == "No":
                        diagID = 7
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear()
                        self.winspeaker.text = templist[0]
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            self.dwb1
                        )
                    elif widget.text == "Next Chapter":
                        chapter += 1
                        diagID = 0
                        hold = self.autosave()
                        templist = gamelogic.requestscene()
                        self.buttonbox.clear()
                        self.winspeaker.text = templist[0]
                        self.windiag.text = templist[1]
                        self.buttonbox.add(
                            toga.Button(
                                templist[4],
                                on_press=self.gwbp,
                                margin=5
                            )
                        )
                    elif widget.text == "Return to Title":
                        self.loadtitlewindow()
            elif chapter == 1:
                if part == 0:
                    if widget.text == "Return to Title":
                        self.loadtitlewindow()
    def newgame(self, widget):
        global chapter
        global part
        global diagID
        chapter = 0
        part = 0
        diagID = 0
        self.rungame()
    def verifysaves(self):
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
    def autosave(self, widget=None):
        path = self.paths.data / "sav00.txt"
        savefile = [str(chapter), str(part), str(diagID)]
        with open(path, "w") as file:
            pass
        with open(path, "w") as file:
            file.write("\n".join(savefile))
        return "Done"
    def rungame(self, widget=None):
        self.currsce = gamelogic.requestscene()
        self.gamewindowdiag()
    def errwin(self):
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
class gamelogic:
    def requestscene():
        global chapter
        global part
        if chapter == 0:
            if part == 0:
                retlist = gamelogic.c0p0()
        elif chapter == 1:
            if part == 0:
                retlist = gamelogic.c1p0()
        return retlist
    def c0p0():
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
    def c1p0():
        if diagID == 0:
            diag = ["Notice", "Chapter One of the game is currently being ported to this new engine. \nPlease be patient while it is worked on."]
        elif diagID == 1:
            diag = ["Notice", "Please return to the title now.", "buttons", 1, "Return to Title"]
        return diag
def main():
    return WaywardSoul()
