# Change checklist

Run this list after every keymap change. Top to bottom. Skip a section only if nothing in it changed.
Each section has a `tools/ops` command that does the mechanical part. Start with `tools/ops check`.

## 1. Keymap

- [ ] Edit `config/adv360.keymap` (bindings) and `config/symbols.dtsi` (macros).
- [ ] Keep Mod at layer index 3 and the Mod layer stock. Keep Qwerty at index 1, below every hold layer.
- [ ] `tools/ops check`: Mod at 3, Qwerty at 1, 76 bindings per layer, tools present.
- [ ] Update `LAYOUT.md` for anything a person needs to know.
- [ ] Commit and push to `fazeshift-wesley-davenport/Adv360-Pro-ZMK`, branch `wesley`.
- [ ] Wait for the Actions run to go green, then `tools/ops fetch`. It downloads **firmware-no-clique** (never the clique one) into `firmware/` and warns if the run is older than your HEAD.
- [ ] Or build locally with Docker Desktop running: `tools/ops build`. Writes `firmware/<ts>-<sha>-left-legacy.uf2` and `-right.uf2`, restores `config/version.dtsi` when done.

## 2. Keyboard

The left half holds the keymap. Reflash the right half only when `config/west.yml` or the board files change.

- [ ] `tools/ops flash left`. It names the newest left file, waits for the drive, and checks the drive really is the left half. It never copies.
- [ ] Plug the **left half** into the Mac with USB-C. Leave its power switch on.
- [ ] Hold **Mod** (top of the right half's inner column) and press the **1** key (below Kp on the left half).
- [ ] A drive named `ADV360PRO` appears in Finder and `ops` prints the `cp` line.
- [ ] Run that `cp`. The drive ejects itself in a second or two. A "disk not ejected properly" warning is normal.
- [ ] Unplug. Switch both halves off. Switch the left on, wait five seconds, switch the right on.
- [ ] Verify:
  - [ ] Hold Mod, press the V cap. The version string types out, ending in the new commit.
  - [ ] Type `asdf` on the caps. Expect `arst`.
  - [ ] Try every key you changed.
- [ ] Bluetooth to the Mac survives a flash. Reconnect only if you also ran a settings reset.

If the key combo does nothing:

- [ ] Paperclip: double-click the reset button under the thumb cluster of that half, where three thumb keys meet. Single click only power-cycles. Drive appears within two seconds.
- [ ] `tools/ops flash <half>` checks which half mounted before printing the copy line. By hand: `strings /Volumes/ADV360PRO/CURRENT.UF2 | grep "Adv360 Pro"`; the right half prints `Adv360 Pro rt`.

If the halves flash red and never link:

- [ ] Settings reset: flash `settings-reset.uf2` onto each half with the paperclip. It runs, wipes settings, and re-enters the bootloader by itself.
- [ ] Then flash the real firmware onto each half. Left gets left, right gets right. Do not automate the copy.
- [ ] Re-pair the Mac: Mod+1 selects profile 1, then connect "Adv360 Pro" in Bluetooth settings.

## 3. Screenshots and wallpaper

- [ ] If Raycast hotkeys changed, edit `tools/apps.json` (`bound` = hotkey exists, `suggested` = idea).
- [ ] `tools/ops wallpaper`. Regenerates the HTML, renders `~/Pictures/adv360-layout-wallpaper-<date>.png` at 6016x3384, opens it.
- [ ] Check nothing is clipped at the right edge and the thumb clusters do not overlap.
- [ ] Set it: System Settings > Wallpaper > Add Photo. A new file name each time, since macOS caches by path.
- [ ] Commit `tools/` changes.

## 4. Trainer website

Repo: `~/GitHub/adv360-trainer` (GitHub: `fazeshift-wesley-davenport/adv360-trainer`).

- [ ] `tools/ops trainer`. Copies the keymap in, runs `pnpm gen:keymap` and `pnpm build`, prints the trainer's git status.
- [ ] New key worth drilling? Add a `pick(...)` line in `src/lib/drills.ts`. New macro? It is picked up automatically.
- [ ] New physical key or moved thumb? Edit `src/data/geometry.ts`.
- [ ] Open `pnpm dev`, check the Keymap page shows the change, run one drill that uses it.
- [ ] Commit and push.

## 5. Raycast

- [ ] App-layer letter added or moved? Raycast > search the app > Cmd+K > Add Hotkey > hold Del and press the letter.
- [ ] Record it in `tools/apps.json` under `bound`.
