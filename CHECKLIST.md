# Change checklist

Run this list after every keymap change. Top to bottom. Skip a section only if nothing in it changed.

## 1. Keymap

- [ ] Edit `config/adv360.keymap` (bindings) and `config/symbols.dtsi` (macros).
- [ ] Keep Mod at layer index 3 and the Mod layer stock. Keep Qwerty at index 1, below every hold layer.
- [ ] Keep 76 bindings per layer. Quick check:
      `python3 tools/gen_cheatsheet.py` fails on a wrong count.
- [ ] Update `LAYOUT.md` for anything a person needs to know.
- [ ] Commit and push to `fazeshift-wesley-davenport/Adv360-Pro-ZMK`, branch `wesley`.
- [ ] Wait for the Actions run to go green. Download the **firmware-no-clique** artifact. Not the clique one.

Local build instead of CI (Docker Desktop running):

```
bin/get_version_local.sh
docker run --rm -v "$PWD/firmware:/app/firmware" -v "$PWD/config:/app/config:ro" zmk bash -c '
  west build -s zmk/app -p -d build/left -b adv360_left -- -DZMK_CONFIG=/app/config &&
  cp build/left/zephyr/zmk.uf2 /app/firmware/left-legacy.uf2'
git checkout config/version.dtsi
```

## 2. Keyboard

The left half holds the keymap. Reflash the right half only when `config/west.yml` or the board files change.

- [ ] Plug the **left half** into the Mac with USB-C. Leave its power switch on.
- [ ] Hold **Mod** (top of the right half's inner column) and press the **1** key (below Kp on the left half).
- [ ] A drive named `ADV360PRO` appears in Finder.
- [ ] Copy the `*-left*.uf2` file onto the drive. It ejects itself in a second or two. A "disk not ejected properly" warning is normal.
- [ ] Unplug. Switch both halves off. Switch the left on, wait five seconds, switch the right on.
- [ ] Verify:
  - [ ] Hold Mod, press the V cap. The version string types out, ending in the new commit.
  - [ ] Type `asdf` on the caps. Expect `arst`.
  - [ ] Try every key you changed.
- [ ] Bluetooth to the Mac survives a flash. Reconnect only if you also ran a settings reset.

If the key combo does nothing:

- [ ] Paperclip: double-click the reset button under the thumb cluster of that half, where three thumb keys meet. Single click only power-cycles. Drive appears within two seconds.
- [ ] If a drive mounts, check which half it is before copying: `strings /Volumes/ADV360PRO/CURRENT.UF2 | grep "Adv360 Pro"`. The right half prints `Adv360 Pro rt`.

If the halves flash red and never link:

- [ ] Settings reset: flash `settings-reset.uf2` onto each half with the paperclip. It runs, wipes settings, and re-enters the bootloader by itself.
- [ ] Then flash the real firmware onto each half. Left gets left, right gets right. Do not automate the copy.
- [ ] Re-pair the Mac: Mod+1 selects profile 1, then connect "Adv360 Pro" in Bluetooth settings.

## 3. Screenshots and wallpaper

- [ ] If Raycast hotkeys changed, edit `tools/apps.json` (`bound` = hotkey exists, `suggested` = idea).
- [ ] Regenerate:
      `python3 tools/gen_cheatsheet.py && python3 tools/gen_wallpaper.py`
- [ ] Render the wallpaper PNG:
      ```
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
        --window-size=6016,3384 --screenshot="$HOME/Pictures/adv360-layout-wallpaper-v2.png" "file://$PWD/tools/wallpaper.html"
      ```
- [ ] Open the PNG and check nothing is clipped at the right edge and the thumb clusters do not overlap.
- [ ] Set it: System Settings > Wallpaper, or
      `osascript -e 'tell application "System Events" to set picture of every desktop to POSIX file "'$HOME'/Pictures/adv360-layout-wallpaper-v2.png"'`
- [ ] Commit `tools/` changes.

## 4. Trainer website

Repo: `~/GitHub/adv360-trainer` (GitHub: `fazeshift-wesley-davenport/adv360-trainer`).

- [ ] Copy the keymap in:
      `cp config/adv360.keymap config/symbols.dtsi ~/GitHub/adv360-trainer/keymap/`
- [ ] `cd ~/GitHub/adv360-trainer && pnpm gen:keymap`
- [ ] New key worth drilling? Add a `pick(...)` line in `src/lib/drills.ts`. New macro? It is picked up automatically.
- [ ] New physical key or moved thumb? Edit `src/data/geometry.ts`.
- [ ] `pnpm exec tsc -b && pnpm build`
- [ ] Open `pnpm dev`, check the Keymap page shows the change, run one drill that uses it.
- [ ] Commit and push.

## 5. Raycast

- [ ] App-layer letter added or moved? Raycast > search the app > Cmd+K > Add Hotkey > hold Del and press the letter.
- [ ] Record it in `tools/apps.json` under `bound`.
