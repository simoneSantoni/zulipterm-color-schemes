"""
COLORS FOR GITHUB LIGHT THEME
------------------------------
Based on projekt0n/github-nvim-theme (GitHub Light).

Color reference: https://github.com/projekt0n/github-nvim-theme

GitHub Light Palette:
    bg:          #ffffff
    bg_alt:      #f6f8fa
    fg:          #1f2328
    fg_dim:      #57606a
    comment:     #6e7781
    blue:        #0969da
    blue_bright: #218bff
    green:       #1a7f37
    green_bright:#2da44e
    yellow:      #9a6700
    yellow_bright:#bf8700
    orange:      #e8590c
    red:         #cf222e
    purple:      #8250df
    cyan:        #1b7c83
    selection:   #add6ff
    border:      #d0d7de
    disabled:    #8c959f
"""
from enum import Enum

from zulipterminal.config.color import color_properties


# fmt: off

class GitHubLightColor(Enum):
    # color               = 16code          256code    24code

    # Backgrounds
    BG                    = 'white           h231      #ffffff'
    BG_ALT                = 'white           h255      #f6f8fa'
    SELECTION             = 'light_cyan      h153      #add6ff'
    BORDER                = 'light_gray      h252      #d0d7de'

    # Foregrounds
    FG                    = 'black           h235      #1f2328'
    FG_DIM                = 'dark_gray       h240      #57606a'
    COMMENT               = 'dark_gray       h243      #6e7781'
    DISABLED              = 'light_gray      h246      #8c959f'

    # Blues (primary accent)
    BLUE                  = 'dark_blue       h32       #0969da'
    BLUE_BRIGHT           = 'light_blue      h33       #218bff'

    # Greens
    GREEN                 = 'dark_green      h28       #1a7f37'
    GREEN_BRIGHT          = 'dark_green      h35       #2da44e'

    # Yellows
    YELLOW                = 'brown           h136      #9a6700'
    YELLOW_BRIGHT         = 'yellow          h172      #bf8700'

    # Others
    ORANGE                = 'light_red       h166      #e8590c'
    RED                   = 'dark_red        h160      #cf222e'
    PURPLE                = 'dark_magenta    h98       #8250df'
    CYAN                  = 'dark_cyan       h30       #1b7c83'

# fmt: on


DefaultBoldColor = color_properties(GitHubLightColor, "BOLD")
