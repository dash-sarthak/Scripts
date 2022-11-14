from helper import JsonReader, cwd
import os


CONFIG_LOCATION = os.path.join(cwd, "config/gtk-config.json")


class GTKThemeSwitcher:
    """GTK Theme Switcher"""

    def __init__(self, theme: str) -> None:
        self.theme: str = theme

    def switch_theme(self):
        """Execute command to change gtk theme"""

        command: str = JsonReader(CONFIG_LOCATION).return_json()["commands"]["gtk-theme"]
        command = command + self.theme
        os.system(command)
