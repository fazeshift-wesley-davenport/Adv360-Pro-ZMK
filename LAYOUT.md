# Wesley's layout

Six layers. The Kinesis LED shows the highest active layer.

| # | Layer | Trigger | LED |
|---|-------|---------|-----|
| 0 | Base | | off |
| 1 | Nav | hold the left lower thumb key (tap = Esc) | white |
| 2 | Sym | hold the right lower thumb key (tap = Tab), or tap the top-left key to lock | blue |
| 3 | App | hold Del (left big thumb key) | green |
| 4 | Fn | hold either outer bottom pinky key | red |
| 5 | Mod | hold the top inner key on the right half | purple |

## Thumb clusters (mirrored)

```
 left                      right
   Opt   Cmd           Cmd   Opt
 Bksp Del  Ctrl       Ctrl  Enter Space
           Esc/Nav    Tab/Sym
```

Cmd sits on the inner top key of each side. Opt on the outer top key. Ctrl on the upper column key.

## Nav (hold Esc)

Right hand:

- `H J K L` = ← ↓ ↑ →
- `Y U I O P` = line start, word left, PgUp, word right, line end
- `\` = Home, `'` = End
- `N M` = previous tab, next tab (Ctrl+Shift+Tab, Ctrl+Tab)
- `,` = PgDn, `.` = back (Cmd+[), `/` = forward (Cmd+])

Thumb modifiers stay active, so Shift+arrow selects and Cmd+K is document top.

Left hand, Rectangle:

- `A` previous display (Cmd+Opt+←), `G` next display (Cmd+Opt+→)
- `S` left half, `F` right half, `D` maximize (Cmd+Opt+Return)
- `W` top half, `X` bottom half, `C` center, `E` restore
- `Q` next window of the app (Cmd+`), `T` Mission Control

Halves, center, and restore use Rectangle's default Ctrl+Opt chords. Check they are enabled in Rectangle preferences.

## Sym (hold Tab)

Left hand, TypeScript:

- `Q W E R` = `()` `[]` `{}` `${}` with the cursor placed inside
- `T` = backtick
- `A S D F G` = `=>` `===` `!==` `?.` `??`
- `Z X C V B` = `&&` `||` `<` `>` `~`
- `Esc` = `_`

Right hand numpad: `U I O` 7 8 9, `J K L` 4 5 6, `M , .` 1 2 3, Space and ↑ = 0, ↓ = `.`, `Y` = `-`, `P` = `+`, `\` = `*`, `H` = `=`, `N` = `/`, `;` = `:`, `'` = `"`, `/` = `%`.

## App (hold Del)

Every letter, digit, arrow, Enter, and Space sends Hyper (Ctrl+Opt+Shift+Cmd) plus itself. The keyboard never changes. Bind targets in Raycast under Settings > Extensions > Applications, or as Raycast hotkeys:

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

F1 to F12 on the top row. `W E` brightness. `U I O` previous, play/pause, next. `J K L` mute, volume down, volume up. Old Caps key = Caps Lock. The base Caps key is Caps Word: type one ALL_CAPS identifier, it turns off at the first space.

## Build and flash

1. Push to GitHub. Actions builds `firmware-clique` (for boards on the Feb 2025 firmware) and `firmware-no-clique`.
2. Local: `make` (Docker), output in `firmware/`.
3. Flash left: USB, Mod+macro1 (Mod + the key at position 65... see README), copy `*-left*.uf2`. Power cycle both. Flash right the same way with Mod+macro3.

## Timing

Layer keys use the balanced hold-tap flavor, 200 ms tapping term, 175 ms quick tap. If a layer key produces a tap when you meant hold, lower `tapping-term-ms` in `config/adv360.keymap`. If it produces a hold while you type fast, raise it.
