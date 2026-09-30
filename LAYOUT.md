# Wesley's layout

Seven layers. The Kinesis LED shows the highest active layer. Mod and Fn keep their stock Kinesis indexes and colors.

| # | Layer | Trigger | LED |
|---|-------|---------|-----|
| 0 | Base (Colemak-DH) | | off |
| 1 | Qwerty | Mod+Q toggles it on and off. Resets to Colemak-DH on power cycle | white |
| 2 | Fn | hold either outer bottom pinky key (stock) | blue |
| 3 | Mod | hold the top inner key on the right half (stock, untouched) | green |
| 4 | Sym | hold the right lower thumb key (tap = Tab), or tap the stock Kp key (top row, innermost on the left half) to lock | red |
| 5 | Nav | hold the left lower thumb key (tap = Esc) | purple |
| 6 | App | hold Del (left big thumb key) | cyan |

## Base: Colemak-DH

```
 q w f p b     j l u y ;
 a r s t g     m n e i o
 z x c d v     k h , . /
```

Letters below refer to the Colemak-DH key, then the physical Qwerty cap in parentheses where they differ.

## Thumb clusters (mirrored)

```
 left                      right
   Cmd   Opt           Opt   Cmd
 Bksp Del  Ctrl       Ctrl  Enter Space
           Esc/Nav    Tab/Sym
```

Cmd sits on the outer top key of each side, the easier reach. Opt on the inner top key. Ctrl on the upper column key.

Both Cmd keys are hold-taps. Hold = Cmd. Tap left Cmd = Cmd+Space (Raycast). Tap right Cmd = Cmd+K (Slack quick switcher, Linear command menu, Cursor inline edit). Terminal.app treats Cmd+K as clear scrollback, so a missed hold there wipes the screen. Change the tap to something else if that bites. Hold Cmd and press Space still gives Cmd+Space. Cmd+click and Cmd+drag work because the behavior sets `hold-while-undecided`.

## Home-row mods

Hold a home-row key and it becomes a modifier. Tap it and it types the letter.

```
 A     R    S   T          N   E   I    O
 Shift Ctrl Opt Cmd        Cmd Opt Ctrl Shift
```

Rules that keep typing clean ("timeless" home-row mods):

- A hold only counts when the next key is on the other hand or a thumb. Same-hand rolls like `st` or `ne` always type letters.
- 280 ms tapping term, 175 ms quick-tap (tap then hold repeats the letter), 150 ms prior-idle guard.
- Same-hand shortcuts still need the thumb modifiers: Cmd+C, Cmd+V, Cmd+Z, Cmd+A are all left-hand letters, so use a thumb Cmd or the copy/paste keys beside B and G.
- The Qwerty overlay uses the same finger order on A S D F and J K L ;.

## Inner-column keys (the ones capped 1, 2, 3, 4)

Index-finger stretch keys beside B, G, J and M. Taps, not letters.

- `1` (beside B) = copy, Cmd+C
- `2` (beside G) = paste, Cmd+V
- `3` (beside J) = previous app, a single Cmd+Tab
- `4` (beside M) = delete word, Opt+Backspace

Copy and paste sit on the left so they work while the right hand is on the mouse. Mod+1 and Mod+3 are still the bootloader keys, since that lives in the Mod layer.

## Nav (hold Esc)

Right hand, one direction per column. Home keys `N E I O` are the arrows. Index = ↑ and middle = ↓, the same fingers as the base-layer arrow keys.

| | `N` col | `E` col | `I` col | `O` col |
|---|---|---|---|---|
| row above | doc top (Cmd+↑) | doc end (Cmd+↓) | word left (Opt+←) | word right (Opt+→) |
| home | ↑ | ↓ | ← | → |
| row below | PgUp | PgDn | line start (Cmd+←) | line end (Cmd+→) |

