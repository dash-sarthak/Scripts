import os
from helper import JsonReader, replace_line, cwd


CONFIG_LOCATION = os.path.join(cwd, "config/neovim-config.json")


class NvimThemeSwitcher:
    """Neovim Theme Switcher"""

    def __init__(self, theme: str) -> None:
        self.theme = theme
        self.conf = JsonReader(CONFIG_LOCATION).return_json()

    def switch_theme(self):
        """Change Neovim Theme"""

        self.switch_main_theme()
        self.switch_lualine_theme()

    def switch_main_theme(self):
        """Switch the main neovim theme"""

        init_loc = self.conf["init"]["location"]
        line_nr = int(self.conf["init"]["line"])
        theme_command = f"require('colors.{self.theme}')"
        replace_line(init_loc, line_nr, theme_command)

    def switch_lualine_theme(self):
        """Switch the lualine theme"""

        lualine_loc = self.conf["lualine"]["location"]
        line_nr = int(self.conf["lualine"]["line"])

        if self.theme == "material":
            lua_theme_name = "material-stealth"
        else:
            lua_theme_name = self.theme

        theme_command = f"        theme = '{lua_theme_name}',"
        replace_line(lualine_loc, line_nr, theme_command)
