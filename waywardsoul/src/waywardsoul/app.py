import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
from toga.constants import Direction
from pathlib import Path
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
            on_press=self.loadgame,
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
    def loadgame(self, widget):
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
        currch = "1"
        currpt = "1"
        self.dialoguelist = gamedialog.getdialogue()
        print(self.dialoguelist)
class gamedialog:
    def getdialogue():
        if currch == "1":
            if currpt == "1":
                diaglist = [1, 2, 3, 4]
                return diaglist
def main():
    return WaywardSoul()
