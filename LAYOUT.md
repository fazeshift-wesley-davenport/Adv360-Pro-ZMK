# Wesley's layout

Seven layers. The Kinesis LED shows the highest active layer.

| # | Layer | Trigger |
|---|-------|---------|
| 0 | Base (Colemak-DH) | |
| 1 | Qwerty | Mod+Q toggles it on and off. Resets to Colemak-DH on power cycle |
| 2 | Nav | hold the left lower thumb key (tap = Esc) |
| 3 | Sym | hold the right lower thumb key (tap = Tab), or tap the top-left key to lock |
| 4 | App | hold Del (left big thumb key) |
| 5 | Fn | hold either outer bottom pinky key |
| 6 | Mod | hold the top inner key on the right half |

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
   Opt   Cmd           Cmd   Opt
 Bksp Del  Ctrl       Ctrl  Enter Space
           Esc/Nav    Tab/Sym
```

Cmd sits on the inner top key of each side. Opt on the outer top key. Ctrl on the upper column key.

Both Cmd keys are hold-taps. Hold = Cmd. Tap left Cmd = Cmd+Space (Raycast). Tap right Cmd = Cmd+K (command palette in Slack, Linear, Zed, Cursor). Hold Cmd and press Space still gives Cmd+Space. Cmd+click and Cmd+drag work because the behavior sets `hold-while-undecided`.

## Nav (hold Esc)

Right hand:

- `M N E I` (HJKL caps) = ← ↓ ↑ →
- `J L U Y ;` (YUIOP caps) = line start, word left, PgUp, word right, line end
- `\` = Home, `'` = End
- `K H` (NM caps) = previous tab, next tab (Ctrl+Shift+Tab, Ctrl+Tab)
- `,` = PgDn, `.` = back (Cmd+[), `/` = forward (Cmd+])

Thumb modifiers stay active, so Shift+arrow selects and Cmd+K is document top.

Left hand, Rectangle:

- `A` previous display (Cmd+Opt+←), `G` next display (Cmd+Opt+→)
- `R` (S cap) left half, `T` (F cap) right half, `S` (D cap) maximize (Cmd+Opt+Return)
- `W` top half, `X` bottom half, `C` center, `F` (E cap) restore
- `Q` next window of the app (Cmd+`), `B` (T cap) Mission Control

Halves, center, and restore use Rectangle's default Ctrl+Opt chords. Check they are enabled in Rectangle preferences.

## Sym (hold Tab)

Left hand, TypeScript:

- `Q W F P` (QWER caps) = `()` `[]` `{}` `${}` with the cursor placed inside
- `B` (T cap) = backtick
- `A R S T G` (ASDFG caps) = `=>` `===` `!==` `?.` `??`
- `Z X C D V` (ZXCVB caps) = `&&` `||` `<` `>` `~`
- `Esc` = `_`

Right hand numpad (physical caps): `U I O` 7 8 9, `J K L` 4 5 6, `M , .` 1 2 3, Space and ↑ = 0, ↓ = `.`, `Y` = `-`, `P` = `+`, `\` = `*`, `H` = `=`, `N` = `/`, `;` = `:`, `'` = `"`, `/` = `%`.

## App (hold Del)

Every letter, digit, arrow, Enter, and Space sends Hyper (Ctrl+Opt+Shift+Cmd) plus the Colemak-DH letter under it, so Hyper+S is the key that types S. With the Qwerty toggle on, the App layer still uses Colemak positions. Bind targets in Raycast under Settings > Extensions > Applications, or as Raycast hotkeys:

| Key | Target |
|-----|--------|
| Hyper+S | Slack |
| Hyper+C | Google Chrome |
| Hyper+L | Linear |
| Hyper+D | Conductor |
| Hyper+Z | Zed |
| Hyper+U | Cursor |
| Hyper+T | iTerm |
| Hyper+F | Finder |
| Hyper+Space | Raycast root search (optional) |

## Fn

F1 to F12 on the top row. `W F` (WE caps) brightness. `L U Y` (UIO caps) previous, play/pause, next. `N E I` (JKL caps) mute, volume down, volume up. Old Caps key = Caps Lock. The base Caps key is Caps Word: type one ALL_CAPS identifier, it turns off at the first space.

## Build and flash

1. Push to GitHub. Actions builds `firmware-clique` (for boards on the Feb 2025 firmware) and `firmware-no-clique`.
2. Local: `make` (Docker), output in `firmware/`.
3. Flash left: USB, Mod+macro1 (Mod + the key at position 65... see README), copy `*-left*.uf2`. Power cycle both. Flash right the same way with Mod+macro3.

## Timing

Layer keys use the balanced hold-tap flavor, 200 ms tapping term, 175 ms quick tap. If a layer key produces a tap when you meant hold, lower `tapping-term-ms` in `config/adv360.keymap`. If it produces a hold while you type fast, raise it.