Inner column `M`: previous tab, next tab, next window of the app (Cmd+`), top to bottom.
Outer column: `\` = back (Cmd+[), `'` = forward (Cmd+]).

Thumb modifiers stay active, so Shift+arrow selects.

Left hand, window controls:

- `R` (S cap) previous display (Cmd+Opt+←), `S` (D cap) maximize (Cmd+Opt+Return), `T` (F cap) next display (Cmd+Opt+→)
- `C` (C cap) macOS Full Screen (Ctrl+Cmd+F), `F` (E cap) restore
- `Q` next window of the app (Cmd+`), `B` (T cap) Mission Control

Maximize sends Rectangle's Cmd+Opt+Return. Full Screen sends macOS's native Control+Command+F. Restore keeps Ctrl+Opt+Backspace; display moves keep the Cmd+Opt arrow shortcuts.

## Sym (hold Tab)

Left hand, TypeScript:

- `Q W F P` (QWER caps) = `()` `[]` `{}` `${}` with the cursor placed inside
- `B` (T cap) = backtick
- `A R S T G` (ASDFG caps) = `=>` `===` `!==` `?.` `??`
- `Z X C D V` (ZXCVB caps) = `&&` `||` `<` `>` `~`
- `Esc` = `_`

Right hand numpad (physical caps): `U I O` 7 8 9, `J K L` 4 5 6, `M , .` 1 2 3, ↑ = 0, ↓ = `.`, `Y` = `-`, `P` = `+`, `\` = `*`, `H` = `=`, `N` = `/`, `;` = `:`, `'` = `"`, `/` = `%`.

## App (hold Del)

Every letter, digit, arrow, Enter, and Space sends Hyper (Ctrl+Opt+Shift+Cmd) plus the Colemak-DH letter under it, so Hyper+S is the key that types S. The Qwerty toggle sits below the App layer, so Hyper letters follow Colemak positions either way.

Holding Del for the layer means Del does not auto-repeat from a cold hold. Tap Del, then hold it again within 175 ms, and it repeats. Bind targets in Raycast under Settings > Extensions > Applications, or as Raycast hotkeys:

Bound in Raycast (solid on the wallpaper):

| Key | Target |
|-----|--------|
| Hyper+S | Slack |
| Hyper+C | Google Chrome |
| Hyper+L | Linear |
| Hyper+D | Conductor |
| Hyper+Z | Zed |
| Hyper+U | Cursor |
| Hyper+T | Terminal |
| Hyper+V | Clipboard History |

Suggested, not bound yet (dashed on the wallpaper). Each follows the letter the key types:

| Key | Target |
|-----|--------|
| Hyper+F | Finder |
| Hyper+N | Notion |
| Hyper+P | Postman |
| Hyper+A | Claude |
| Hyper+G | ChatGPT |
| Hyper+B | Bitwarden |
| Hyper+Q | TablePlus |
| Hyper+M | Messages |
| Hyper+E | Mail |
| Hyper+K | Calendar |
| Hyper+O | OpenCode |
| Hyper+X | VS Code |
| Hyper+H | GitHub Desktop |
| Hyper+Space | Raycast root search |
| Hyper+, | Raycast emoji picker |
| Hyper+. | Raycast snippets |
| Hyper+; | System Settings |

Free: `W R I J Y` and the digits. The list lives in `tools/apps.json`; move a key to `bound` after you add the hotkey.

## Fn

F-keys on the top row in the stock Kinesis order: F1 on `=`, F2 to F6 on `1` to `5`, F7 to F11 on `6` to `0`, F12 on `-`. `W F` (WE caps) brightness. `L U Y` (UIO caps) previous, play/pause, next. `N E I` (JKL caps) mute, volume down, volume up. Old Caps key = Caps Lock. The base Caps key is Caps Word: type one ALL_CAPS identifier, it turns off at the first space.

After any change, walk `CHECKLIST.md`: keymap, keyboard, wallpaper, trainer, Raycast.

## Build and flash

1. Push to GitHub. Actions builds `firmware-no-clique` (use this) and `firmware-clique`.
2. Local: `make` (Docker), output in `firmware/`.
3. Follow the step-by-step two-half procedure in `CHECKLIST.md`: disconnect Bluetooth without forgetting the pairing; restart both halves with USB unplugged; plug in and flash left using Mod + the inner-column `1` key below Kp (Kinesis "macro1", position 20); switch both off and move USB to right; restart both and flash right using Mod + the inner-column `3` key below Mod ("macro3", position 21); restart both and move USB back to left. `tools/ops flash left|right` checks the mounted half and prints the `cp -X` command. Fallback: paperclip double-click the reset button under that half's thumb cluster.

The left half is built as the Kinesis Legacy variant (no Clique/Studio). Clique needs the Studio build, which keeps a layer-order table in flash that can hide layers above index 3.

## Timing

Layer keys use the tap-preferred hold-tap flavor, 200 ms tapping term, 175 ms quick tap, 150 ms prior-idle guard. A fast roll from Esc, Tab, or Del into a letter stays a tap. If a layer key produces a tap when you meant hold, lower `tapping-term-ms` in `config/adv360.keymap`. If it produces a hold while you type fast, raise it.
