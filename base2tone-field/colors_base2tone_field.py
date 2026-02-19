"""
COLORS FOR BASE2TONE FIELD DARK THEME
--------------------------------------
Derived from Base2Tone Field Dark by Bram de Haan.
A duotone theme using teal/turquoise and bright field green.

Color reference: https://github.com/atelierbram/Base2Tone-kitty
"""
from enum import Enum

from zulipterminal.config.color import color_properties


# fmt: off

class Base2ToneFieldColor(Enum):
    # color               = 16code          256code    24code

    # Backgrounds
    BG_DARK               = 'black           h234      #18201e'
    BG_MID                = 'black           h235      #242e2c'

    # Foreground / grays
    FG_MAIN               = 'white           h109      #8ea4a0'
    FG_DIM                = 'dark_gray       h66       #5a6d6a'
    FG_MUTED              = 'light_gray      h244      #667a77'
    FG_SUBTLE             = 'dark_gray       h239      #42524f'

    # Teals (primary accent)
    TEAL                  = 'dark_cyan       h43       #0fbda0'
    TEAL_BRIGHT           = 'dark_cyan       h44       #25d0b4'
    CYAN                  = 'light_cyan      h80       #40ddc3'
    CYAN_BRIGHT           = 'light_cyan      h122      #88f2e0'

    # Greens (secondary accent)
    GREEN                 = 'light_green     h84       #3be381'
    GREEN_BRIGHT          = 'light_green     h85       #55ec94'
    GREEN_SOFT            = 'light_green     h121      #85ffb8'
    GREEN_DARK            = 'dark_green      h29       #00943e'

    # Bright whites
    WHITE_MINT            = 'white           h159      #a8fff1'
    WHITE_PURE            = 'white           h231      #f9fbfa'

# fmt: on


DefaultBoldColor = color_properties(Base2ToneFieldColor, "BOLD")
