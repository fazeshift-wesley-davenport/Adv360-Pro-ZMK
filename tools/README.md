# Layout images

`gen_cheatsheet.py` reads `config/adv360.keymap` and `apps.json`, writes `layers.json` and `cheatsheet.html` (light, one board per layer).
`gen_wallpaper.py` reads `layers.json` and writes `wallpaper.html`: Base full width, then Nav/Sym and App/Fn in pairs. Mod and Qwerty stay in the full cheat sheet but are omitted from the wallpaper. Side margins survive the 3456x2234 laptop crop.
The Solarized background is an SVG drawn by `background()` in `gen_wallpaper.py`, so it renders sharp at full resolution.
Each non-Base board colors its own activation key (Esc for Nav, Enter/Kp for Sym, Del for App, and both Fn keys). The Base board remains uncolored.

`gen_wallpaper.py dark` writes `wallpaper-dark.html` with a Solarized Dark palette (`THEMES` in the script).
`make_dynamic_heic.swift light.png dark.png out.heic` packs both renders into one HEIC with the `apple_desktop:apr` appearance tag, so macOS shows the light frame in Light mode and the dark frame in Dark mode.
`tools/ops wallpaper` runs all of it at 6016x3384.

`apps.json`: `bound` = Raycast hotkeys that exist, drawn solid on the App board. `suggested` = mnemonic ideas, drawn dashed. Move a key from `suggested` to `bound` after you add the hotkey in Raycast.

## ops

`tools/ops` runs the mechanical steps of `../CHECKLIST.md`. Settings in `tools/ops.conf`.

```
tools/ops check              preflight: docker, gh, Chrome, trainer dir, Mod = 3, Qwerty = 1, 76 keys per layer
tools/ops build              Docker: Legacy left + right -> firmware/<ts>-<sha>-left-legacy.uf2, -right.uf2
tools/ops fetch              download firmware-no-clique from the latest green CI run
tools/ops flash left|right   name the file, wait for the drive, verify the half. Prints the cp line; never copies.
tools/ops wallpaper          regenerate the light + dark HTML, render a dynamic HEIC into ~/Pictures, open it
tools/ops wallpaper-install  set the newest rendered wallpaper (HEIC or PNG) on all displays (or pass a path)
tools/ops trainer            copy the keymap into the trainer app, regenerate, build
```
