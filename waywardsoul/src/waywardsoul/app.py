import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
from toga.constants import Direction

class WaywardSoul(toga.App):
    def startup(self):
        self.main_box = toga.Box()
        self.loadtitlewindow()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()
    def loadtitlewindow(self):
        self.main_box = toga.Box()
        logobox = toga.Box(
            style=Pack(
                flex=1
            )
        )
        titlebox = toga.Box(
            style=Pack(
                flex=1
            )
        )
        titlebox.add(
            toga.Label(
                "Wayward Soul",
                margin=(0,5)
            )
        )
        uppersplit = toga.SplitContainer(
            content=[
                (logobox, 9),
                (titlebox, 1)
            ],
            direction=Direction.HORIZONTAL
        )
        mainbuttons = toga.Box(
            style=Pack(
                flex=1
            )
        )
        ngb = toga.Button(
            "New Game",
            #on_press=self.newgame,
            margin=5
        )
        lgb = toga.Button(
            "Load Game",
            #on_press=self.loadgame,
            margin=5
        )
        cfb = toga.Button(
            "Config",
            #on_press=self.configmenu,
            margin=5
        )
        qtb = toga.Button(
            "Quit",
            #on_press=self.quit,
            margin=5
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
            direction=Direction.HORIZONTAL
        )
        self.main_box.add(
            wholesplit
        )


def main():
    return WaywardSoul()
