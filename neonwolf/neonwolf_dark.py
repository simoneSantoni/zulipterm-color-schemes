"""
NEONWOLF DARK
-------------
Based on the Base2Tone Meadow Dark color scheme (Bram de Haan).
Duotone theme using slate blue and light lime green.

For further details on themefiles look at the theme contribution guide.
"""
from pygments.styles.solarized import SolarizedDarkStyle

from zulipterminal.config.color import Background
from zulipterminal.themes.colors_neonwolf import DefaultBoldColor as Color


# fmt: off
STYLES = {
    # style_name      :  foreground                  background
    None              : (Color.FG,                   Background.COLOR),
    'selected'        : (Color.FG_BRIGHT,            Color.DARK_ACCENT),
    'msg_selected'    : (Color.FG_BRIGHT,            Color.DARK_ACCENT),
    'header'          : (Color.FG_BRIGHT,            Color.TEAL),
    'general_narrow'  : (Color.FG_BRIGHT,            Color.TEAL),
    'general_bar'     : (Color.FG,                   Background.COLOR),
    'msg_sender'      : (Color.LIME__BOLD,           Background.COLOR),
    'unread'          : (Color.CYAN,                 Background.COLOR),
    'user_active'     : (Color.BRIGHT_GREEN,         Background.COLOR),
    'user_idle'       : (Color.LIME,                 Background.COLOR),
    'user_offline'    : (Color.FG,                   Background.COLOR),
    'user_inactive'   : (Color.FG,                   Background.COLOR),
    'user_bot'        : (Color.FG,                   Background.COLOR),
    'title'           : (Color.FG_BRIGHT__BOLD,      Background.COLOR),
    'column_title'    : (Color.FG_BRIGHT__BOLD,      Background.COLOR),
    'time'            : (Color.SKY_BLUE,             Background.COLOR),
    'bar'             : (Color.FG_BRIGHT,            Color.MUTED),
    'msg_emoji'       : (Color.LIGHT_BLUE,           Background.COLOR),
    'reaction'        : (Color.LIGHT_BLUE__BOLD,     Background.COLOR),
    'reaction_mine'   : (Color.BG_DARK,              Color.LIGHT_BLUE),
    'msg_heading'     : (Color.BG_DARK__BOLD,        Color.GREEN),
    'msg_math'        : (Color.FG,                   Color.MUTED),
    'msg_mention'     : (Color.LIME__BOLD,           Background.COLOR),
    'msg_link'        : (Color.CYAN,                 Background.COLOR),
    'msg_link_index'  : (Color.CYAN__BOLD,           Background.COLOR),
    'msg_quote'       : (Color.SKY_BLUE,             Background.COLOR),
    'msg_bold'        : (Color.FG_BRIGHT__BOLD,      Background.COLOR),
    'msg_time'        : (Color.BG_DARK,              Color.FG),
    'footer'          : (Color.BG_DARK,              Color.FG),
    'footer_contrast' : (Color.FG_BRIGHT,            Background.COLOR),
    'starred'         : (Color.BRIGHT_GREEN__BOLD,   Background.COLOR),
    'unread_count'    : (Color.LIME,                 Background.COLOR),
    'starred_count'   : (Color.MID_GRAY,             Background.COLOR),
    'table_head'      : (Color.FG_BRIGHT__BOLD,      Background.COLOR),
    'filter_results'  : (Color.BG_DARK,              Color.GREEN),
    'edit_topic'      : (Color.FG_BRIGHT,            Color.MUTED),
    'edit_tag'        : (Color.FG_BRIGHT,            Color.MUTED),
    'edit_author'     : (Color.LIME,                 Background.COLOR),
    'edit_time'       : (Color.SKY_BLUE,             Background.COLOR),
    'current_user'    : (Color.FG_BRIGHT,            Background.COLOR),
    'muted'           : (Color.MID_GRAY,             Background.COLOR),
    'popup_border'    : (Color.FG,                   Background.COLOR),
    'popup_category'  : (Color.CYAN__BOLD,           Background.COLOR),
    'popup_contrast'  : (Color.FG_BRIGHT,            Color.MUTED),
    'popup_important' : (Color.LIME__BOLD,           Background.COLOR),
    'widget_disabled' : (Color.MUTED,                Background.COLOR),
    'area:help'       : (Color.BG_DARK,              Color.GREEN),
    'area:msg'        : (Color.FG_BRIGHT,            Color.TEAL),
    'area:stream'     : (Color.FG_BRIGHT,            Color.DARK_ACCENT),
    'area:error'      : (Color.BG_DARK,              Color.BRIGHT_GREEN),
    'area:user'       : (Color.FG_BRIGHT,            Color.MUTED),
    'search_error'    : (Color.LIME,                 Background.COLOR),
    'task:success'    : (Color.BG_DARK,              Color.GREEN),
    'task:error'      : (Color.BG_DARK,              Color.BRIGHT_GREEN),
    'task:warning'    : (Color.BG_DARK,              Color.SKY_BLUE),
    'ui_code'         : (Color.BG_DARK,              Color.FG),
}

META = {
    'background': Color.BG_DARK,
    'pygments': {
        'styles'    : SolarizedDarkStyle().styles,
        'background': 'h236',
        'overrides' : {
            'c'   : '#3d5e76, italics',    # comments: muted
            'cp'  : '#47adf5',             # preprocessor: cyan
            'cpf' : '#3d5e76',             # preprocessor comment: muted
            'ge'  : '#7b9eb7, italics',    # emphasis: fg
            'gh'  : '#d1ecff, bold',       # heading: bright
            'gu'  : '#7b9eb7, underline',  # subheading: fg
            'gp'  : '#4299d7, bold',       # prompt: sky blue
            'gs'  : '#d1ecff, bold',       # strong: bright
            'err' : '#8cdd3c',             # error: bright green
            'n'   : '#7b9eb7',             # name: fg
            'p'   : '#7b9eb7',             # punctuation: fg
            'w'   : '#7b9eb7',             # whitespace: fg
        }
    }
}
# fmt: on
