# Color Schemes for Zulip Terminal

Custom color schemes for [Zulip Terminal](https://github.com/zulip/zulip-terminal).

## Available Schemes

### Meadow Dark

Based on the [Base2Tone Meadow Dark](https://github.com/atelierbram/Base2Tone-kitty) color scheme by Bram de Haan. A duotone theme pairing slate blue with light lime green.

| Color | Hex | Usage |
|-------|-----|-------|
| Dark Navy | `#192834` | Background |
| Slate Blue | `#7b9eb7` | Default text |
| Bright White | `#d1ecff` | Titles, bold text |
| Lime | `#a6f655` | Sender names, mentions, accents |
| Green | `#80bf40` | Message headings, success |
| Cyan | `#47adf5` | Links, unread markers |
| Sky Blue | `#4299d7` | Timestamps, quotes |
| Teal | `#277fbe` | Headers |

Files: `meadow/colors_meadow.py`, `meadow/meadow_dark.py`

### Ubuntu Yaru Dark

Based on [yaru.nvim](https://github.com/simoneSantoni/yaru.nvim) by Simone Santoni. Features the distinctive Ubuntu eggplant background with aubergine accent colors.

| Color | Hex | Usage |
|-------|-----|-------|
| Eggplant | `#2C001E` | Background |
| Orange | `#E95420` | Accents, mentions, keywords |
| Aubergine | `#772953` | Headers, bars |
| Gold | `#F99B15` | Sender names, functions |
| Green | `#26A269` | Strings, active users |
| Teal | `#19B6EE` | Links, time, unread |
| Red | `#C7162B` | Errors, starred |

Files: `yaru/colors_yaru.py`, `yaru/ubuntu_yaru_dark.py`

## Installation

Each scheme has two files: a color definitions file (`colors_*.py`) and a theme file (`*_dark.py`). Both must be copied into the zulip-terminal themes directory and the theme registered in the package.

### 1. Locate the themes directory

The target is `zulipterminal/themes/` inside your zulip-terminal installation. The path depends on how you installed it:

```bash
# pip (user)
~/.local/lib/python3.x/site-packages/zulipterminal/themes/

# pip (system)
/usr/lib/python3.x/site-packages/zulipterminal/themes/

# conda / miniconda
~/miniconda3/envs/<env>/lib/python3.x/site-packages/zulipterminal/themes/

# pipx
~/.local/pipx/venvs/zulip-term/lib/python3.x/site-packages/zulipterminal/themes/
```

You can find the exact path with:

```bash
python -c "import zulipterminal.themes; print(zulipterminal.themes.__path__[0])"
```

### 2. Copy the scheme files

Using Meadow Dark as an example:

```bash
THEMES_DIR=$(python -c "import zulipterminal.themes; print(zulipterminal.themes.__path__[0])")
cp meadow/colors_meadow.py meadow/meadow_dark.py "$THEMES_DIR/"
```

### 3. Register the theme

Edit `$THEMES_DIR/../config/themes.py` (i.e. `zulipterminal/config/themes.py`):

**Add the import** alongside the existing theme imports:

```python
from zulipterminal.themes import (
    gruvbox_dark,
    gruvbox_light,
    meadow_dark,       # <-- add this
    zt_blue,
    zt_dark,
    zt_light,
)
```

**Add the entry** to the `THEMES` dictionary:

```python
THEMES: Dict[str, Any] = {
    "gruvbox_dark": gruvbox_dark,
    "gruvbox_light": gruvbox_light,
    "meadow_dark": meadow_dark,       # <-- add this
    "zt_dark": zt_dark,
    "zt_light": zt_light,
    "zt_blue": zt_blue,
}
```

Repeat for any other scheme (e.g. `ubuntu_yaru_dark` with `colors_yaru`).

### 4. Verify

```bash
zulip-term --list-themes
```

The new theme should appear in the list.

### 5. Use the theme

Pass it on the command line:

```bash
zulip-term --theme meadow_dark --color-depth 24bit
```

Or set it permanently in `~/.zuliprc`:

```ini
[zterm]
theme=meadow_dark
color-depth=24bit
```

## Notes

### Color depth

Each color definition has three columns: 16-color, 256-color, and 24-bit. Use `--color-depth 24bit` for the most accurate rendering. The `256` and `16` modes use approximations that lose fidelity, especially for non-standard palettes.

### 16-color and terminal palette interaction

In 16-color mode, zulip-terminal sends standard color names (e.g. `dark_red`, `light_blue`) which the terminal maps to its own palette. If your terminal uses a non-standard palette (as many themes do), the 16-color fallback names in a scheme are chosen to produce the correct visual result in the *intended* terminal theme, not by their literal color name.

For example, in Meadow Dark, `TEAL` uses the 16-color code `dark_red` because kitty's Meadow palette maps color1 (red) to `#277fbe` (a teal blue). This means **the 16-color mode only looks correct when using the matching terminal color scheme**.

For universal accuracy, use `--color-depth 256` or `--color-depth 24bit`.

### Scheme updates after package upgrades

Reinstalling or upgrading zulip-terminal will overwrite the themes directory. You will need to re-copy the scheme files and re-register them in `themes.py` after each upgrade.

## File Structure

```
.
├── meadow/
│   ├── colors_meadow.py        # MeadowColor enum (palette)
│   └── meadow_dark.py          # STYLES + META (theme mapping)
├── yaru/
│   ├── colors_yaru.py          # YaruColor enum (palette)
│   └── ubuntu_yaru_dark.py     # STYLES + META (theme mapping)
├── README.md
└── LICENSE
```

Each scheme directory contains:

- **`colors_*.py`** -- Color palette as a Python enum. Defines the raw colors with values for 16-color, 256-color, and 24-bit modes.
- **`*_dark.py`** -- Theme mapping. Assigns colors from the palette to each of zulip-terminal's ~56 UI style slots, plus Pygments syntax highlighting overrides.

## License

MIT
