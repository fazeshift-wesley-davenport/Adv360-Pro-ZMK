import re, html, json, os
HERE=os.path.dirname(os.path.abspath(__file__))
_cands=[os.path.join(HERE,'official/config/adv360.keymap'),os.path.join(HERE,'../config/adv360.keymap')]
KEYMAP=os.environ.get('KEYMAP') or next(c for c in _cands if os.path.exists(c))
src=open(KEYMAP).read()
apps=json.load(open(os.path.join(HERE,'apps.json')))
defs=dict(re.findall(r'#define (WIN_\w+)\s+(&kp \S+)',src))
# value = label, or (label, sub-label, css class)
label_map={
 '&trans':'','&none':'','&kp EQUAL':'=','&kp MINUS':'-','&kp TAB':'Tab','&kp ESC':'Esc','&kp LSHFT':'Shift','&kp RSHFT':'Shift',
 '&kp GRAVE':'`','&caps_word':('Caps','word',''),'&kp LEFT':'←','&kp RIGHT':'→','&kp UP':'↑','&kp DOWN':'↓','&kp LBKT':'[','&kp RBKT':']',
 '&kp BSLH':'\\','&kp SEMI':';','&kp SQT':"'",'&kp COMMA':',','&kp DOT':'.','&kp FSLH':'/','&kp BSPC':'Bksp','&kp DEL':'Del',
 '&kp ENTER':'Enter','&kp SPACE':'Space','&kp LALT':'Opt','&kp RALT':'Opt','&kp LGUI':'Cmd','&kp RGUI':'Cmd','&kp LCTRL':'Ctrl','&kp RCTRL':'Ctrl',
 '&mtc LGUI LG(SPACE)':('Cmd','tap ⌘Space','hold'),'&mtc RGUI LG(K)':('Cmd','tap ⌘K','hold'),
 '&mo FN':('Fn','hold','hold'),'&mo MOD':('Mod','hold','hold'),'&tog SYM':('Kp','Sym lock','hold'),'&tog QWERTY':('Qwerty','toggle','hold'),
 '&lth APP DEL':('Del','hold → App','hold'),'&lth NAV ESC':('Esc','hold → Nav','hold'),'&lth SYM TAB':('Tab','hold → Sym','hold'),
 '&kp PG_UP':'PgUp','&kp PG_DN':'PgDn','&kp HOME':'Home','&kp END':'End','&kp LG(LEFT)':('⌘←','line start',''),'&kp LG(RIGHT)':('⌘→','line end',''),
 '&kp LA(LEFT)':('⌥←','word',''),'&kp LA(RIGHT)':('⌥→','word',''),'&kp LC(LS(TAB))':('⌃⇧Tab','prev tab',''),'&kp LC(TAB)':('⌃Tab','next tab',''),
 '&kp LG(LBKT)':('⌘[','back',''),'&kp LG(RBKT)':('⌘]','forward',''),
 '&kp LG(GRAVE)':('⌘`','next window',''),'&kp LG(C)':('⌘C','copy',''),'&kp LG(V)':('⌘V','paste',''),'&kp LG(TAB)':('⌘Tab','prev app',''),'&kp LA(BSPC)':('⌥⌫','delete word',''),'&kp LG(UP)':('⌘↑','doc top',''),'&kp LG(DOWN)':('⌘↓','doc end',''),'&kp LC(UP)':('⌃↑','Mission Ctl',''),
 '&kp LC(LA(C))':('▢','center',''),'&kp LC(LA(BSPC))':('↺','restore',''),'&kp LG(LA(RET))':('▣','maximize',''),
 '&kp LG(LA(LEFT))':('⇠','display',''),'&kp LG(LA(RIGHT))':('⇢','display',''),
 '&mpar':'( )','&mbkt':'[ ]','&mbrc':'{ }','&mtmpl':'${ }','&fat_arrow':'=>','&triple_eq':'===','&not_eq':'!==','&opt_chain':'?.','&nullish':'??',
 '&and_and':'&&','&or_or':'||','&kp LT':'<','&kp GT':'>','&kp TILDE':'~','&kp UNDER':'_','&kp PLUS':'+','&kp ASTRK':'*','&kp COLON':':','&kp DQT':'"','&kp PRCNT':'%',
 '&kp C_BRI_DN':'Bri−','&kp C_BRI_UP':'Bri+','&kp C_PREV':'⏮','&kp C_PP':'⏯','&kp C_NEXT':'⏭','&kp C_MUTE':'Mute','&kp C_VOL_DN':'Vol−','&kp C_VOL_UP':'Vol+','&kp CAPS':'CapsLock',
 '&bt BT_SEL 0':('BT 1','profile',''),'&bt BT_SEL 1':('BT 2','profile',''),'&bt BT_SEL 2':('BT 3','profile',''),'&bt BT_SEL 3':('BT 4','profile',''),'&bt BT_SEL 4':('BT 5','profile',''),
 '&bt BT_CLR':('BT clear','forget host',''),'&bootloader':('Boot','flash this half','warn'),'&stp STP_BAT':('Battery','type level',''),'&macro_ver':('Version','type string',''),
 '&bl BL_TOG':('Backlight','on/off',''),'&rgb_ug RGB_TOG':('LEDs','on/off',''),'&bl BL_INC':'Bri+','&bl BL_DEC':'Bri−','&studio_unlock':'',
}
SPECIAL={'RET':'Enter','SPACE':'Space','SEMI':';','COMMA':',','DOT':'.','LEFT':'←','RIGHT':'→','UP':'↑','DOWN':'↓'}
def lab(tok):
    if tok in label_map: return label_map[tok]
    m=re.match(r'&kp HYPER\((\w+)\)',tok)
    if m:
        k=SPECIAL.get(m.group(1), re.sub(r'^N(\d)$',r'\1',m.group(1)))
        if k in apps['bound']: return ('✦'+k, apps['bound'][k], 'bound')
        if k in apps['suggested']: return ('✦'+k, apps['suggested'][k], 'sugg')
        return ('✦'+k,'','free')
    m=re.match(r'&hm[lr] (\w+) (\w+)$',tok)
    if m:
        mods={'LGUI':'⌘','RGUI':'⌘','LALT':'⌥','RALT':'⌥','LCTRL':'⌃','RCTRL':'⌃','LSHFT':'⇧','RSHFT':'⇧'}
        return (SPECIAL.get(m.group(2), m.group(2)), 'hold '+mods[m.group(1)], 'hold')
    m=re.match(r'&kp (F\d+|N\d)$',tok)
    if m: return m.group(1).replace('N','')
    m=re.match(r'&kp (\w)$',tok)
    if m: return m.group(1)
    return tok.replace('&','')
