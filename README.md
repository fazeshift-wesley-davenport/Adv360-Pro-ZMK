# Adv360 Pro · wesley

Kinesis Advantage 360 Pro ZMK config. Fork of [KinesisCorporation/Adv360-Pro-ZMK](https://github.com/KinesisCorporation/Adv360-Pro-ZMK) (upstream README: `git show origin/V3.0:README.md`).

## Layout

- Base: Colemak-DH (matrix variant). Layer order `Base 0, Qwerty 1, Fn 2, Mod 3, Sym 4, Nav 5, App 6` + 4 reserved.
- Mod stays at index 3 with the stock layer. Qwerty at 1, below every hold layer, so Mod+Q toggles it off again.
- Thumbs, mirrored, outside → in: Cmd (tap: left ⌘Space, right ⌘K), Opt, Ctrl. Big keys: Bksp Del | Enter Space. Lower column: Esc/hold Nav | Tab/hold Sym. Hold Del = App.
- Home-row mods, mirrored by finger: `A R S T` = Cmd Opt Ctrl Shift, `O I E N` the same. Balanced, 280 ms, quick-tap 175, prior-idle 150, cross-hand + thumbs only (`hold-trigger-key-positions`).
- Inner column: 1 = ⌘C, 2 = ⌘V, 3 = ⌘Tab, 4 = ⌥⌫. Kp = Sym lock. Caps key = caps_word.
- Nav: arrows on N E I O, one direction per column (⌥ word above, ⌘ line / Pg below); inner column tabs + ⌘`; outer column ⌘[ ⌘]; left hand Rectangle chords.
- Sym: left hand TS macros (`=> === !== ?. ?? && || ${} ()[]{}`) in `config/symbols.dtsi`; right hand numpad, 0 on ↑.
- App: every key sends Hyper (⌃⌥⇧⌘) + Colemak letter; Raycast hotkeys open apps. Bound: S C L D Z U T V (`tools/apps.json`).
- Layer thumb keys: tap-preferred, 200 ms, prior-idle 150. Cmd thumbs: hold-preferred, `hold-while-undecided` (+linger).
- Full key-by-key guide: `LAYOUT.md`. Key positions 0-75: `assets/key-positions.md`.

## Firmware

- Build the left half as the **Legacy** variant (no `-S studio-rpc-usb-uart`, no `CONFIG_ZMK_STUDIO=y`). The Studio/Clique build keeps a layer-order table in flash that can hide layers above index 3 (symptom: Mod dead, no LED). CI artifact: `firmware-no-clique`.
- Right half: `-b adv360_right`, no keymap logic. The full flash procedure updates both halves from the same build.
- Flash step by step: disconnect (do not forget) Bluetooth; with USB unplugged, restart both halves left first; plug in and flash left with Mod + the left inner-column `1` key; switch both off; move USB to right; start both left first and flash right with Mod + the right inner-column `3` key; restart both and move USB back to left. Use `tools/ops flash left|right` to verify each mounted `ADV360PRO` drive and print the `cp -X` command. See `CHECKLIST.md` for the full sequence and verification.
- Bootloader fallback: paperclip double-click under the thumb cluster. `strings CURRENT.UF2 | grep "Adv360 Pro"` prints `rt` for the right half.
- Settings reset: flash `settings-reset.uf2` per half (it re-enters the bootloader by itself), then real firmware; re-pair Bluetooth.

## Tools

```
tools/ops check              docker, gh, Chrome, trainer dir, MOD=3, QWERTY=1, 76 keys/layer, pos 7 = Mod
tools/ops build              Docker → firmware/<ts>-<sha>-left-legacy.uf2 + -right.uf2 (restores config/version.dtsi)
tools/ops fetch              gh: firmware-no-clique from the latest green run on branch wesley
tools/ops flash left|right   names the file, waits for the drive, verifies the half, prints the cp. Never copies.
tools/ops wallpaper          gen_cheatsheet.py + gen_wallpaper.py → Chrome headless 6016x3384 → ~/Pictures. Render only.
tools/ops wallpaper-install  set the newest rendered PNG (or a given path) on every display.
tools/ops trainer            copies keymap + symbols into the trainer, pnpm gen:keymap, pnpm build
```

Config: `tools/ops.conf`. Full procedure: `CHECKLIST.md`. Image generators and `apps.json` schema: `tools/README.md`.

## Trainer

React/Vite/Tailwind/shadcn typing trainer driven by this keymap: https://github.com/fazeshift-wesley-davenport/adv360-trainer (`~/GitHub/adv360-trainer`, `pnpm dev`). Letters (Colemak-DH stages, repeat/vocab controls), drills (thumbs, home-row Shift, Nav, Sym), code snippets with next-key + layer hints, live keymap. Sync: `tools/ops trainer`. New keycode → `scripts/gen-keymap.py` `KEY` map.

## Research

`.context/adv360-research/` in the tehran workspace (not committed): 349-fork keymap survey (`modifier-patterns.md`), key-event logger page, wallpaper drafts.
