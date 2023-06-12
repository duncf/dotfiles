# -*- coding: utf-8 -*-
# autostart = true

import re
from xkeysnail.transform import *

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = [
    "gnome-terminal",
]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str("^" + x + "$") for x in terminals)

mscodes = ["code", "vscodium"]
mscodes.append("code - insiders")  # duncf
codeStr = "|".join(str("^" + x + "$") for x in mscodes)

# Use for browser specific hotkeys
browsers = [
    "Chromium",
    "Chromium-browser",
    "Firefox",
    "Google-chrome",
]
browsers = [browser.casefold() for browser in browsers]
browserStr = "|".join(str("^" + x + "$") for x in browsers)

chromes = [
    "Brave-browser",
    "Chromium",
    "Chromium-browser",
    "Google-chrome",
    "microsoft-edge",
    "microsoft-edge-dev",
    "org.deepin.browser",
]
chromes = [chrome.casefold() for chrome in chromes]
chromeStr = "|".join(str("^" + x + "$") for x in chromes)

# duncf 2023-05-30
define_modmap(
    {
        # AFAICT, most of the keybindings below assume that the "command key" is
        # bound to Right Ctrl, so bind "Windows key" to Right Ctrl.
        Key.LEFT_META: Key.RIGHT_CTRL,
        Key.CAPSLOCK: Key.LEFT_CTRL,
    }
)


define_keymap(
    re.compile(chromeStr, re.IGNORECASE),
    {
        K("C-comma"): [K("Alt-e"), K("s"), K("Enter")],  # Open preferences
        K("RC-q"): K("Alt-F4"),  # Quit Chrome(s) browsers with Cmd+Q
        # K("RC-Left"):           K("Alt-Left"),            # Page nav: Back to prior page in history (conflict with wordwise)
        # K("RC-Right"):          K("Alt-Right"),           # Page nav: Forward to next page in history (conflict with wordwise)
        K("RC-Left_Brace"): K("Alt-Left"),  # Page nav: Back to prior page in history
        K("RC-Right_Brace"): K(
            "Alt-Right"
        ),  # Page nav: Forward to next page in history
    },
    "Chrome Browsers",
)

# Keybindings for General Web Browsers
define_keymap(
    re.compile(browserStr, re.IGNORECASE),
    {
        K("RC-Q"): K("RC-Q"),  # Close all browsers Instances
        K("Alt-RC-I"): K("RC-Shift-I"),  # Dev tools
        K("Alt-RC-J"): K("RC-Shift-J"),  # Dev tools
        K("RC-Key_1"): K("Alt-Key_1"),  # Jump to Tab #1-#8
        K("RC-Key_2"): K("Alt-Key_2"),
        K("RC-Key_3"): K("Alt-Key_3"),
        K("RC-Key_4"): K("Alt-Key_4"),
        K("RC-Key_5"): K("Alt-Key_5"),
        K("RC-Key_6"): K("Alt-Key_6"),
        K("RC-Key_7"): K("Alt-Key_7"),
        K("RC-Key_8"): K("Alt-Key_8"),
        K("RC-Key_9"): K("Alt-Key_9"),  # Jump to last tab
        # Enable Cmd+Shift+Braces for tab navigation
        K("RC-Shift-Left_Brace"): K("C-Page_Up"),  # Go to prior tab
        K("RC-Shift-Right_Brace"): K("C-Page_Down"),  # Go to next tab
        # Enable Cmd+Option+Left/Right for tab navigation
        K("RC-Alt-Left"): K("C-Page_Up"),  # Go to prior tab
        K("RC-Alt-Right"): K("C-Page_Down"),  # Go to next tab
        # Enable Ctrl+PgUp/PgDn for tab navigation
        K("Super-Page_Up"): K("C-Page_Up"),  # Go to prior tab
        K("Super-Page_Down"): K("C-Page_Down"),  # Go to next tab
        # Use Cmd+Braces keys for tab navigation instead of page navigation
        # K("C-Left_Brace"): K("C-Page_Up"),
        # K("C-Right_Brace"): K("C-Page_Down"),
    },
    "General Web Browsers",
)

# Note: terminals extends to remotes as well
define_keymap(
    lambda wm_class: wm_class.casefold() not in terminals,
    {
        K("RC-Dot"): K("Esc"),  # Mimic macOS Cmd+dot = Escape key (not in terminals)
    },
)

