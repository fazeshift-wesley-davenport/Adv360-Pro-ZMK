import json, html, os
HERE=os.path.dirname(os.path.abspath(__file__))
W,H=3008,1692          # logical size of the main display; rendered at zoom 2 -> 6016x3384
SAFE=200               # side margin: the 3456x2234 laptop screen crops ~195px per side when it fills the height
layers={l['name']:l['keys'] for l in json.load(open(os.path.join(HERE,'layers.json')))}
L_rows=[[0,1,2,3,4,5,6],[14,15,16,17,18,19,20],[28,29,30,31,32,33,34],[46,47,48,49,50,51],[60,61,62,63,64]]
R_rows=[[7,8,9,10,11,12,13],[21,22,23,24,25,26,27],[39,40,41,42,43,44,45],[54,55,56,57,58,59],[71,72,73,74,75]]
ACCENT={'Base':'#586e75','Nav':'#6c71c4','Sym':'#b63e2f','App':'#14756d','Fn':'#176487'}
TRIGGER_POSITIONS={'Nav':(67,), 'Sym':(6,69), 'App':(66,), 'Fn':(60,75)}
def key(k,cls=''):
    e=' empty' if k['l']=='' else ''
    layer=f' layer-key layer-{k["layer"]}' if k.get('layer') else ''
    compact=' compact' if len(k['s'])>=8 else ''
    sub=f'<span class="s">{html.escape(k["s"])}</span>' if k['s'] else ''
    main='Caps<br>Lock' if k['l']=='CapsLock' else html.escape(k['l'])
    return f'<div class="k{e}{compact} {cls} {k["c"]}{layer}"><span class="m">{main}</span>{sub}</div>'
def half(rows,keys,side): return f'<div class="half {side}">'+''.join('<div class="row">'+''.join(key(keys[p]) for p in r)+'</div>' for r in rows)+'</div>'
def thumbs(keys,side):
    if side=='L': return f'<div class="thumb L"><div class="trow">{key(keys[35],"s")}{key(keys[36],"s")}</div><div class="tbody">{key(keys[65],"big")}{key(keys[66],"big")}<div class="tcol">{key(keys[52],"s")}{key(keys[67],"s")}</div></div></div>'
    return f'<div class="thumb R"><div class="trow">{key(keys[37],"s")}{key(keys[38],"s")}</div><div class="tbody"><div class="tcol">{key(keys[53],"s")}{key(keys[68],"s")}</div>{key(keys[69],"big")}{key(keys[70],"big")}</div></div>'
def board(name,trigger,zoom,cls=''):
    k=[dict(v) for v in layers[name]]
    for pos in TRIGGER_POSITIONS.get(name,()):
        k[pos]=dict(layers['Base'][pos],layer=name.lower())
    return f'''<section class="{cls}" style="--accent:{ACCENT[name]};--z:{zoom}"><h2>{name}<small>{html.escape(trigger)}</small></h2>
<div class="board">{half(L_rows,k,'L')}{thumbs(k,'L')}{thumbs(k,'R')}{half(R_rows,k,'R')}</div></section>'''
def background():
    # Solarized Light backdrop drawn as vectors, so it stays sharp at 6016x3384.
    def dots(p0,p1,p2,p3,n,r,fill):
        pts=[tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d for a,b,c,d in zip(p0,p1,p2,p3)) for t in (i/(n-1) for i in range(n))]
        return ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r*(.6+.4*i/(n-1)):.1f}" fill="{fill}"/>' for i,(x,y) in enumerate(pts))
    return f'''<svg class="bg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><defs>
<linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fdf6e3"/><stop offset="1" stop-color="#f5ebcf"/></linearGradient>
<linearGradient id="blue" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#268bd2" stop-opacity=".30"/><stop offset="1" stop-color="#2aa198" stop-opacity=".10"/></linearGradient>
<linearGradient id="slate" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#657b83" stop-opacity=".16"/><stop offset="1" stop-color="#93a1a1" stop-opacity=".06"/></linearGradient>
<linearGradient id="gold" x1="1" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#b58900" stop-opacity=".24"/><stop offset="1" stop-color="#b58900" stop-opacity=".04"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".46" r=".55"><stop offset="0" stop-color="#fdf6e3" stop-opacity=".85"/><stop offset=".7" stop-color="#fdf6e3" stop-opacity=".35"/><stop offset="1" stop-color="#fdf6e3" stop-opacity="0"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#paper)"/>
<path d="M0,0H760C600,170 400,250 320,520C240,790 450,1010 250,1260C150,1390 70,1480 0,1540Z" fill="url(#blue)"/>
<path d="M0,180C250,300 190,620 130,900C90,1110 170,1300 0,1430Z" fill="url(#slate)"/>
<path d="M2160,0H{W}V920C2860,780 2900,560 2700,430C2500,300 2360,190 2160,0Z" fill="url(#blue)"/>
<path d="M2560,0H{W}V560C2930,450 2880,300 2780,220C2680,140 2620,80 2560,0Z" fill="url(#slate)"/>
<path d="M{W},980V{H}H1860C2120,1580 2400,1610 2610,1420C2790,1260 2870,1110 {W},980Z" fill="url(#gold)"/>
<path d="M0,{H}H1150C930,1600 720,1650 490,1570C310,1500 160,1530 0,1450Z" fill="url(#gold)"/>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
<g fill="none" stroke-linecap="round">
<path d="M0,690C320,770 540,1010 800,{H}" stroke="#b58900" stroke-opacity=".45" stroke-width="2.5"/>
<path d="M2420,0C2680,240 2950,300 {W},540" stroke="#b58900" stroke-opacity=".45" stroke-width="2.5"/>
<path d="M2240,{H}C2420,1480 2700,1380 {W},1300" stroke="#b58900" stroke-opacity=".35" stroke-width="2"/>
<path d="M1150,0C1360,140 1700,150 1960,0" stroke="#93a1a1" stroke-opacity=".45" stroke-width="1.5"/>
<path d="M0,1180C420,1240 820,1380 1180,{H}" stroke="#93a1a1" stroke-opacity=".40" stroke-width="1.5"/>
<path d="M{W},760C2700,820 2460,1020 2320,1240" stroke="#93a1a1" stroke-opacity=".35" stroke-width="1.5"/></g>
{dots((340,270),(420,380),(520,520),(560,700),11,6,"#b58900")}
{dots((2500,90),(2560,200),(2640,330),(2720,420),9,5,"#2aa198")}
{dots((180,1420),(260,1500),(380,1560),(520,1600),8,4,"#93a1a1")}
<circle cx="316" cy="250" r="19" fill="#b58900" fill-opacity=".75"/>
<circle cx="2766" cy="306" r="18" fill="#268bd2" fill-opacity=".55"/>
<circle cx="2860" cy="1560" r="10" fill="#b58900" fill-opacity=".5"/></svg>'''
base=board('Base','Colemak-DH',1.18,'hero')
row1=board('Nav','hold Esc (left thumb column)',.76) \
   + board('Sym','hold Enter · Kp locks',.76)
