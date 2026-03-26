"""
GITHUB LIGHT
-------------
GitHub Light theme for Zulip Terminal.
Based on projekt0n/github-nvim-theme.

A clean light theme using GitHub's signature blue accent on
a white background.

For further details on themefiles look at the theme contribution guide.
"""

from pygments.styles.friendly import FriendlyStyle

from zulipterminal.config.color import Background
from zulipterminal.themes.colors_github_light import DefaultBoldColor as Color


# fmt: off

STYLES = {
    # style_name       :  foreground                   background
    None               : (Color.FG,                    Background.COLOR),
    'selected'         : (Color.FG,                    Color.SELECTION),
    'msg_selected'     : (Color.FG,                    Color.SELECTION),
    'header'           : (Color.BG,                    Color.BLUE),
    'general_narrow'   : (Color.BG,                    Color.BLUE),
    'general_bar'      : (Color.FG,                    Background.COLOR),
    'msg_sender'       : (Color.PURPLE__BOLD,          Background.COLOR),
    'unread'           : (Color.BLUE,                  Background.COLOR),
    'user_active'      : (Color.GREEN,                 Background.COLOR),
    'user_idle'        : (Color.YELLOW,                Background.COLOR),
    'user_offline'     : (Color.FG_DIM,                Background.COLOR),
    'user_inactive'    : (Color.COMMENT,               Background.COLOR),
    'user_bot'         : (Color.PURPLE,                Background.COLOR),
    'title'            : (Color.FG__BOLD,              Background.COLOR),
    'column_title'     : (Color.FG__BOLD,              Background.COLOR),
    'time'             : (Color.COMMENT,               Background.COLOR),
    'bar'              : (Color.FG_DIM,                Color.BG_ALT),
    'msg_emoji'        : (Color.YELLOW,                Background.COLOR),
    'reaction'         : (Color.YELLOW__BOLD,          Background.COLOR),
    'reaction_mine'    : (Color.BG,                    Color.YELLOW),
    'msg_heading'      : (Color.BG,                    Color.BLUE),
    'msg_math'         : (Color.FG_DIM,                Color.BG_ALT),
    'msg_mention'      : (Color.ORANGE__BOLD,          Background.COLOR),
    'msg_link'         : (Color.BLUE,                  Background.COLOR),
    'msg_link_index'   : (Color.BLUE__BOLD,            Background.COLOR),
    'msg_quote'        : (Color.COMMENT,               Background.COLOR),
    'msg_bold'         : (Color.FG__BOLD,              Background.COLOR),
    'msg_time'         : (Color.FG_DIM,                Color.BG_ALT),
    'footer'           : (Color.FG_DIM,                Color.BG_ALT),
    'footer_contrast'  : (Color.FG,                    Background.COLOR),
    'starred'          : (Color.RED__BOLD,             Background.COLOR),
    'unread_count'     : (Color.BLUE,                  Background.COLOR),
    'starred_count'    : (Color.COMMENT,               Background.COLOR),
    'table_head'       : (Color.FG__BOLD,              Background.COLOR),
    'filter_results'   : (Color.BG,                    Color.GREEN),
    'edit_topic'       : (Color.FG,                    Color.BG_ALT),
    'edit_tag'         : (Color.FG,                    Color.BG_ALT),
    'edit_author'      : (Color.PURPLE,                Background.COLOR),
    'edit_time'        : (Color.COMMENT,               Background.COLOR),
    'current_user'     : (Color.BLUE,                  Background.COLOR),
    'muted'            : (Color.DISABLED,              Background.COLOR),
    'popup_border'     : (Color.BORDER,                Background.COLOR),
    'popup_category'   : (Color.BLUE__BOLD,            Background.COLOR),
    'popup_contrast'   : (Color.FG,                    Color.BG_ALT),
    'popup_important'  : (Color.RED__BOLD,             Background.COLOR),
    'widget_disabled'  : (Color.DISABLED,              Background.COLOR),
    'area:help'        : (Color.BG,                    Color.GREEN),
    'area:msg'         : (Color.BG,                    Color.YELLOW),
    'area:stream'      : (Color.BG,                    Color.BLUE),
    'area:error'       : (Color.BG,                    Color.RED),
    'area:user'        : (Color.BG,                    Color.ORANGE),
    'search_error'     : (Color.RED,                   Background.COLOR),
    'task:success'     : (Color.BG,                    Color.GREEN),
    'task:error'       : (Color.BG,                    Color.RED),
    'task:warning'     : (Color.BG,                    Color.YELLOW),
    'ui_code'          : (Color.FG,                    Color.BG_ALT),
}

META = {
    'background': Color.BG,
    'pygments': {
        'styles'    : FriendlyStyle().styles,
        'background': 'h231',  # #ffffff
        'overrides' : {
            'c'   : '#6e7781, italics',    # comments
            'cp'  : '#cf222e',              # preprocessor (red)
            'cpf' : '#6e7781',              # comments
            'ge'  : '#1f2328, italics',     # emphasis
            'gh'  : '#1f2328, bold',        # heading
            'gu'  : '#1f2328, underline',   # subheading
            'gp'  : '#0969da, bold',        # prompt (blue)
            'gs'  : '#1f2328, bold',        # strong
            'err' : '#cf222e',              # error (red)
            'n'   : '#1f2328',              # name
            'p'   : '#1f2328',              # punctuation
            'w'   : '#1f2328',              # whitespace
            'k'   : '#cf222e',              # keyword (red)
            'kn'  : '#cf222e, italics',     # keyword namespace
            's'   : '#0a3069',              # string (dark blue)
            'nf'  : '#8250df',              # function name (purple)
            'nc'  : '#e8590c',              # class name (orange)
        }
    }
}
# fmt: on