# Special overrides for terminals for shortcuts that conflict with General GUI block below.
define_keymap(
    re.compile(termStr, re.IGNORECASE),
    {
        K("Alt-Backspace"): K(
            "Alt-Shift-Backspace"
        ),  # Wordwise delete word left of cursor in terminals
        K("Alt-Delete"): [
            K("Esc"),
            K("d"),
        ],  # Wordwise delete word right of cursor in terminals
        K("RC-Backspace"): K("C-u"),  # Wordwise delete line left of cursor in terminals
        K("RC-Delete"): K("C-k"),  # Wordwise delete line right of cursor in terminals
        ### Tab navigation
        K("RC-Shift-Left"): K("C-Page_Up"),  # Tab nav: Go to prior tab (Left)
        K("RC-Shift-Right"): K("C-Page_Down"),  # Tab nav: Go to next tab (Right)
    },
    "Special overrides for terminals",
)

define_keymap(
    lambda wm_class: wm_class.casefold() in mscodes,
    {
        # duncf
        # From terminal section below. Might make sense to limit to vscode.
        K("RC-Z"): K("C-Shift-Z"),
        K("RC-Y"): K("C-Shift-Y"),
        K("RC-V"): K("C-Shift-V"),
        K("RC-X"): K("C-Shift-X"),
        K("RC-C"): K("C-Shift-C"),
        K("RC-V"): K("C-Shift-V"),
    },
)

define_keymap(
    lambda wm_class: wm_class.casefold() not in mscodes,
    {
        # Wordwise remaining - for Everything but VS Code
        K("Alt-Left"): K("C-Left"),  # Left of Word
        K("Alt-Shift-Left"): K("C-Shift-Left"),  # Select Left of Word
        K("Alt-Right"): K("C-Right"),  # Right of Word
        K("Alt-Shift-Right"): K("C-Shift-Right"),  # Select Right of Word
        K("Alt-Shift-g"): K("C-Shift-g"),  # View source control
        # ** VS Code fix **
        #   Electron issue precludes normal keybinding fix.
        #   Alt menu auto-focus/toggle gets in the way.
        #
        #   refer to ./xkeysnail-config/vscode_keybindings.json
        # **
        #
        # ** Firefox fix **
        #   User will need to set "ui.key.menuAccessKeyFocuses"
        #   under about:config to false.
        #
        #   https://superuser.com/questions/770301/pentadactyl-how-to-disable-menu-bar-toggle-by-alt
        # **
        #
    },
    "Wordwise - not vscode",
)

# Keybindings for VS Code
define_keymap(
    re.compile(codeStr, re.IGNORECASE),
    {
        K("Super-Space"): K("LC-Space"),  # Basic code completion
        # Wordwise remaining - for VS Code
        # Alt-F19 hack fixes Alt menu activation
        K("Alt-Left"): [K("Alt-F19"), K("C-Left")],  # Left of Word
        K("Alt-Right"): [K("Alt-F19"), K("C-Right")],  # Right of Word
        K("Alt-Shift-Left"): [K("Alt-F19"), K("C-Shift-Left")],  # Select Left of Word
        K("Alt-Shift-Right"): [
            K("Alt-F19"),
            K("C-Shift-Right"),
        ],  # Select Right of Word
        # K("C-PAGE_DOWN"):         pass_through_key,             # cancel next_view
        # K("C-PAGE_UP"):           pass_through_key,             # cancel prev_view
        K("C-Alt-Left"): K("C-PAGE_UP"),  # next_view
        K("C-Alt-Right"): K("C-PAGE_DOWN"),  # prev_view
        K("RC-Shift-Left_Brace"): K("C-PAGE_UP"),  # next_view
        K("RC-Shift-Right_Brace"): K("C-PAGE_DOWN"),  # prev_view
        # VS Code Shortcuts
        K("C-g"): pass_through_key,  # cancel Go to Line...
        K("Super-g"): K("C-g"),  # Go to Line...
        K("F3"): pass_through_key,  # cancel Find next
        K("C-h"): pass_through_key,  # cancel replace
        K("C-Alt-f"): K("C-h"),  # replace
        K("C-Shift-h"): pass_through_key,  # cancel replace_next
        K("C-Alt-e"): K("C-Shift-h"),  # replace_next
        K("f3"): pass_through_key,  # cancel find_next
        K("C-g"): K("f3"),  # find_next
        K("Shift-f3"): pass_through_key,  # cancel find_prev
        K("C-Shift-g"): K("Shift-f3"),  # find_prev
        # K("Super-c"): K("LC-c"),                    # Default - Terminal - Sigint
        # K("Super-x"): K("LC-x"),                    # Default - Terminal - Exit nano
        # K("Alt-c"): K("LC-c"),                        #  Chromebook/IBM - Terminal - Sigint
        # K("Alt-x"): K("LC-x"),                        #  Chromebook/IBM - Terminal - Exit nano
        # K("Super-C-g"): K("C-f2"),                  # Default - Sublime - find_all_under
        # K("C-Alt-g"): K("C-f2"),                      # Chromebook/IBM - Sublime - find_all_under
        # K("Super-Shift-up"): K("Alt-Shift-up"),       # multi-cursor up - Sublime
        # K("Super-Shift-down"): K("Alt-Shift-down"),   # multi-cursor down - Sublime
        # K(""): pass_through_key,                    # cancel
        # K(""): K(""),                               #
    },
    "Code",
)

