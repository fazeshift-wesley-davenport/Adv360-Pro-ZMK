# Layout images

`gen_cheatsheet.py` reads `config/adv360.keymap` and `apps.json`, writes `layers.json` and `cheatsheet.html` (light, one board per layer).
`gen_wallpaper.py` reads `layers.json` and writes `wallpaper.html`: Base full width and centered, the other layers in pairs below, side margins that survive the 3456x2234 laptop crop.

Render the wallpaper at 6016x3384:

```
python3 tools/gen_cheatsheet.py && python3 tools/gen_wallpaper.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=6016,3384 --screenshot=wallpaper.png "file://$PWD/tools/wallpaper.html"
```

`apps.json`: `bound` = Raycast hotkeys that exist, drawn solid on the App board. `suggested` = mnemonic ideas, drawn dashed. Move a key from `suggested` to `bound` after you add the hotkey in Raycast.
