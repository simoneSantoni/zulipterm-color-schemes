"""
COLORS FOR NEONWOLF DARK THEME
-------------------------------
Based on the Base2Tone Meadow Dark color scheme by Bram de Haan.
Duotone theme: slate blue + light lime green.

Color reference:
    https://github.com/atelierbram/Base2Tone-kitty

NOTE: The 16-color codes map to kitty's Meadow palette indices,
not to standard terminal color semantics. For example, 'dark_red'
maps to kitty color1 which displays as #277fbe (a blue) in this theme.
"""
from enum import Enum

from zulipterminal.config.color import color_properties


# fmt: off
class NeonwolfColor(Enum):
    # color          =  16code          256code   24code

    # Backgrounds & darks
    BG_DARK       = 'black           h235      #192834'
    SURFACE       = 'light_green     h236      #223644'
    DARK_ACCENT   = 'yellow          h239      #335166'

    # Mid tones
    MUTED         = 'dark_gray       h60       #3d5e76'
    MID_GRAY      = 'light_blue      h60       #466b86'

    # Foregrounds & lights
    FG            = 'light_gray      h109      #7b9eb7'
    FG_BRIGHT     = 'white           h195      #d1ecff'

    # Blues
    TEAL          = 'dark_red        h31       #277fbe'
    SKY_BLUE      = 'dark_blue       h68       #4299d7'
    CYAN          = 'dark_cyan       h75       #47adf5'
    LIGHT_BLUE    = 'light_magenta   h153      #afddfe'

    # Greens
    DARK_GREEN    = 'light_cyan      h71       #73b234'
    GREEN         = 'dark_green      h107      #80bf40'
    BRIGHT_GREEN  = 'light_red       h113      #8cdd3c'
    LIME          = 'brown           h155      #a6f655'
# fmt: on


DefaultBoldColor = color_properties(NeonwolfColor, "BOLD")
