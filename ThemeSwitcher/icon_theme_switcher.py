import os
from helper import JsonReader, cwd


CONFIG_LOCATION = os.path.join(cwd, "config/gtk-config.json")


class IconThemeSwitcher:
    """Icon theme switcher"""

    def __init__(self, theme) -> None:
        self.theme = theme

    def switch_theme(self):
        """Execute command to change icon theme"""

        command: str = JsonReader(CONFIG_LOCATION).return_json()["commands"]["icon-theme"]
        command = command + self.theme
        os.system(command)