def norm(v):
    if isinstance(v,tuple): return {'l':v[0],'s':v[1],'c':v[2]}
    return {'l':v,'s':'','c':''}
TOK=r'&(?:hml \w+ \w+|hmr \w+ \w+|lth \w+ \w+|mtc \w+ \w+\(\w+\)|kp HYPER\(\w+\)|kp [A-Z_0-9]+(?:\([A-Z_0-9()]*\))?|mo \w+|tog \w+|bt \w+ \d|bt \w+|stp \w+|bl \w+|rgb_ug \w+|\w+)'
layers=[]
for name,disp,body in re.findall(r'(\w+) \{\s*display-name = "([^"]+)";\s*bindings = <(.*?)>;',src,re.S):
    if name in ('extra1','extra2','extra3'): continue
    b=body
    for k,v in defs.items(): b=b.replace(k,v)
    b=b.replace('___','&trans').replace('XXX','&none')
    toks=re.findall(TOK,b)
    assert len(toks)==76,(name,len(toks))
    layers.append({'name':disp,'keys':[norm(lab(t)) for t in toks]})
json.dump(layers,open(os.path.join(HERE,'layers.json'),'w'),ensure_ascii=False)

# ---- light HTML cheat sheet ----
L_rows=[[0,1,2,3,4,5,6],[14,15,16,17,18,19,20],[28,29,30,31,32,33,34],[46,47,48,49,50,51],[60,61,62,63,64]]
R_rows=[[7,8,9,10,11,12,13],[21,22,23,24,25,26,27],[39,40,41,42,43,44,45],[54,55,56,57,58,59],[71,72,73,74,75]]
def key(k,cls=''):
    e=' empty' if k['l']=='' else ''
    sub=f'<span class="s">{html.escape(k["s"])}</span>' if k['s'] else ''
    return f'<div class="k{e} {cls} {k["c"]}"><span class="m">{html.escape(k["l"])}</span>{sub}</div>'
def half(rows,keys,side):
    return f'<div class="half {side}">'+''.join('<div class="row">'+''.join(key(keys[p]) for p in r)+'</div>' for r in rows)+'</div>'
