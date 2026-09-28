# Layout images

`gen_cheatsheet.py` reads `config/adv360.keymap` and `apps.json`, writes `layers.json` and `cheatsheet.html` (light, one board per layer).
`gen_wallpaper.py` reads `layers.json` and writes `wallpaper.html`: Base full width, then Nav/Sym and App/Fn in pairs. Mod and Qwerty stay in the full cheat sheet but are omitted from the wallpaper. Side margins survive the 3456x2234 laptop crop.

Render the wallpaper at 6016x3384:

```
python3 tools/gen_cheatsheet.py && python3 tools/gen_wallpaper.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=6016,3384 --screenshot=wallpaper.png "file://$PWD/tools/wallpaper.html"
```

`apps.json`: `bound` = Raycast hotkeys that exist, drawn solid on the App board. `suggested` = mnemonic ideas, drawn dashed. Move a key from `suggested` to `bound` after you add the hotkey in Raycast.

## ops

`tools/ops` runs the mechanical steps of `../CHECKLIST.md`. Settings in `tools/ops.conf`.

```
tools/ops check              preflight: docker, gh, Chrome, trainer dir, Mod = 3, Qwerty = 1, 76 keys per layer
tools/ops build              Docker: Legacy left + right -> firmware/<ts>-<sha>-left-legacy.uf2, -right.uf2
tools/ops fetch              download firmware-no-clique from the latest green CI run
tools/ops flash left|right   name the file, wait for the drive, verify the half. Prints the cp line; never copies.
tools/ops wallpaper          regenerate the HTML, render the PNG into ~/Pictures, open it
tools/ops wallpaper-install  set the newest rendered PNG on all displays (or pass a path)
tools/ops trainer            copy the keymap into the trainer app, regenerate, build
```
