import json, html, os
HERE=os.path.dirname(os.path.abspath(__file__))
W,H=3008,1692          # logical size of the main display; rendered at zoom 2 -> 6016x3384
SAFE=200               # side margin: the 3456x2234 laptop screen crops ~195px per side when it fills the height
layers={l['name']:l['keys'] for l in json.load(open(os.path.join(HERE,'layers.json')))}
L_rows=[[0,1,2,3,4,5,6],[14,15,16,17,18,19,20],[28,29,30,31,32,33,34],[46,47,48,49,50,51],[60,61,62,63,64]]
R_rows=[[7,8,9,10,11,12,13],[21,22,23,24,25,26,27],[39,40,41,42,43,44,45],[54,55,56,57,58,59],[71,72,73,74,75]]
ACCENT={'Base':'#9aa4b2','Nav':'#c084fc','Sym':'#f87171','App':'#22d3ee','Fn':'#60a5fa','Mod':'#4ade80','Qwerty':'#e5e7eb'}
LED={'Base':'LED off','Nav':'LED purple','Sym':'LED red','App':'LED cyan','Fn':'LED blue','Mod':'LED green','Qwerty':'LED white'}
def key(k,cls=''):
    e=' empty' if k['l']=='' else ''
    sub=f'<span class="s">{html.escape(k["s"])}</span>' if k['s'] else ''
    return f'<div class="k{e} {cls} {k["c"]}"><span class="m">{html.escape(k["l"])}</span>{sub}</div>'
def half(rows,keys): return '<div class="half">'+''.join('<div class="row">'+''.join(key(keys[p]) for p in r)+'</div>' for r in rows)+'</div>'
def thumbs(keys,side):
    if side=='L': return f'<div class="thumb L"><div class="trow">{key(keys[35],"s")}{key(keys[36],"s")}</div><div class="tbody">{key(keys[65],"big")}{key(keys[66],"big")}<div class="tcol">{key(keys[52],"s")}{key(keys[67],"s")}</div></div></div>'
    return f'<div class="thumb R"><div class="trow">{key(keys[37],"s")}{key(keys[38],"s")}</div><div class="tbody"><div class="tcol">{key(keys[53],"s")}{key(keys[68],"s")}</div>{key(keys[69],"big")}{key(keys[70],"big")}</div></div>'
def board(name,trigger,notes,zoom,cls=''):
    k=layers[name]
    chips=''.join(f'<span class="chip">{html.escape(n)}</span>' for n in notes)
    return f'''<section class="{cls}" style="--accent:{ACCENT[name]};--z:{zoom}"><h2><span class="dot"></span>{name}<small>{html.escape(trigger)}</small><em>{LED[name]}</em></h2>
<div class="chips">{chips}</div>
<div class="board">{half(L_rows,k)}{thumbs(k,'L')}{thumbs(k,'R')}{half(R_rows,k)}</div></section>'''
base=board('Base','Colemak-DH',[
 'Thumbs mirrored: Cmd outer · Opt inner · Ctrl upper column · layer hold lower column',
 'Tap left Cmd = ⌘Space (Raycast)','Tap right Cmd = ⌘K (palette)',
 'Tap Del, then hold it again to auto-repeat','Kp locks Sym','Mod+Q toggles Qwerty'],1.18,'hero')
row1=board('Nav','hold Esc (left thumb column)',['Arrows on N E I O home keys · word jump above · line / page below','Inner column: tabs, next window · outer: back, forward','Left hand: Rectangle · Shift+arrow selects'],.74) \
   + board('Sym','hold Tab (right thumb column) · Kp locks',['Left: TypeScript operators, autopairs put the cursor inside','Right: numpad · 0 on ↑ · . on ↓'],.74)
