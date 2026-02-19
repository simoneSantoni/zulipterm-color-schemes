"""
BASE2TONE FIELD DARK
--------------------
A duotone dark theme using teal/turquoise and bright field green,
derived from Base2Tone Field Dark by Bram de Haan.

For syntax highlighting, this theme uses the solarized dark styles
from pygments with overrides to match the teal/green palette.

For further details on themefiles look at the theme contribution guide
"""

from pygments.styles.solarized import SolarizedDarkStyle

from zulipterminal.config.color import Background
from zulipterminal.themes.colors_base2tone_field import DefaultBoldColor as Color


# fmt: off

STYLES = {
    # style_name       :  foreground                   background
    None               : (Color.FG_MAIN,               Background.COLOR),
    'selected'         : (Color.WHITE_PURE,            Color.FG_SUBTLE),
    'msg_selected'     : (Color.WHITE_PURE,            Color.FG_SUBTLE),
    'header'           : (Color.TEAL,                  Color.BG_MID),
    'general_narrow'   : (Color.WHITE_PURE,            Color.TEAL),
    'general_bar'      : (Color.FG_MAIN,               Background.COLOR),
    'msg_sender'       : (Color.GREEN__BOLD,           Background.COLOR),
    'unread'           : (Color.TEAL_BRIGHT,           Background.COLOR),
    'user_active'      : (Color.GREEN,                 Background.COLOR),
    'user_idle'        : (Color.GREEN_SOFT,            Background.COLOR),
    'user_offline'     : (Color.FG_MAIN,               Background.COLOR),
    'user_inactive'    : (Color.FG_MAIN,               Background.COLOR),
    'user_bot'         : (Color.FG_MAIN,               Background.COLOR),
    'title'            : (Color.WHITE_MINT__BOLD,      Background.COLOR),
    'column_title'     : (Color.WHITE_MINT__BOLD,      Background.COLOR),
    'time'             : (Color.TEAL_BRIGHT,           Background.COLOR),
    'bar'              : (Color.FG_MAIN,               Color.FG_SUBTLE),
    'msg_emoji'        : (Color.CYAN_BRIGHT,           Background.COLOR),
    'reaction'         : (Color.CYAN_BRIGHT__BOLD,     Background.COLOR),
    'reaction_mine'    : (Color.BG_DARK,               Color.CYAN_BRIGHT),
    'msg_heading'      : (Color.BG_DARK__BOLD,         Color.TEAL),
    'msg_math'         : (Color.FG_MAIN,               Color.FG_SUBTLE),
    'msg_mention'      : (Color.GREEN_BRIGHT__BOLD,    Background.COLOR),
    'msg_link'         : (Color.CYAN,                  Background.COLOR),
    'msg_link_index'   : (Color.CYAN__BOLD,            Background.COLOR),
    'msg_quote'        : (Color.FG_DIM,                Background.COLOR),
    'msg_bold'         : (Color.WHITE_MINT__BOLD,      Background.COLOR),
    'msg_time'         : (Color.BG_DARK,               Color.FG_MAIN),
    'footer'           : (Color.BG_DARK,               Color.FG_MUTED),
    'footer_contrast'  : (Color.FG_MAIN,               Background.COLOR),
    'starred'          : (Color.GREEN_SOFT__BOLD,      Background.COLOR),
    'unread_count'     : (Color.GREEN_SOFT,            Background.COLOR),
    'starred_count'    : (Color.FG_MUTED,              Background.COLOR),
    'table_head'       : (Color.WHITE_MINT__BOLD,      Background.COLOR),
    'filter_results'   : (Color.BG_DARK,               Color.GREEN),
    'edit_topic'       : (Color.BG_DARK,               Color.FG_SUBTLE),
    'edit_tag'         : (Color.BG_DARK,               Color.FG_SUBTLE),
    'edit_author'      : (Color.GREEN,                 Background.COLOR),
    'edit_time'        : (Color.TEAL_BRIGHT,           Background.COLOR),
    'current_user'     : (Color.FG_MAIN,               Background.COLOR),
    'muted'            : (Color.FG_DIM,                Background.COLOR),
    'popup_border'     : (Color.FG_MAIN,               Background.COLOR),
    'popup_category'   : (Color.TEAL_BRIGHT__BOLD,     Background.COLOR),
    'popup_contrast'   : (Color.BG_DARK,               Color.FG_SUBTLE),
    'popup_important'  : (Color.GREEN_BRIGHT__BOLD,    Background.COLOR),
    'widget_disabled'  : (Color.FG_SUBTLE,             Background.COLOR),
    'area:help'        : (Color.BG_DARK,               Color.GREEN),
    'area:msg'         : (Color.BG_DARK,               Color.TEAL),
    'area:stream'      : (Color.BG_DARK,               Color.TEAL_BRIGHT),
    'area:error'       : (Color.WHITE_PURE,            Color.GREEN_DARK),
    'area:user'        : (Color.BG_DARK,               Color.CYAN),
    'search_error'     : (Color.GREEN_BRIGHT,          Background.COLOR),
    'task:success'     : (Color.BG_DARK,               Color.GREEN),
    'task:error'       : (Color.WHITE_PURE,            Color.GREEN_DARK),
    'task:warning'     : (Color.BG_DARK,               Color.CYAN),
    'ui_code'          : (Color.BG_DARK,               Color.FG_MAIN),
}

META = {
    'background': Color.BG_DARK,
    'pygments': {
        'styles'    : SolarizedDarkStyle().styles,
        'background': 'h235',
        'overrides' : {
            'c'   : '#5a6d6a, italics',   # comments: FG_DIM
            'cp'  : '#0fbda0',            # preprocessor: TEAL
            'cpf' : '#5a6d6a',            # comment preproc file: FG_DIM
            'ge'  : '#8ea4a0, italics',   # generic emphasis: FG_MAIN
            'gh'  : '#8ea4a0, bold',      # generic heading: FG_MAIN
            'gu'  : '#8ea4a0, underline', # generic underline: FG_MAIN
            'gp'  : '#25d0b4, bold',      # generic prompt: TEAL_BRIGHT
            'gs'  : '#8ea4a0, bold',      # generic strong: FG_MAIN
            'err' : '#55ec94',            # error: GREEN_BRIGHT
            'k'   : '#25d0b4, bold',      # keyword: TEAL_BRIGHT
            'kn'  : '#40ddc3, italics',   # keyword namespace: CYAN
            'n'   : '#8ea4a0',            # name: FG_MAIN
            'p'   : '#8ea4a0',            # punctuation: FG_MAIN
            's'   : '#3be381',            # string: GREEN
            'na'  : '#88f2e0',            # name attribute: CYAN_BRIGHT
            'nb'  : '#40ddc3',            # name builtin: CYAN
            'nf'  : '#3be381',            # name function: GREEN
            'mi'  : '#85ffb8',            # number integer: GREEN_SOFT
            'o'   : '#0fbda0',            # operator: TEAL
            'w'   : '#8ea4a0',            # whitespace: FG_MAIN
        }
    }
}
# fmt: on