define_keymap(
    re.compile(termStr, re.IGNORECASE),
    {
        K("LC-RC-f"): K("Alt-F10"),  # Toggle window maximized state
        # K("RC-Grave"): K("Super-Tab"),                # xfce4 Switch within app group
        # K("RC-Shift-Grave"): K("Super-Shift-Tab"),    # xfce4 Switch within app group
        # K("LC-Right"):K("C-Alt-Right"),                 # Default SL - Change workspace (budgie)
        # K("LC-Left"):K("C-Alt-Left"),                   # Default SL - Change workspace (budgie)
        # K("LC-Left"):K("C-Alt-End"),                    # SL - Change workspace xfce4
        # K("LC-Left"):K("Super-Left"),                 # SL - Change workspace eos
        # K("LC-Right"):K("C-Alt-Home"),                  # SL - Change workspace xfce4
        # K("LC-Right"):K("Super-Right"),               # SL - Change workspace eos
        # K("LC-Right"):K("Super-Page_Up"),             # SL - Change workspace (ubuntu/fedora)
        # K("LC-Left"):K("Super-Page_Down"),            # SL - Change workspace (ubuntu/fedora)
        # K("LC-Right"):K("Super-C-Up"),                # SL - Change workspace (popos)
        # K("LC-Left"):K("Super-C-Down"),               # SL - Change workspace (popos)
        # Ctrl Tab - In App Tab Switching
        K("LC-Tab"): K("LC-PAGE_DOWN"),
        K("LC-Shift-Tab"): K("LC-PAGE_UP"),
        K("LC-Grave"): K("LC-PAGE_UP"),
        # K("Alt-Tab"): pass_through_key,                 # Default - Cmd Tab - App Switching Default
        # K("RC-Tab"): K("Alt-Tab"),                      # Default - Cmd Tab - App Switching Default
        # K("RC-Shift-Tab"): K("Alt-Shift-Tab"),          # Default - Cmd Tab - App Switching Default
        # Converts Cmd to use Ctrl-Shift
        K("RC-MINUS"): K("C-MINUS"),
        K("RC-EQUAL"): K("C-Shift-EQUAL"),
        K("RC-BACKSPACE"): K("C-Shift-BACKSPACE"),
        K("RC-W"): K("C-Shift-W"),
        K("RC-E"): K("C-Shift-E"),
        K("RC-R"): K("C-Shift-R"),
        K("RC-T"): K("C-Shift-t"),
        K("RC-Y"): K("C-Shift-Y"),
        K("RC-U"): K("C-Shift-U"),
        K("RC-I"): K("C-Shift-I"),
        K("RC-O"): K("C-Shift-O"),
        K("RC-P"): K("C-Shift-P"),
        K("RC-LEFT_BRACE"): K("C-Shift-LEFT_BRACE"),
        K("RC-RIGHT_BRACE"): K("C-Shift-RIGHT_BRACE"),
        K("RC-Shift-Left_Brace"): K("C-Page_Up"),  # Go to prior tab (Left)
        K("RC-Shift-Right_Brace"): K("C-Page_Down"),  # Go to next tab (Right)
        K("RC-A"): K("C-Shift-A"),
        K("RC-S"): K("C-Shift-S"),
        K("RC-D"): K("C-Shift-D"),
        K("RC-F"): K("C-Shift-F"),
        K("RC-G"): K("C-Shift-G"),
        K("RC-H"): K("C-Shift-H"),
        K("RC-J"): K("C-Shift-J"),
        K("RC-K"): K("C-Shift-K"),
        K("RC-L"): K("C-Shift-L"),
        K("RC-SEMICOLON"): K("C-Shift-SEMICOLON"),
        K("RC-APOSTROPHE"): K("C-Shift-APOSTROPHE"),
        K("RC-GRAVE"): K("C-Shift-GRAVE"),
        K("RC-Z"): K("C-Shift-Z"),
        K("RC-X"): K("C-Shift-X"),
        K("RC-C"): K("C-Shift-C"),
        K("RC-V"): K("C-Shift-V"),
        K("RC-B"): K("C-Shift-B"),
        K("RC-N"): K("C-Shift-N"),
        K("RC-M"): K("C-Shift-M"),
        K("RC-COMMA"): K("C-Shift-COMMA"),
        K("RC-Dot"): K("LC-c"),
        K("RC-SLASH"): K("C-Shift-SLASH"),
        K("RC-KPASTERISK"): K("C-Shift-KPASTERISK"),
    },
    "terminals",
)
