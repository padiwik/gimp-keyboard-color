#!/usr/bin/env python2

from gimpfu import *

# DEFAULT_COLOR = gimpcolor.RGB(255, 0, 0) # red

colors = {
    "a": (160, 160, 160),  # gray
    "b": (0, 0, 255),  # blue
    "c": (0, 255, 255),  # cyan
    "g": (0, 255, 0),  # green
    "i": (255, 160, 160),  # pink
    "k": (0, 0, 0),  # black
    "l": (160, 255, 0),  # lime
    "m": (255, 0, 255),  # magenta
    "n": (160, 80, 0),  # brown
    "o": (255, 160, 0),  # orange
    "p": (160, 0, 160),  # purple
    "r": (255, 0, 0),  # red
    "s": (160, 160, 255),  # sky blue?
    "t": (0, 160, 160),  # teal
    "w": (255, 255, 255),  # white
    "y": (255, 255, 0),  # yellow
}


def color_set(shortkey):
    newColor = colors.get(shortkey)
    if newColor:
        gimp.set_foreground(newColor)
    else:
        pdb.gimp_message("Invalid shortkey.")


register(
    "python_fu_keyboard_color_select_fg",
    "Keyboard Color Selection",
    "Select the foreground color with your keyboard.",
    "padiwik",
    "MIT License",
    "2020",
    "Color Select Foreground",
    "*",
    [
        (PF_STRING, "shortkey", "Short key", "r"),
    ],
    [],
    color_set,
    menu="<Image>/Colors",
)

main()