row2=board('App','hold Del',.76) \
   + board('Fn','hold either outer bottom pinky key',.76)
page=f'''<!doctype html><html><head><meta charset="utf-8"><style>
html{{zoom:2}} body{{margin:0;width:{W}px;height:{H}px;background:#fdf6e3;color:#073642;font:13px/1.3 -apple-system,Helvetica,Arial,sans-serif;overflow:hidden}}
.bg{{position:fixed;inset:0;width:100%;height:100%;z-index:-1}}
.wrap{{padding:0 {SAFE}px;box-sizing:border-box;height:{H}px;display:flex;flex-direction:column;gap:28px;align-items:center;justify-content:center}}
.rowx{{display:flex;gap:56px;justify-content:center;align-items:flex-start}}
section{{--accent:#888;display:flex;flex-direction:column;align-items:center}}
h2{{font-size:27px;margin:0 0 4px;font-weight:600;display:flex;align-items:center;gap:10px;color:#073642}}
.hero h2{{font-size:30px}}
h2 small{{font-size:19px;color:#586e75;font-weight:400}}
.board{{display:grid;grid-template-columns:auto auto auto auto;gap:12px;align-items:start;zoom:var(--z);width:max-content}}
.row{{display:flex;gap:4px;margin-bottom:4px}}
.half.R .row{{justify-content:flex-end}}
.k{{width:82px;height:80px;border:1px solid #c8c1ac;border-radius:6px;background:#fff9ebf2;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-size:21px;padding:3px;box-sizing:border-box;overflow:hidden;word-break:normal;overflow-wrap:normal;line-height:1.05;color:#073642;gap:1px}}
.k .s{{font-size:17.5px;color:#586e75;line-height:1.02}} .k.hold .s{{color:#425b62}}
.k.bound .s{{color:var(--accent);font-weight:600;font-size:18px}}
.k.compact .s{{font-size:15px}}
.k.s.compact .s{{font-size:13.5px}}
.k.sugg{{border-style:dashed;border-color:#9b9d94}} .k.sugg .s{{color:#657b83;font-style:italic}}
.k.free .m{{color:#657b83}}
.k.warn .s{{color:#876600}}
.k.empty{{background:#eee8d5c9;border-color:#d8d1bc}}
.thumb{{margin-top:160px}} .trow{{display:flex;gap:4px;margin-bottom:4px}} .tbody{{display:flex;gap:4px}} .tcol{{display:flex;flex-direction:column;gap:4px}}
.k.s{{width:68px;font-size:18.5px}} .k.big{{width:68px;height:164px;font-size:19.5px}} .thumb.L .trow{{justify-content:flex-end}}
section .k:not(.empty):not(.sugg){{border-color:color-mix(in srgb,var(--accent) 32%,#c8c1ac)}}
section .k.layer-key{{background:var(--layer-fill);border:2px solid var(--layer-fill);color:var(--layer-ink);font-weight:600}}
section .k.layer-key .s{{color:var(--layer-ink);font-weight:600}}
.layer-nav{{--layer-fill:#6c71c4;--layer-ink:#fff9eb}}
.layer-sym{{--layer-fill:#b63e2f;--layer-ink:#fff9eb}}
.layer-app{{--layer-fill:#14756d;--layer-ink:#fff9eb}}
.layer-fn{{--layer-fill:#176487;--layer-ink:#fff9eb}}
</style></head><body>{background()}<div class="wrap">
{base}
<div class="rowx">{row1}</div>
<div class="rowx">{row2}</div>
</div></body></html>'''
open(os.path.join(HERE,'wallpaper.html'),'w').write(page); print('ok')