row2=board('App','hold Del',['✦ = Ctrl+Opt+Shift+Cmd + the Colemak letter under the key','Solid name = bound in Raycast','Dashed = suggested app, not bound yet','Bind: Raycast › app › ⌘K › Add Hotkey › hold Del + key'],.74) \
   + board('Fn','hold either outer bottom pinky key',['F1 on = · F2–F6 on 1–5 · F7–F11 on 6–0 · F12 on -','Brightness W F · media L U Y · volume N E I'],.74)
row3=board('Mod','hold the top inner key, right half',['Stock Kinesis layer, untouched','Boot = flash: left half below Kp, right half below Mod','Version on the V cap · Qwerty on the Q cap'],.6) \
   + board('Qwerty','Mod+Q toggles',['Transition overlay · sits below every hold layer','Resets to Colemak-DH on power cycle'],.6)
page=f'''<!doctype html><html><head><meta charset="utf-8"><style>
html{{zoom:2}} body{{margin:0;width:{W}px;height:{H}px;background:#0e1014;color:#e6e8eb;font:13px/1.3 -apple-system,Helvetica,Arial,sans-serif;overflow:hidden}}
.wrap{{padding:54px {SAFE}px 0;display:flex;flex-direction:column;gap:18px;align-items:center}}
.rowx{{display:flex;gap:56px;justify-content:center;align-items:flex-start}}
section{{--accent:#888;display:flex;flex-direction:column;align-items:center}}
h2{{font-size:22px;margin:0 0 4px;font-weight:600;display:flex;align-items:center;gap:10px;color:#f3f4f6}}
.hero h2{{font-size:30px}}
h2 small{{font-size:15px;color:#9aa4b2;font-weight:400}} h2 em{{font-style:normal;font-size:12px;color:var(--accent);border:1px solid var(--accent);border-radius:99px;padding:1px 8px;opacity:.85}}
.dot{{width:12px;height:12px;border-radius:50%;background:var(--accent);display:inline-block;box-shadow:0 0 12px var(--accent)}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:2px 0 8px;max-width:1240px}}
.hero .chips{{max-width:1900px}}
.chip{{font-size:12px;color:#c3c8d1;background:#171b22;border:1px solid #262b34;border-radius:99px;padding:3px 10px;white-space:nowrap}}
.hero .chip{{font-size:14px}}
.board{{display:grid;grid-template-columns:auto auto auto auto;gap:12px;align-items:start;zoom:var(--z);width:max-content}}
.row{{display:flex;gap:4px;margin-bottom:4px}}
.k{{width:76px;height:74px;border:1px solid #2b3039;border-radius:6px;background:#181c23;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:15px;padding:3px;box-sizing:border-box;overflow:hidden;word-break:normal;overflow-wrap:normal;line-height:1.15;color:#e6e8eb;gap:2px}}
.k .s{{font-size:12.5px;color:#8b93a1;line-height:1.1}} .k.hold .s{{color:#c3c8d1}}
.k.bound .s{{color:var(--accent);font-weight:600;font-size:13px}}
.k.sugg{{border-style:dashed;border-color:#3a404b}} .k.sugg .s{{color:#6b7280;font-style:italic}}
.k.free .m{{color:#4b5563}}
.k.warn .s{{color:#fbbf24}}
.k.empty{{background:#111419;border-color:#1c2027}}
.thumb{{margin-top:160px}} .trow{{display:flex;gap:4px;margin-bottom:4px}} .tbody{{display:flex;gap:4px}} .tcol{{display:flex;flex-direction:column;gap:4px}}
.k.s{{width:64px;font-size:13px}} .k.big{{width:64px;height:152px;font-size:13.5px}} .thumb.L .trow{{justify-content:flex-end}}
section .k:not(.empty):not(.sugg){{border-color:color-mix(in srgb,var(--accent) 35%,#2b3039)}}
</style></head><body><div class="wrap">
{base}
<div class="rowx">{row1}</div>
<div class="rowx">{row2}</div>
<div class="rowx">{row3}</div>
</div></body></html>'''
open(os.path.join(HERE,'wallpaper.html'),'w').write(page); print('ok')