def thumbs(keys,side):
    if side=='L':
        return f'<div class="thumb L"><div class="trow">{key(keys[35],"s")}{key(keys[36],"s")}</div><div class="tbody">{key(keys[65],"big")}{key(keys[66],"big")}<div class="tcol">{key(keys[52],"s")}{key(keys[67],"s")}</div></div></div>'
    return f'<div class="thumb R"><div class="trow">{key(keys[37],"s")}{key(keys[38],"s")}</div><div class="tbody"><div class="tcol">{key(keys[53],"s")}{key(keys[68],"s")}</div>{key(keys[69],"big")}{key(keys[70],"big")}</div></div>'
notes={
 'Base':'Colemak-DH. LED off. Thumbs mirrored: Cmd outer, Opt inner, Ctrl on the upper column key. Tap left Cmd for Raycast (Cmd+Space), tap right Cmd for the command palette (Cmd+K). Hold the lower column key for a layer, tap it for Esc or Tab. Hold Del for App; tap Del then hold it to auto-repeat.',
 'Qwerty':'Mod+Q toggles this over the base. LED white. It sits below every hold layer, so Mod, Nav, Sym, App and Fn still win while it is on. Resets to Colemak-DH on power cycle.',
 'Fn':'Hold either outer bottom pinky key. LED blue. F-keys on the top row, brightness on W/F, media on L/U/Y and N/E/I, Caps Lock on the old Caps key.',
 'Mod':'Hold the top inner key on the right half. LED green. Stock Kinesis layer: Bluetooth profiles on 1–5, Boot on the key below Kp (left half) or below Mod (right half), version on the V cap, Qwerty toggle on the Q cap.',
 'Sym':'Hold Tab (right thumb column), or tap Kp to lock. LED red. Left hand: TypeScript operators and autopairs. Right hand: numpad, 0 on the up-arrow key.',
 'Nav':'Hold Esc (left thumb column). LED purple. Right hand: arrows on the N E I O home keys, one direction per column (word jump above, line jump or page below). Inner column: tabs and next window. Outer column: back and forward. Left hand: Rectangle. Thumb mods stay live, so Shift+arrow selects.',
 'App':'Hold Del. LED cyan. Every key sends Hyper (Ctrl+Opt+Shift+Cmd) plus the Colemak letter under it. Solid label = hotkey bound in Raycast. Dashed = suggested app, not bound yet. Bind in Raycast: search the app, Cmd+K, Add Hotkey, then hold Del and press the key.',
}
sections=''.join(f'<section><h2>{l["name"]}</h2><p>{notes.get(l["name"],"")}</p><div class="board">{half(L_rows,l["keys"],"L")}{thumbs(l["keys"],"L")}{thumbs(l["keys"],"R")}{half(R_rows,l["keys"],"R")}</div></section>' for l in layers)
page=f'''<!doctype html><html><head><meta charset="utf-8"><title>Advantage 360 Pro layers</title>
<style>
body{{font:13px/1.35 -apple-system,Helvetica,Arial,sans-serif;background:#f6f6f7;color:#111;margin:24px}}
h1{{font-size:20px;margin:0 0 4px}} h2{{font-size:16px;margin:0 0 4px}} p{{margin:0 0 10px;color:#444;max-width:1100px}}
section{{margin-bottom:28px}}
.board{{display:grid;grid-template-columns:auto auto auto auto;gap:14px;align-items:start;background:#fff;border:1px solid #ddd;border-radius:10px;padding:14px;width:max-content}}
.row{{display:flex;gap:4px;margin-bottom:4px}}
.half.R .row{{justify-content:flex-end}}
.k{{width:70px;height:46px;border:1px solid #bbb;border-radius:6px;background:#fafafa;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:12px;padding:2px;box-sizing:border-box;overflow:hidden;word-break:break-word;line-height:1.15}}
.k .s{{font-size:9.5px;color:#666}} .k.bound .s{{color:#0369a1;font-weight:600}} .k.sugg{{border-style:dashed}} .k.sugg .s{{color:#888;font-style:italic}} .k.warn .s{{color:#b45309}}
.k.empty{{background:#eee;border-color:#e2e2e2}}
.thumb{{margin-top:100px}} .trow{{display:flex;gap:4px;margin-bottom:4px}} .tbody{{display:flex;gap:4px}} .tcol{{display:flex;flex-direction:column;gap:4px}}
.k.s{{width:58px;font-size:11px}} .k.big{{width:58px;height:96px}} .thumb.L .trow{{justify-content:flex-end}}
</style></head><body>
<h1>Advantage 360 Pro layers</h1>
<p>Generated from <code>config/adv360.keymap</code>. Grey keys are transparent (fall through to Base) or unused.</p>
{sections}</body></html>'''
open(os.path.join(HERE,'cheatsheet.html'),'w').write(page); print('layers',[l['name'] for l in layers])
