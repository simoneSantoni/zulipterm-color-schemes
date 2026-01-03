# ubuntu-cs-for-zulipterm

Ubuntu Yaru-inspired color scheme for [Zulip Terminal](https://github.com/zulip/zulip-terminal).

Features the distinctive Ubuntu eggplant background with aubergine accent colors, based on [yaru.nvim](https://github.com/simoneSantoni/yaru.nvim).

## Preview

The theme uses Ubuntu's signature palette:

| Color | Hex | Usage |
|-------|-----|-------|
| Eggplant | `#2C001E` | Background |
| Orange | `#E95420` | Accents, mentions, keywords |
| Aubergine | `#772953` | Headers, bars |
| Gold | `#F99B15` | Sender names, functions |
| Green | `#26A269` | Strings, active users |
| Teal | `#19B6EE` | Links, time, unread |
| Red | `#C7162B` | Errors, starred |

## Installation

Copy the theme files to your zulip-terminal themes directory:

```bash
cp colors_yaru.py ubuntu_yaru_dark.py ~/.local/lib/python3.x/site-packages/zulipterminal/themes/
```

Or if using a conda environment:

```bash
cp colors_yaru.py ubuntu_yaru_dark.py ~/miniconda3/envs/zulip/lib/python3.x/site-packages/zulipterminal/themes/
```

Then run zulip-terminal with:

```bash
zulip-term -t ubuntu_yaru_dark
```

## Files

- `colors_yaru.py` - Color definitions (YaruColor enum)
- `ubuntu_yaru_dark.py` - Theme styles mapping

## License

MIT
