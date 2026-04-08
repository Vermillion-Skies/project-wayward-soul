import toga
from toga.constants import Direction
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
from toga.constants import Direction
from pathlib import Path
import asyncio
class WaywardSoul(toga.App):
    def startup(self):
        self.main_box = toga.Box()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.loadtitlewindow()
        self.main_window.show()
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
            #on_press=self.configmenu,
            margin=5,
            flex=0
        )
        qtb = toga.Button(
            "Quit",
            #on_press=self.quit,
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
    def loadgamewindow(self, widget):
        self.main_box = toga.Box(
            direction=COLUMN
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
            self.f1b,
            self.f2b,
            self.f3b
        )
        self.verifysaves()
        self.main_window.content = self.main_box
    def gamewindowdiag(self):
        self.main_box = toga.Box(
            flex=0
        )
        self.winspeaker = toga.Label(
            "Speaker",
            margin=5,
            flex=0
        )
        self.windiag = toga.Label(
            "Dialogue",
            margin=5,
            flex=0
        )
        self.diagbox = toga.Box(
            children=[
                self.winspeaker,
                self.windiag
            ],
            direction=ROW
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
            direction=COLUMN
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
        self.main_window.content(
            self.main_box
        )
    def gwbp(self, widget):
        pass
    def verifysaves(self):
        filestocheck = 3
        filechecking = 1
        while filechecking <= filestocheck:
            file = "sav0" + str(filechecking) + ".txt"
            path = self.paths.data / file
            if not path.exists():
                pass
            else:
                if filechecking == 1:
                    self.f1b.enabled = True
                elif filechecking == 2:
                    self.f2b.enabled = True
                elif filechecking == 3:
                    self.f3b.enabled = True
            filechecking += 1
            pass
    def newgame(self, widget):
        global currch
        global currpt
        global req
        global errt
        currch = "0"
        req = "D"
        self.dialoguelist = self.getdialogue()
        print(self.dialoguelist)
        req = "S"
        self.speakerlist = self.getdialogue()
        if self.dialoguelist[0] == "ERROR":
            errt = "Error: Dialogue file doesn't exist. Maybe it's corrupted?"
            self.errwin()
        else:
            if self.speakerlist[0] == "ERROR":
                errt = "Error: Dialogue speaker file doesn't exist. Maybe it's corrupted?"
                self.errwin()
            else:
                self.rungame()
    def getdialogue(self):
        if currch == "0":
            if req == "D":
                path = self.paths.app / "resources/0/0D.txt"
            elif req == "S":
                path = self.paths.app / "resources/0/0S.txt"
        if path.exists():
            with open(path, "r") as file:
                ret = [line.strip() for line in file]
                return ret
        elif not path.exists():
            x = ["ERROR"]
            return x
    def rungame(self, widget=None):
        self.gamewindow()
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
def main():
    return WaywardSoul()
