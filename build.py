#!/usr/bin/env python3
"""Generador común para las 8 webs. Uso: python3 build.py [site_id ...]"""
import json, os, sys, html, importlib, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '..', 'out')
# Verificación de las 5 webs en Profitshare (las mismas etiquetas en todas; cada web valida la suya).
PS_CODES = ('4b117ecedd5396bdf8d4694a050ff64c', 'a4904ead5cafa76fa39f06a137dbe139', '98eda5bf57e12769b802a733f1f129be',
            'b33f3182567693567e2349dac833116f', '295f669d182e8b3e2cc9c129dccc2bf5')
PS_META = ''.join("<meta name='profitshareid' content='%s' />\n" % x for x in PS_CODES)
PUB = 'ca-pub-3913582839475889'
UPDATED = '2026-11-24'
UPDATED_RO = '24 noiembrie 2026'
PRICE_VALID = '2026-12-31'  # actualizar junto con los precios
FORMSPREE = 'https://formspree.io/f/mjywywjw'

SITES = ['dronaagricola', 'robotgazon', 'gratarexpert', 'energiemobila',
         'sculapotrivita', 'irigasmart', 'stupulmodern', 'somnbun']
EXTRA = ['salariuclar', 'pensiaclara']

esc = html.escape

CSS = r"""
:root{--c1:%(c1)s;--c2:%(c2)s;--ac:%(accent)s;--ink:#14202b;--mut:#5b6876;--bg:#f6f8fb;--card:#fff;--line:#e3e8ef;--r:14px}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%%}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;font-size:17px}
a{color:var(--c1)}img,svg{max-width:100%%}
.wrap{max-width:1080px;margin:0 auto;padding:0 18px}
header.top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:60px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:19px;color:var(--ink);text-decoration:none;letter-spacing:-.2px}
.logo svg{width:32px;height:32px;flex:none}
nav.main{display:flex;gap:4px;flex-wrap:wrap}
nav.main a{color:var(--ink);text-decoration:none;font-weight:600;font-size:15px;padding:7px 10px;border-radius:9px}
nav.main a:hover,nav.main a.on{background:var(--bg);color:var(--c1)}
.burger{display:none;background:none;border:1px solid var(--line);border-radius:9px;padding:6px 10px;font-size:15px;font-weight:700}
@media(max-width:820px){nav.main{display:none;position:absolute;left:0;right:0;top:60px;background:#fff;border-bottom:1px solid var(--line);flex-direction:column;padding:8px 14px}nav.main.open{display:flex}.burger{display:block}}
.hero{background:linear-gradient(135deg,var(--c1),var(--c2));color:#fff;padding:38px 0 64px}
.hero h1{font-size:clamp(27px,4.4vw,42px);line-height:1.15;margin:0 0 10px;letter-spacing:-.5px}
.hero p{margin:0;max-width:720px;font-size:18px;opacity:.95}
.hero .badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.hero .badges span{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);padding:4px 11px;border-radius:99px;font-size:14px;font-weight:600}
.pagehead{background:linear-gradient(135deg,var(--c1),var(--c2));color:#fff;padding:26px 0 30px}
.pagehead h1{margin:6px 0 6px;font-size:clamp(25px,3.8vw,36px);line-height:1.2;letter-spacing:-.4px}
.pagehead p{margin:0;opacity:.95;max-width:760px}
.crumbs{font-size:14px;opacity:.9}.crumbs a{color:#fff}
.tool{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:0 10px 30px rgba(20,32,43,.08);padding:22px;margin-top:-42px;position:relative}
.tool h2{margin:0 0 14px;font-size:21px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media(max-width:720px){.grid2,.grid3{grid-template-columns:1fr}}
label.f{display:block;font-size:14px;font-weight:700;margin-bottom:5px;color:#2b3947}
.f small{font-weight:500;color:var(--mut)}
input[type=number],input[type=text],input[type=email],select,textarea{width:100%%;padding:11px 12px;border:1.5px solid var(--line);border-radius:10px;font-size:17px;font-family:inherit;background:#fff;color:var(--ink)}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--c2);box-shadow:0 0 0 3px rgba(0,0,0,.05)}
.chk{display:flex;gap:8px;align-items:flex-start;font-size:15px;margin-top:6px}
.chk input{margin-top:5px}
.seg{display:flex;border:1.5px solid var(--line);border-radius:10px;overflow:hidden}
.seg button{flex:1;padding:10px;border:0;background:#fff;font-weight:700;font-size:15px;cursor:pointer;color:var(--mut)}
.seg button.on{background:var(--c1);color:#fff}
.btn{display:inline-block;background:var(--c1);color:#fff;border:0;border-radius:10px;padding:12px 18px;font-weight:700;font-size:16px;cursor:pointer;text-decoration:none}
.btn.alt{background:var(--ac);color:#14202b}
.res{margin-top:18px;border-top:1px dashed var(--line);padding-top:16px}
.big{display:flex;flex-wrap:wrap;gap:12px}
.kpi{flex:1 1 180px;background:var(--bg);border-radius:12px;padding:12px 14px}
.kpi b{display:block;font-size:clamp(22px,3.4vw,30px);line-height:1.15;color:var(--c1)}
.kpi span{font-size:14px;color:var(--mut);font-weight:600}
.kpi.main{background:var(--c1)}.kpi.main b,.kpi.main span{color:#fff}
table.t{width:100%%;border-collapse:collapse;margin:14px 0;font-size:15.5px;background:#fff}
table.t th,table.t td{padding:9px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
table.t th{background:var(--bg);font-size:14px}
table.t td.n,table.t th.n{text-align:right;white-space:nowrap}
.tw{overflow-x:auto}
.bar{height:12px;border-radius:99px;background:var(--line);overflow:hidden;display:flex;margin:10px 0}
.bar i{display:block;height:100%%}
.note{font-size:14px;color:var(--mut)}
.box{background:#fff;border:1px solid var(--line);border-left:5px solid var(--ac);border-radius:12px;padding:14px 16px;margin:18px 0}
.box.info{border-left-color:var(--c2)}
main.content{padding:26px 0 10px}
.cols{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:28px}
@media(max-width:900px){.cols{grid-template-columns:1fr}}
article.prose{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px clamp(16px,3vw,34px)}
.prose h2{font-size:24px;margin:30px 0 10px;letter-spacing:-.3px;line-height:1.25}
.prose h3{font-size:19px;margin:22px 0 6px}
.prose p,.prose li{max-width:72ch}
.prose ul,.prose ol{padding-left:22px}
.meta{font-size:14px;color:var(--mut);margin-bottom:6px}
aside.side .card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:16px;margin-bottom:16px}
aside.side h3{margin:0 0 8px;font-size:16px}
aside.side ul{list-style:none;padding:0;margin:0}
aside.side li{border-top:1px solid var(--line);padding:8px 0;font-size:15px}
aside.side li:first-child{border-top:0}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px;margin:16px 0}
.cards a.c{display:block;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:16px;text-decoration:none;color:var(--ink);transition:transform .12s,box-shadow .12s}
.cards a.c:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(20,32,43,.08)}
.cards a.c b{display:block;font-size:17px;margin-bottom:4px;color:var(--c1)}
.cards a.c span{font-size:14.5px;color:var(--mut)}
.tag{display:inline-block;font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;color:var(--c1);background:var(--bg);border-radius:6px;padding:2px 7px;margin-bottom:6px}
section.sec{margin:34px 0}
section.sec h2{font-size:25px;margin:0 0 8px;letter-spacing:-.3px}
details{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:9px 0}
details summary{cursor:pointer;font-weight:700}
details p{margin:8px 0 2px}
.ad{margin:22px 0;min-height:10px}
footer.foot{background:#101a24;color:#c8d2dc;margin-top:44px;padding:34px 0 22px;font-size:15px}
footer.foot a{color:#fff;text-decoration:none}
footer.foot .fg{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}
@media(max-width:720px){footer.foot .fg{grid-template-columns:1fr}}
footer.foot h4{color:#fff;margin:0 0 8px;font-size:15px}
footer.foot ul{list-style:none;padding:0;margin:0}footer.foot li{margin:5px 0}
footer.foot .legal{border-top:1px solid #263544;margin-top:22px;padding-top:14px;font-size:13px;color:#8fa0b0}
.sr{position:absolute;left:-9999px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin:18px 0}
.pc{background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}
.pc .im{background:linear-gradient(160deg,#eef3f7,#dfe7ee);aspect-ratio:16/10;display:flex;align-items:center;justify-content:center;position:relative}
.pc .im svg{width:78%%;height:auto}
.pc .rib{position:absolute;top:12px;left:12px;background:var(--ac);color:#14202b;font-size:12.5px;font-weight:800;padding:4px 10px;border-radius:99px}
.pc .bd{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
.pc h3{margin:0;font-size:21px;letter-spacing:-.3px}.pc h3 a{color:var(--ink);text-decoration:none}
.pc .tl{margin:0;color:var(--mut);font-size:15.5px}
.pc ul.ks{list-style:none;padding:0;margin:4px 0;display:grid;grid-template-columns:1fr 1fr;gap:6px}
.pc ul.ks li{background:var(--bg);border-radius:10px;padding:7px 9px;font-size:13.5px;color:var(--mut);line-height:1.3}
.pc ul.ks b{display:block;color:var(--ink);font-size:16px}
.pc .pr{font-size:20px;font-weight:800;color:var(--c1);margin-top:auto}.pgrid:has(>.pc:only-child){grid-template-columns:1fr}.pc .pr small{display:block;font-size:12.5px;color:var(--mut);font-weight:600}
.pc .act{display:flex;gap:8px;flex-wrap:wrap}.pc .act .btn{flex:1;text-align:center;padding:11px 12px;font-size:15px}
.btn.ghost{background:#fff;color:var(--c1);border:1.5px solid var(--c1)}
.picks{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:-40px;position:relative}
@media(max-width:620px){.picks{grid-template-columns:1fr 1fr;gap:8px}.picks a{padding:10px 12px}.picks a b{font-size:15px}.picks a span{font-size:11px}}
.picks a{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px 16px;text-decoration:none;color:var(--ink);box-shadow:0 8px 24px rgba(20,32,43,.07)}
.picks a span{display:block;font-size:13px;font-weight:700;color:var(--mut);text-transform:uppercase;letter-spacing:.4px}
.picks a b{font-size:18px;color:var(--c1)}
.cmp{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px clamp(12px,2.5vw,26px)}
.cmp .cols3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(8px,2vw,22px)}
.cmp select{font-weight:700;font-size:15px;padding:9px 10px}@media(max-width:520px){.cmp select{font-size:13px;padding:8px 4px}}
.cmp .ch{text-align:center;padding:12px 4px 6px}
.cmp .ch svg{width:100%%;max-width:170px;height:auto}
.cmp .ch .pr{font-weight:800;color:var(--c1);margin:4px 0 8px}
.cmp .ch .btn{padding:9px 12px;font-size:14px}
.cmp .row{border-top:1px solid var(--line);padding:12px 0 10px}
.cmp .row h4{margin:0 0 8px;text-align:center;font-size:13px;font-weight:800;color:var(--mut);text-transform:uppercase;letter-spacing:.5px}
.cmp .row .cols3 div{text-align:center;font-size:clamp(14px,2.2vw,19px);font-weight:700;line-height:1.3}
.cmp .row .cols3 div small{display:block;font-size:12.5px;color:var(--mut);font-weight:600}
.cmp .row .cols3 div.win{color:var(--c1)}
.cmp .row .cols3 div.win:after{content:"▲ cel mai bun";display:block;font-size:11px;color:var(--c2);font-weight:800;letter-spacing:.3px}
.phero{display:grid;grid-template-columns:1.1fr 1fr;gap:24px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;margin-top:-30px;position:relative}
@media(max-width:820px){.phero{grid-template-columns:1fr}}
.phero .im{background:linear-gradient(160deg,#eef3f7,#dfe7ee);border-radius:14px;display:flex;align-items:center;justify-content:center;min-height:220px}
.phero .im svg{width:82%%}
.phero h2{margin:0 0 6px;font-size:24px}
.phero .pr{font-size:26px;font-weight:800;color:var(--c1);margin:10px 0 2px}
.pros{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0}@media(max-width:620px){.pros{grid-template-columns:1fr}}
.pros div{border-radius:12px;padding:12px 16px}.pros .p{background:#eef7ea}.pros .c{background:#fbefee}
.pros h3{margin:0 0 6px;font-size:16px}.pros ul{margin:0;padding-left:20px}.pros li{font-size:15.5px;margin:3px 0}
.disc{font-size:13px;color:var(--mut);margin-top:6px}
.split{display:grid;grid-template-columns:minmax(0,360px) 1fr;gap:24px;align-items:center}@media(max-width:720px){.split{grid-template-columns:1fr}}
"""

NAV_JS = "document.addEventListener('click',function(e){var b=e.target.closest('.burger');if(b){document.querySelector('nav.main').classList.toggle('open')}});"


def logo_svg(s, size=32):
    return ('<svg viewBox="0 0 64 64" width="%d" height="%d" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect width="64" height="64" rx="16" fill="url(#lg)"/>%s</svg>') % (size, size, s['c1'], s['c2'], s['mark'])


def favicon(s):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect width="64" height="64" rx="16" fill="url(#lg)"/>%s</svg>') % (s['c1'], s['c2'], s['mark'])


def url(s, slug):
    return 'https://%s/%s' % (s['domain'], '' if slug == 'index' else slug + '.html')


def asset(s, name):
    """URL absoluta de una imagen copiada desde la raíz del repo (og-image.jpg, logo.png), o None."""
    return 'https://%s/%s' % (s['domain'], name) if name in s.get('assets', ()) else None


def ldjson(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(',', ':'))


AFF_NOTE = '<p class="note">Unele linkuri către magazine pot fi linkuri de afiliere. Prețurile sunt orientative, verificate la data actualizării; verifică prețul final în magazin.</p>'


def faq_html(faq):
    if not faq:
        return ''
    out = ['<section class="sec"><h2>Întrebări frecvente</h2>']
    for q, a in faq:
        out.append('<details><summary>%s</summary><p>%s</p></details>' % (q, a))
    out.append('</section>')
    return ''.join(out)


def strip_tags(t):
    return re.sub(r'<[^>]+>', '', t)


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip_tags(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]}


def crumbs_ld(s, p):
    items = [{"@type": "ListItem", "position": 1, "name": s['name'], "item": url(s, 'index')}]
    if p.get('kind') == 'article':
        items.append({"@type": "ListItem", "position": 2, "name": "Ghiduri", "item": url(s, 'ghiduri')})
    items.append({"@type": "ListItem", "position": len(items) + 1, "name": p.get('crumb', p['h1']), "item": url(s, p['slug'])})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def head(s, p):
    title = p['title']
    assert len(title) <= 62, (s['id'], p['slug'], len(title), title)
    desc = p['desc']
    canon = url(s, p['slug'])
    lds = []
    if p['slug'] == 'index':
        lds.append({"@context": "https://schema.org", "@type": "WebSite", "name": s['name'], "url": url(s, 'index'),
                    "inLanguage": "ro-RO", "description": s['tagline']})
        lds.append({"@context": "https://schema.org", "@type": "Organization", "name": s['name'], "url": url(s, 'index'),
                    "logo": asset(s, 'logo.png') or 'https://%s/favicon.svg' % s['domain']})
        if s.get('products'):
            lds.append({"@context": "https://schema.org", "@type": "ItemList", "name": p['h1'][:110],
                        "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(s, x['slug']), "name": x['name']}
                                            for i, x in enumerate(s['products'])]})
    else:
        lds.append(crumbs_ld(s, p))
    if p.get('kind') == 'tool' or p.get('tool'):
        lds.append({"@context": "https://schema.org", "@type": "WebApplication", "name": p.get('toolname', p['h1']),
                    "url": canon, "applicationCategory": p.get('appcat', 'FinanceApplication'), "operatingSystem": "Any",
                    "inLanguage": "ro-RO", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "RON"}})
    if p.get('kind') == 'article':
        lds.append({"@context": "https://schema.org", "@type": "Article", "headline": p['h1'][:110], "description": desc,
                    "inLanguage": "ro-RO", "datePublished": p.get('date', UPDATED), "dateModified": max(p.get('date', UPDATED), UPDATED),
                    "mainEntityOfPage": canon, "author": {"@type": "Organization", "name": s['name'], "url": url(s, 'despre')},
                    "publisher": {"@type": "Organization", "name": s['name'], "url": url(s, 'index'),
                                  "logo": {"@type": "ImageObject", "url": asset(s, 'logo.png') or 'https://%s/favicon.svg' % s['domain']}}})
        if asset(s, 'og-image.jpg'):
            lds[-1]["image"] = asset(s, 'og-image.jpg')
    if p.get('kind') == 'product' and product_ld(s, p['prod']).get('offers'):
        lds.append(product_ld(s, p['prod']))  # sin precio no hay Product: Google lo marcaría como inválido
    if p.get('faq'):
        lds.append(faq_ld(p['faq']))
    elif p.get('kind') == 'product' and p['prod'].get('faq'):
        lds.append(faq_ld(p['prod']['faq']))
    noindex = '<meta name="robots" content="noindex">' if p['slug'] == '404' else ''
    noindex += PS_META
    return """<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
%(noindex)s<link rel="canonical" href="%(canon)s">
<meta property="og:type" content="%(ogt)s">
<meta property="og:site_name" content="%(name)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canon)s">
<meta property="og:locale" content="ro_RO">
%(ogimg)s<meta name="theme-color" content="%(c1)s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css?v=3">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%(pub)s" crossorigin="anonymous"></script>
%(ld)s
</head>""" % dict(title=esc(title), desc=esc(desc), canon=canon, name=esc(s['name']), c1=s['c1'], pub=PUB,
                    ogt='article' if p.get('kind') in ('article', 'product') else 'website', noindex=noindex,
                    ld='\n'.join(ldjson(x) for x in lds), ogimg=og_tags(s, title))


def og_tags(s, title):
    img = asset(s, 'og-image.jpg')
    if not img:
        return '<meta name="twitter:card" content="summary">\n'
    return ('<meta property="og:image" content="%s">\n<meta property="og:image:width" content="1200">\n'
            '<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="%s">\n'
            '<meta name="twitter:card" content="summary_large_image">\n') % (img, esc(s['name'] + ': ' + s['tagline']))


def header(s, p):
    links = []
    for href, label in s['nav']:
        on = ' class="on"' if href.replace('.html', '') == p['slug'] or (href == '/' and p['slug'] == 'index') else ''
        links.append('<a href="%s"%s>%s</a>' % (href, on, label))
    return """<body>
<header class="top"><div class="wrap">
<a class="logo" href="/">%s<span>%s</span></a>
<button class="burger" aria-label="Meniu">Meniu ☰</button>
<nav class="main">%s</nav>
</div></header>""" % (logo_svg(s), esc(s['name']), ''.join(links))


def footer(s):
    arts = [p for p in s['pages'] if p.get('kind') == 'article'][:5]
    tools = [p for p in s['pages'] if p.get('kind') == 'tool' or p['slug'] == 'index']
    col1 = 'Calculatoare'
    if s.get('products'):
        col1 = s.get('models_label', 'Modele')
        tools = [{'slug': x['slug'], 'short': x['name']} for x in s['products'][:6]]
    return """<footer class="foot"><div class="wrap"><div class="fg">
<div><a class="logo" href="/" style="color:#fff">%s<span>%s</span></a><p>%s</p><p class="note" style="color:#8fa0b0">Informațiile au caracter general și nu înlocuiesc sfatul unui specialist. Verificăm cifrele cu sursele oficiale; dacă vezi o greșeală, <a href="/contact.html">scrie-ne</a>.</p></div>
<div><h4>%s</h4><ul>%s</ul></div>
<div><h4>Ghiduri</h4><ul>%s<li><a href="/ghiduri.html">Toate ghidurile →</a></li></ul></div>
</div>
<div class="legal">© 2026 %s · Actualizat: %s · <a href="/despre.html">Despre</a> · <a href="/contact.html">Contact</a> · <a href="/politica-confidentialitate.html">Confidențialitate</a></div>
</div></footer>
<script>%s</script>
%s
</body>
</html>""" % (logo_svg(s), esc(s['name']), s['tagline'],
              col1, ''.join('<li><a href="%s">%s</a></li>' % ('/' if t['slug'] == 'index' else '/' + t['slug'] + '.html', t.get('short') or t['h1']) for t in tools),
              ''.join('<li><a href="/%s.html">%s</a></li>' % (a['slug'], a.get('short', a['h1'])) for a in arts),
              esc(s['name']), UPDATED_RO, NAV_JS,
              '<script src="/app.js?v=2" defer></script>' if s.get('js') else '')


def side(s, p):
    others = [x for x in s['pages'] if x.get('kind') in ('article', 'tool', 'product') and x['slug'] not in (p['slug'], 'index')][:7]
    return """<aside class="side"><div class="card"><h3>%s</h3><p class="note" style="margin:0 0 10px">%s</p><a class="btn" href="%s">%s</a></div>
<div class="card"><h3>Citește și</h3><ul>%s</ul></div></aside>""" % (
        s['side_title'], s['side_text'], s.get('side_href', '/'), s.get('side_btn', 'Deschide calculatorul'),
        ''.join('<li><a href="/%s.html">%s</a></li>' % (x['slug'], x.get('short', x['h1'])) for x in others))


REL = 'sponsored nofollow noopener'


def prod_url(x):
    return '/%s.html' % x['slug']


MODERN_CSS = """
/* v3: aspect modern */
body{background:#f4f6f9}
.hero{position:relative;overflow:hidden;padding:46px 0 78px;background:radial-gradient(1200px 400px at 85% -10%,rgba(255,255,255,.22),transparent 60%),linear-gradient(135deg,var(--c1),var(--c2))}
.hero:after{content:"";position:absolute;right:-120px;bottom:-160px;width:420px;height:420px;border-radius:50%;background:rgba(255,255,255,.07)}
.hero h1{font-weight:850;letter-spacing:-.8px}
.pc{border-radius:20px!important;border:1px solid #e6ebf1!important;box-shadow:0 1px 2px rgba(16,24,40,.04),0 8px 24px rgba(16,24,40,.06);transition:transform .18s ease,box-shadow .18s ease;overflow:hidden}
.pc:hover{transform:translateY(-4px);box-shadow:0 2px 4px rgba(16,24,40,.05),0 18px 40px rgba(16,24,40,.12)}
.pc .im{background:#fff!important;border-bottom:1px solid #eef1f5}
.pc .im img{width:100%;height:100%;object-fit:cover;transition:transform .35s ease}
.pc:hover .im img{transform:scale(1.04)}
.pc .rib{border-radius:99px!important;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.pc h3 a{color:var(--ink);text-decoration:none}.pc h3 a:hover{color:var(--c1)}
.btn{border-radius:12px;transition:filter .15s ease,transform .15s ease}.btn:hover{filter:brightness(1.06);transform:translateY(-1px)}
.phero{border-radius:24px!important;box-shadow:0 10px 40px rgba(16,24,40,.10)}
.phero .im{background:#fff!important;border:1px solid #eef1f5}
.phero .im{overflow:hidden;padding:0!important}.phero .im img{width:100%;height:100%;max-height:440px;object-fit:cover;border-radius:14px}
.cmp .ch img{width:100%;max-width:190px;height:120px;object-fit:cover;border-radius:12px}
.credit{font-size:12px;color:var(--mut);margin:6px 2px 0;text-align:right}
article.prose,aside.side .card,.tool{border-radius:20px!important}
"""


def prod_art(s, x, eager=False):
    if x.get('img_local'):
        w, h = x['img_wh']
        return '<img src="/img/%s" alt="%s" width="%d" height="%d"%s decoding="async">' % (
            x['img_local'], esc(x['name']), w, h, '' if eager else ' loading="lazy"')
    return x.get('art') or s.get('art_default', '')


# Fotos oficiales de prensa (licencia de uso para medios; sin modificar, con crédito).
PRESS = {
    'dji-agras-t50': ('https://mnd-assets.mynewsdesk.com/image/upload/fl_attachment/kconiglt2215uqbsf9jo2p',
                      'Foto: DJI (material de presă) – Agras T50 și T25'),
    'dji-agras-t25p': ('https://mnd-assets.mynewsdesk.com/image/upload/fl_attachment/utfe68m2nfn1k62pmci7qq',
                       'Foto: DJI (material de presă) – de la stânga: Agras T70P, T100 și T25P'),
    'dji-agras-t70p': ('https://mnd-assets.mynewsdesk.com/image/upload/fl_attachment/utfe68m2nfn1k62pmci7qq',
                       'Foto: DJI (material de presă) – de la stânga: Agras T70P, T100 și T25P'),
    'dji-agras-t100': ('https://mnd-assets.mynewsdesk.com/image/upload/fl_attachment/utfe68m2nfn1k62pmci7qq',
                       'Foto: DJI (material de presă) – de la stânga: Agras T70P, T100 și T25P'),
    'segway-navimow-i105e': ('https://mma.prnewswire.com/media/2352379/Segway_Robotic.jpg?p=original',
                             'Foto: Segway Navimow (material de presă) – seria Navimow i'),
    'ecoflow-delta-3-plus': ('https://mma.prnewswire.com/media/2620507/D3P.jpg?p=original', 'Foto: EcoFlow (material de presă)'),
    'ecoflow-river-3-plus': ('https://mma.prnewswire.com/media/2620508/R3P.jpg?p=original', 'Foto: EcoFlow (material de presă)'),
    'bluetti-premium-100-v2': ('https://mma.prnewswire.com/media/2724776/0704.jpg?p=original', 'Foto: BLUETTI (material de presă)'),
    'bosch-easydrill-18v-40': ('https://www.bosch-presse.de/pressportal/de/media/dam_images/pi11432/2_easydrill_18v-40_anwendung_img_w1280-2.jpg',
                               'Foto: Bosch'),
}


def fetch_images(s, out):
    """Descarga las fotos oficiales (campo img) y las reduce a WebP. Si algo falla, se queda la ilustración SVG."""
    for x in s.get('products', []):
        if not x.get('img') and x['slug'] in PRESS:
            x['img'], x['img_credit'] = PRESS[x['slug']]
    items = [x for x in s.get('products', []) if x.get('img')]
    if not items:
        return
    try:
        from PIL import Image
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 'pillow'], check=False)
        try:
            from PIL import Image
        except ImportError:
            print('PIL no disponible: se usan ilustraciones')
            return
    import io, urllib.request
    os.makedirs(os.path.join(out, 'img'), exist_ok=True)
    for x in items:
        try:
            req = urllib.request.Request(x['img'], headers={'User-Agent': 'Mozilla/5.0 (site build)'})
            data = urllib.request.urlopen(req, timeout=30).read()
            im = Image.open(io.BytesIO(data))
            im = im.convert('RGBA')  # sin recortes: las licencias de prensa piden la imagen sin modificar
            bg = Image.new('RGB', im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            im = bg
            im.thumbnail((900, 900))
            name = x['slug'] + '.webp'
            im.save(os.path.join(out, 'img', name), 'WEBP', quality=82, method=6)
            x['img_local'], x['img_wh'] = name, im.size
        except Exception as e:  # noqa
            print('imagen fallida', x['slug'], e)


def price_html(x):
    return '%s<small>%s</small>' % (x['price'], x.get('price_note', 'preț orientativ'))


def buy_btn(x, cls='btn alt'):
    return '<a class="%s" href="%s" rel="%s" target="_blank">%s</a>' % (cls, esc(x['link']), REL, x.get('link_label', 'Vezi prețul'))


def prod_card(s, x):
    ks = ''.join('<li><b>%s</b>%s</li>' % (v, k) for k, v in x['keys'][:4])
    rib = '<span class="rib">%s</span>' % x['ribbon'] if x.get('ribbon') else ''
    return """<div class="pc"><a class="im" href="%(u)s" aria-label="%(n)s">%(rib)s%(art)s</a><div class="bd">
<h3><a href="%(u)s">%(n)s</a></h3><p class="tl">%(tl)s</p><ul class="ks">%(ks)s</ul>
<div class="pr">%(pr)s<small>%(cn)s</small></div><div class="act"><a class="btn ghost" href="%(u)s">Detalii</a>%(buy)s</div></div></div>""" % dict(
        u=prod_url(x), n=esc(x['name']), rib=rib, art=prod_art(s, x), tl=x['tagline'], ks=ks, pr=x['price'], cn=x.get('card_note', s.get('card_note', 'preț orientativ · confirmă la dealer')), buy=buy_btn(x))


def prod_grid(s, items=None):
    return '<div class="pgrid">%s</div>' % ''.join(prod_card(s, x) for x in (items or s['products']))


def compare_html(s, title='Compară modelele'):
    """Comparador estilo Apple: 3 columnas con selector; el mejor valor de cada fila se resalta."""
    ps = [x for x in s['products'] if x.get('compare', True)]
    pre = s.get('compare_default', [x['slug'] for x in ps[:3]])
    rows = s['compare_rows']
    def col(slot, x):
        opts = ''.join('<option value="%s"%s>%s</option>' % (y['slug'], ' selected' if y['slug'] == x['slug'] else '', esc(y.get('cmp_label', y['name']))) for y in ps)
        return '<div><select aria-label="Model %d" data-slot="%d">%s</select><div class="ch" data-h="%d">%s</div></div>' % (slot + 1, slot, opts, slot, cmp_head(s, x))
    sel = [next(y for y in ps if y['slug'] == sl) for sl in pre]
    head_ = '<div class="cols3">%s</div>' % ''.join(col(i, x) for i, x in enumerate(sel))
    body = ''
    for ri, r in enumerate(rows):
        cells = cmp_cells(r, sel)
        body += '<div class="row"><h4>%s</h4><div class="cols3" data-r="%d">%s</div></div>' % (r[0], ri, cells)
    data = {y['slug']: {'h': cmp_head(s, y), 'v': [y['spec'].get(r[1]) for r in rows]} for y in ps}
    js_rows = [r[2] if len(r) > 2 else None for r in rows]
    return """<section class="sec" id="compara"><h2>%s</h2><p class="note">Alege oricare trei modele. Valoarea cea mai bună pe fiecare rând este evidențiată.</p>
<div class="cmp" id="cmp">%s%s</div>
<script type="application/json" id="cmpdata">%s</script></section>""" % (
        title, head_, body, json.dumps({'p': data, 'r': js_rows}, ensure_ascii=False).replace('</', '<\\/'))


def cmp_head(s, x):
    return '%s<div class="pr">%s</div><a class="btn ghost" href="%s">Detalii</a>' % (prod_art(s, x), x['price'], prod_url(x))


def cmp_cells(r, sel):
    vals = [x['spec'].get(r[1]) for x in sel]
    best = None
    mode = r[2] if len(r) > 2 else None
    nums = [v[0] for v in vals if isinstance(v, list) and isinstance(v[0], (int, float))]
    if mode and len(nums) > 1 and len(set(nums)) > 1:
        best = max(nums) if mode == 'max' else min(nums)
    out = ''
    for v in vals:
        if v is None:
            out += '<div>—</div>'
        elif isinstance(v, list):
            win = ' class="win"' if best is not None and v[0] == best else ''
            out += '<div%s>%s%s</div>' % (win, v[1], '<small>%s</small>' % v[2] if len(v) > 2 else '')
        else:
            out += '<div>%s</div>' % v
    return out


CMP_JS = r"""
(function(){var c=document.getElementById('cmp');if(!c)return;var D=JSON.parse(document.getElementById('cmpdata').textContent);
function cell(v){if(v==null)return['—',null];if(Array.isArray(v))return[v[1]+(v[2]?'<small>'+v[2]+'</small>':''),typeof v[0]==='number'?v[0]:null];return[v,null]}
function draw(){var ss=[].map.call(c.querySelectorAll('select'),function(s){return s.value});
ss.forEach(function(sl,i){c.querySelector('[data-h="'+i+'"]').innerHTML=D.p[sl].h});
D.r.forEach(function(mode,ri){var cs=ss.map(function(sl){return cell(D.p[sl].v[ri])});var nums=cs.map(function(x){return x[1]}).filter(function(n){return n!=null});
var best=null;if(mode&&nums.length>1&&Math.max.apply(0,nums)!==Math.min.apply(0,nums))best=mode==='max'?Math.max.apply(0,nums):Math.min.apply(0,nums);
c.querySelector('[data-r="'+ri+'"]').innerHTML=cs.map(function(x){return'<div'+(best!=null&&x[1]===best?' class="win"':'')+'>'+x[0]+'</div>'}).join('')})}
c.addEventListener('change',draw)})();
"""


def product_page(s, x):
    spec_rows = ''.join('<tr><th>%s</th><td>%s</td></tr>' % (k, v) for k, v in x['specs'])
    others = [y for y in s['products'] if y['slug'] != x['slug']][:3]
    body = """<div class="phero"><div class="im">%(art)s</div><div><h2>%(n)s</h2><p>%(tl)s</p>
<p><b>Ideal pentru:</b> %(bf)s</p><div class="pr">%(pr)s</div><p class="disc">%(pn)s</p>
<p>%(buy)s</p><p class="disc">Linkul duce la %(store)s. %(aff)s</p></div></div>%(credit)s
<main class="content"><div class="cols" style="padding:0"><article class="prose"><div class="meta">Actualizat: %(upd)s</div>%(desc)s
<div class="pros"><div class="p"><h3>Ce ne place</h3><ul>%(pros)s</ul></div><div class="c"><h3>De ținut cont</h3><ul>%(cons)s</ul></div></div>
<h2>Specificații principale</h2><div class="tw"><table class="t">%(spec)s</table></div><p class="note">%(src)s</p>
<p>%(buy)s <a class="btn ghost" href="/#compara">Compară cu alte modele</a></p>%(faq)s</article>%(side)s</div>
<section class="sec"><h2>Alternative</h2>%(alt)s</section></main>""" % dict(
        art=prod_art(s, x, eager=True), n=esc(x['name']), tl=x['tagline'], bf=x['best_for'], pr=x['price'],
        credit=('<p class="credit">%s</p>' % esc(x['img_credit'])) if x.get('img_local') and x.get('img_credit') else '',
        pn=x.get('price_note', 'Preț orientativ; verifică oferta actuală la dealer.'), buy=buy_btn(x), store=x.get('store', 'magazin'),
        aff=s.get('aff_short', ''), upd=UPDATED_RO, desc=x['desc'],
        pros=''.join('<li>%s</li>' % i for i in x['pros']), cons=''.join('<li>%s</li>' % i for i in x['cons']),
        spec=spec_rows, src=x.get('src', ''), faq=faq_html(x.get('faq')), side=side(s, x), alt=prod_grid(s, others))
    return body


def product_ld(s, x):
    d = {"@context": "https://schema.org", "@type": "Product", "name": x['name'], "brand": {"@type": "Brand", "name": x['brand']},
         "description": strip_tags(x['tagline']), "url": url(s, x['slug'])}
    cur, val = ('RON', x['price_ron']) if x.get('price_ron') else (('EUR', x['price_eur']) if x.get('price_eur') else (None, None))
    if cur:
        d["offers"] = {"@type": "Offer", "priceCurrency": cur, "price": str(val), "itemCondition": "https://schema.org/NewCondition",
                       "availability": "https://schema.org/InStock", "url": x['link'], "priceValidUntil": PRICE_VALID}
    if asset(s, 'og-image.jpg'):
        d["image"] = asset(s, 'og-image.jpg')
    return d


def emag(q):
    """Link de búsqueda en eMAG (se puede envolver luego con Profitshare)."""
    from urllib.parse import quote
    return 'https://www.emag.ro/search/' + quote(q)


def art(kind, label='', c='#2b3440', c2='#7fb85a'):
    """Ilustraciones genéricas (no son fotos de producto)."""
    sh = {
        'mower': '<rect x="70" y="80" width="180" height="72" rx="34" fill="%(c)s"/><rect x="96" y="66" width="128" height="40" rx="20" fill="%(c)s"/><circle cx="160" cy="70" r="12" fill="#e9eef2"/><circle cx="160" cy="70" r="5" fill="%(c2)s"/><circle cx="96" cy="154" r="18" fill="#1c2430"/><circle cx="224" cy="154" r="18" fill="#1c2430"/><circle cx="96" cy="154" r="7" fill="#9aa5b1"/><circle cx="224" cy="154" r="7" fill="#9aa5b1"/><rect x="120" y="112" width="80" height="8" rx="4" fill="%(c2)s"/>',
        'gas': '<rect x="70" y="58" width="180" height="70" rx="14" fill="%(c)s"/><path d="M70 92h180" stroke="#e9eef2" stroke-width="3"/><rect x="128" y="70" width="64" height="8" rx="4" fill="#9aa5b1"/><rect x="30" y="100" width="40" height="8" rx="3" fill="#9aa5b1"/><rect x="250" y="100" width="40" height="8" rx="3" fill="#9aa5b1"/><rect x="84" y="128" width="152" height="40" rx="6" fill="#3a4550"/><circle cx="110" cy="148" r="5" fill="%(c2)s"/><circle cx="160" cy="148" r="5" fill="%(c2)s"/><circle cx="210" cy="148" r="5" fill="%(c2)s"/><rect x="88" y="168" width="8" height="16" fill="#1c2430"/><rect x="224" y="168" width="8" height="16" fill="#1c2430"/>',
        'kettle': '<path d="M90 92a70 62 0 0 1 140 0z" fill="%(c)s"/><rect x="152" y="24" width="16" height="8" rx="4" fill="#9aa5b1"/><rect x="84" y="92" width="152" height="10" rx="4" fill="#9aa5b1"/><path d="M92 104a68 40 0 0 0 136 0z" fill="%(c)s"/><path d="M118 140l-18 44M202 140l18 44M160 144v40" stroke="#3a4550" stroke-width="6" stroke-linecap="round"/><path d="M130 84q8-12 0-24M160 84q8-12 0-24M190 84q8-12 0-24" stroke="%(c2)s" stroke-width="4" fill="none" stroke-linecap="round"/>',
        'station': '<rect x="80" y="50" width="160" height="130" rx="18" fill="%(c)s"/><rect x="118" y="34" width="84" height="22" rx="10" fill="none" stroke="%(c)s" stroke-width="8"/><rect x="100" y="70" width="70" height="40" rx="6" fill="#1c2430"/><rect x="108" y="80" width="%(w)d" height="20" rx="3" fill="%(c2)s"/><circle cx="198" cy="90" r="14" fill="#e9eef2"/><circle cx="193" cy="90" r="3" fill="%(c)s"/><circle cx="203" cy="90" r="3" fill="%(c)s"/><rect x="100" y="132" width="20" height="12" rx="3" fill="#e9eef2"/><rect x="128" y="132" width="20" height="12" rx="3" fill="#e9eef2"/><rect x="156" y="132" width="20" height="12" rx="3" fill="#e9eef2"/>',
        'panel': '<g transform="skewX(-12) translate(40 0)"><rect x="60" y="40" width="200" height="120" rx="6" fill="#1f3b63"/><path d="M110 40v120M160 40v120M210 40v120M60 80h200M60 120h200" stroke="#7fa7d9" stroke-width="2"/></g><rect x="140" y="160" width="10" height="28" fill="#9aa5b1"/><circle cx="250" cy="40" r="18" fill="#f1c232"/>',
        'drill': '<rect x="70" y="62" width="130" height="50" rx="16" fill="%(c)s"/><rect x="200" y="78" width="30" height="18" rx="4" fill="#3a4550"/><rect x="230" y="84" width="46" height="6" rx="3" fill="#9aa5b1"/><path d="M112 110l-12 52h46l8-52z" fill="%(c)s"/><rect x="86" y="160" width="84" height="28" rx="6" fill="#1c2430"/><rect x="96" y="168" width="22" height="6" rx="3" fill="%(c2)s"/><rect x="90" y="74" width="40" height="8" rx="4" fill="#e9eef2" opacity=".6"/>',
        'controller': '<rect x="96" y="40" width="128" height="140" rx="20" fill="%(c)s"/><rect x="114" y="58" width="92" height="40" rx="6" fill="#1c2430"/><rect x="124" y="70" width="50" height="16" rx="3" fill="%(c2)s"/><circle cx="160" cy="138" r="24" fill="#e9eef2"/><circle cx="160" cy="138" r="8" fill="%(c)s"/><path d="M252 70c-10 16-10 26 0 30 10-4 10-14 0-30zM270 110c-8 12-8 20 0 23 8-3 8-11 0-23zM56 96c-8 12-8 20 0 23 8-3 8-11 0-23z" fill="#4aa3df"/>',
        'hive': '<path d="M70 70l90-34 90 34z" fill="#8a5a2b"/><rect x="80" y="70" width="160" height="40" rx="3" fill="#e8b04a"/><rect x="80" y="112" width="160" height="56" rx="3" fill="#d79a2c"/><rect x="140" y="156" width="40" height="8" rx="3" fill="#3a2a14"/><rect x="74" y="168" width="172" height="10" rx="3" fill="#6b4a24"/><circle cx="262" cy="60" r="7" fill="#f1c232"/><circle cx="48" cy="96" r="6" fill="#f1c232"/>',
        'tool': '<rect x="70" y="80" width="180" height="70" rx="12" fill="%(c)s"/><rect x="130" y="60" width="60" height="26" rx="10" fill="none" stroke="%(c)s" stroke-width="8"/><rect x="86" y="96" width="148" height="10" rx="5" fill="#e9eef2" opacity=".5"/><circle cx="110" cy="128" r="8" fill="%(c2)s"/><circle cx="210" cy="128" r="8" fill="%(c2)s"/>',
        'mattress': '<path d="M50 110l60-40h170l-60 40z" fill="#e9eef2"/><path d="M50 110h170v40H50z" fill="%(c)s"/><path d="M220 110l60-40v40l-60 40z" fill="%(c)s" opacity=".8"/><path d="M50 124h170M50 136h170" stroke="%(c2)s" stroke-width="3"/><rect x="70" y="80" width="60" height="22" rx="10" fill="#fff"/>',
    }[kind]
    w = 54
    if label.endswith('Wh'):
        try:
            w = max(10, min(54, int(int(label.split()[0].replace('.', '')) / 3072 * 54)))
        except ValueError:
            pass
    body = sh % {'c': c, 'c2': c2, 'w': w}
    lab = ('<rect x="%d" y="186" width="%d" height="20" rx="10" fill="#14202b" opacity=".75"/><text x="160" y="200" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-weight="800" font-size="13" fill="#fff">%s</text>' % (160 - (len(label) * 4 + 12), len(label) * 8 + 24, esc(label))) if label else ''
    return '<svg viewBox="0 0 320 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ilustrație %s">%s%s</svg>' % (esc(label or kind), body, lab)


def std_home(s, c, arts):
    """Portada estándar del blog de productos."""
    picks = ''.join('<a href="/%s.html"><span>%s</span><b>%s →</b></a>' % (sl, lab, nm) for sl, lab, nm in c['picks'])
    how = ''.join('<div class="box info" style="margin:0"><b>%d. %s</b><p class="note" style="margin:6px 0 0">%s</p></div>' % (i + 1, q, a) for i, (q, a) in enumerate(c['how']))
    extra = ''
    if any(not x.get('compare', True) for x in c['products']):
        extra = '<section class="sec"><h2>%s</h2><div class="split"><div>{{EXTRA_PRODUCTS}}</div><div>%s</div></div></section>' % (c['extra_h2'], c['extra_text'])
    guides = ''.join('<a class="c" href="/%s.html"><span class="tag">Ghid</span><b>%s</b><span>%s</span></a>' % (a['slug'], a.get('short', a['h1']), a['desc']) for a in arts)
    return """<div class="picks">%s</div>
<section class="sec" id="modele"><h2>%s</h2><p>%s</p>
{{PRODUCTS}}</section>
{{COMPARE}}
%s
<section class="sec"><h2>Cum alegi în 3 întrebări</h2><div class="grid3">%s</div></section>
<section class="sec"><div class="box"><b>%s</b> %s</div>%s</section>
<section class="sec"><h2>Ghiduri</h2><div class="cards">%s</div>
<p class="disc">Ilustrațiile sunt schematice, nu fotografii ale produselor. Prețurile sunt orientative, văzute la data actualizării, și se pot schimba; verifică prețul final în magazin. Unele linkuri pot fi de afiliere: dacă cumperi prin ele putem primi un comision, fără cost în plus pentru tine.</p></section>""" % (
        picks, c['h2'], c['intro'], extra, how, c['calc_box'][0], c['calc_box'][1], c.get('after_calc', ''), guides)


def productize(s, c):
    """Convierte una web 'calculadora primero' en blog de productos: la calculadora pasa a /<calc_slug>.html."""
    pages = s['pages']
    idx = next(p for p in pages if p['slug'] == 'index')
    calc = dict(idx)
    calc.update(slug=c['calc_slug'], title=c['calc_title'], kind='tool', crumb=c.get('calc_crumb', 'Calculator'), faq=None)
    s.setdefault('card_note', 'preț orientativ · verifică în magazin')
    if c.get('calc_desc'):
        calc['desc'] = c['calc_desc']
    home = {'slug': 'index', 'kind': 'home', 'title': c['title'], 'desc': c['desc'], 'h1': c['h1'], 'lead': c['lead'],
            'short': c.get('home_short', 'Modele și comparație'), 'body': c.get('home') or std_home(s, c, [p for p in pages if p.get('kind') == 'article']),
            'faq': c.get('faq', idx.get('faq'))}
    target = '/%s.html' % c['calc_slug']
    rest = []
    for p in pages:
        if p['slug'] == 'index':
            continue
        q = dict(p)
        q['body'] = q['body'].replace('href="/"', 'href="%s"' % target).replace('href="/#', 'href="%s#' % target)
        rest.append(q)
    s['pages'] = [home, calc] + rest
    for k in ('nav', 'badges', 'products', 'compare_rows', 'compare_default', 'aff_short', 'side_title', 'side_text',
              'side_href', 'side_btn', 'tagline', 'models_label', 'card_note'):
        if k in c:
            s[k] = c[k]


def fill(s, body):
    if s.get('products'):
        main = [x for x in s['products'] if x.get('compare', True)]
        rest = [x for x in s['products'] if not x.get('compare', True)]
        body = body.replace('{{PRODUCTS}}', prod_grid(s, main)).replace('{{COMPARE}}', compare_html(s))
        body = body.replace('{{EXTRA_PRODUCTS}}', prod_grid(s, rest) if rest else '')
        body = re.sub(r'\{\{CARDS:([a-z0-9,-]+)\}\}', lambda m: prod_grid(
            s, [x for sl in m.group(1).split(',') for x in s['products'] if x['slug'] == sl]), body)
    return body


def render(s, p):
    if p.get('body'):
        p = dict(p, body=fill(s, p['body']))
    h = head(s, p) + header(s, p)
    kind = p.get('kind', 'page')
    if p['slug'] == 'index':
        h += """<section class="hero"><div class="wrap"><h1>%s</h1><p>%s</p><div class="badges">%s</div></div></section>
<main><div class="wrap">%s%s</div></main>""" % (p['h1'], p['lead'], ''.join('<span>%s</span>' % b for b in s['badges']),
                                                 p['body'], faq_html(p.get('faq')))
    elif kind == 'product':
        h += """<section class="pagehead" style="padding-bottom:48px"><div class="wrap"><div class="crumbs"><a href="/">%s</a> › <a href="/#modele">Modele</a></div><h1>%s</h1><p>%s</p></div></section>
<div class="wrap">%s</div>""" % (esc(s['name']), p['h1'], p['lead'], product_page(s, p['prod']))
    elif kind == 'tool':
        h += """<section class="pagehead" style="padding-bottom:58px"><div class="wrap"><div class="crumbs"><a href="/">%s</a> › %s</div><h1>%s</h1><p>%s</p></div></section>
<main><div class="wrap">%s%s</div></main>""" % (esc(s['name']), p.get('crumb', p['h1']), p['h1'], p['lead'], p['body'], faq_html(p.get('faq')))
    elif kind == 'article':
        h += """<section class="pagehead"><div class="wrap"><div class="crumbs"><a href="/">%s</a> › <a href="/ghiduri.html">Ghiduri</a></div><h1>%s</h1><p>%s</p></div></section>
<main class="content"><div class="wrap cols"><article class="prose"><div class="meta">Actualizat: %s · %s</div>%s%s</article>%s</div></main>""" % (
            esc(s['name']), p['h1'], p['lead'], p.get('date_ro', UPDATED_RO), s['name'], p['body'], faq_html(p.get('faq')), side(s, p))
    else:
        h += """<section class="pagehead"><div class="wrap"><div class="crumbs"><a href="/">%s</a></div><h1>%s</h1><p>%s</p></div></section>
<main class="content"><div class="wrap"><article class="prose">%s</article></div></main>""" % (esc(s['name']), p['h1'], p.get('lead', ''), p['body'])
    h += footer(s)
    return h


def std_pages(s):
    arts = [p for p in s['pages'] if p.get('kind') == 'article']
    tools = [p for p in s['pages'] if p.get('kind') == 'tool' and p['slug'] != 'index']
    cards = lambda lst, tag: ''.join('<a class="c" href="/%s.html"><span class="tag">%s</span><b>%s</b><span>%s</span></a>' % (
        x['slug'], tag, x.get('short', x['h1']), x['desc']) for x in lst)
    hub = {'slug': 'ghiduri', 'title': 'Ghiduri și calculatoare | %s' % s['name'], 'h1': 'Ghiduri și calculatoare',
           'desc': 'Toate ghidurile %s: explicații clare, exemple de calcul și calculatoare gratuite.' % s['name'],
           'lead': s['tagline'], 'crumb': 'Ghiduri',
           'body': ('<h2>%s</h2><div class="cards">%s</div><h2>Calculatoare</h2><div class="cards">%s</div><h2>Ghiduri</h2><div class="cards">%s</div>' % (
               s.get('models_label', 'Modele'), ''.join('<a class="c" href="/%s.html"><span class="tag">Model</span><b>%s</b><span>%s</span></a>' % (x['slug'], esc(x['name']), strip_tags(x['tagline'])) for x in s['products']),
               cards(tools, 'Calculator'), cards(arts, 'Ghid'))) if s.get('products') else
               '<h2>Calculatoare</h2><div class="cards"><a class="c" href="/"><span class="tag">Calculator</span><b>%s</b><span>Calculatorul principal %s.</span></a>%s</div><h2>Ghiduri</h2><div class="cards">%s</div>' % (
               s['main_tool'], s['name'], cards(tools, 'Calculator'), cards(arts, 'Ghid'))}
    despre = {'slug': 'despre', 'title': 'Despre %s' % s['name'], 'h1': 'Despre %s' % s['name'], 'crumb': 'Despre',
              'desc': 'Cine suntem, cum lucrăm și de unde luăm cifrele folosite în calculatoarele %s.' % s['name'],
              'lead': s['tagline'], 'body': s['about'] + """
<h2>Cum ne finanțăm</h2><p>Site-ul este gratuit. Poate afișa reclame Google AdSense și, în unele articole, linkuri de afiliere marcate clar: dacă cumperi ceva prin ele, putem primi un mic comision, fără niciun cost în plus pentru tine. Recomandările nu depind de comision.</p>
<h2>Limitări</h2><p>Calculele sunt estimări orientative, făcute pe baza legislației și a datelor publice valabile la data actualizării (%s). Pentru decizii importante, verifică la instituția competentă sau cu un specialist.</p>
<p><a href="/contact.html">Ne poți scrie aici</a> pentru corecturi sau sugestii.</p>""" % UPDATED_RO}
    contact = {'slug': 'contact', 'title': 'Contact | %s' % s['name'], 'h1': 'Contact', 'crumb': 'Contact',
               'desc': 'Scrie-ne o întrebare, o sugestie sau o corectură pentru %s.' % s['name'],
               'lead': 'Răspundem de obicei în câteva zile lucrătoare.',
               'body': """<p>Ai găsit o cifră depășită sau vrei un calculator nou? Scrie-ne mai jos. Nu trimite date personale sensibile (CNP, date bancare).</p>
<form action="%s" method="POST" style="max-width:560px">
<input type="hidden" name="_subject" value="Mesaj %s">
<label class="f" for="em">E-mail</label><input id="em" type="email" name="email" required>
<label class="f" for="ms" style="margin-top:12px">Mesaj</label><textarea id="ms" name="message" rows="6" required></textarea>
<p><button class="btn" type="submit">Trimite</button></p></form>""" % (FORMSPREE, esc(s['name']))}
    priv = {'slug': 'politica-confidentialitate', 'title': 'Politica de confidențialitate | %s' % s['name'],
            'h1': 'Politica de confidențialitate', 'crumb': 'Confidențialitate',
            'desc': 'Ce date colectează %s, cum folosim cookie-urile și ce drepturi ai conform GDPR.' % s['name'],
            'lead': 'Ultima actualizare: %s' % UPDATED_RO,
            'body': """<h2>Pe scurt</h2><p>Calculatoarele %(n)s funcționează integral în browserul tău: cifrele introduse nu sunt trimise și nu sunt salvate pe serverele noastre.</p>
<h2>Publicitate (Google AdSense)</h2><p>Site-ul poate afișa reclame prin Google AdSense. Google și partenerii săi pot folosi cookie-uri pentru a afișa reclame, inclusiv personalizate, <strong>doar după ce îți exprimi acordul</strong> prin mesajul de consimțământ. Poți gestiona preferințele oricând din <a href="https://adssettings.google.com" rel="nofollow noopener">setările de reclame Google</a>. Detalii: <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">cum folosește Google datele de pe site-urile partenere</a>.</p>
<h2>Linkuri de afiliere</h2><p>Unele linkuri către magazine pot fi linkuri de afiliere (de ex. prin Profitshare sau 2Performant). Platforma respectivă poate plasa un cookie pentru a atribui o eventuală comandă.</p>
<h2>Formularul de contact</h2><p>Dacă ne scrii, primim adresa de e-mail și mesajul (prin serviciul Formspree) doar pentru a-ți răspunde. Le ștergem la cerere.</p>
<h2>Drepturile tale</h2><p>Conform GDPR ai dreptul de acces, rectificare, ștergere, restricționare și opoziție, precum și dreptul de a depune plângere la ANSPDCP (dataprotection.ro). Pentru orice solicitare, folosește <a href="/contact.html">pagina de contact</a>.</p>""" % {'n': esc(s['name'])}}
    nf = {'slug': '404', 'title': 'Pagina nu există | %s' % s['name'], 'h1': 'Pagina nu a fost găsită', 'crumb': '404',
          'desc': 'Pagina căutată nu există.', 'lead': 'Poate a fost mutată. Încearcă de aici:',
          'body': '<p><a class="btn" href="/">Pagina principală</a> <a class="btn alt" href="/ghiduri.html">Vezi ghidurile</a></p>'}
    return [hub, despre, contact, priv, nf]


def relpaths(h):
    """Rutas relativas: funcionan en usuario.github.io/repo/ y en el dominio propio."""
    h = h.replace('href="/"', 'href="./"').replace('href="/#', 'href="./#')
    h = re.sub(r'(href|src)="/(?!/)', r'\1="', h)
    return h


def build(sid):
    mod = importlib.import_module('site_' + sid)
    s = mod.SITE
    s['id'] = sid
    extra = importlib.import_module('site_%s_a' % sid) if os.path.exists(os.path.join(ROOT, 'site_%s_a.py' % sid)) else None
    if extra:  # artículos nuevos y correcciones de productos, sin tocar los archivos grandes
        s['pages'] += getattr(extra, 'PAGES', [])
    if os.path.exists(os.path.join(ROOT, 'site_%s_p.py' % sid)):
        productize(s, importlib.import_module('site_%s_p' % sid).CFG)
    if extra:
        for x in s.get('products', []):
            x.update(getattr(extra, 'PATCH', {}).get(x['slug'], {}))
    s['assets'] = [n for n in ('og-image.jpg', 'logo.png') if os.path.exists(os.path.join(ROOT, '..', n))]
    out = os.path.join(OUT, sid)
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    if s.get('products'):
        for x in s['products']:
            s['pages'].append({'slug': x['slug'], 'kind': 'product', 'prod': x, 'title': x['title'], 'desc': x['meta'],
                               'h1': x.get('h1', x['name']), 'lead': x.get('lead', x['tagline']), 'short': x['name'], 'crumb': x['name']})
        s['js'] = (s.get('js') or '') + CMP_JS
    fetch_images(s, out)
    pages = s['pages'] + std_pages(s)
    s_all = dict(s)
    for p in pages:
        with open(os.path.join(out, ('index' if p['slug'] == 'index' else p['slug']) + '.html'), 'w') as f:
            page = render(s, p)
            f.write(page if p['slug'] == '404' else relpaths(page))
    with open(os.path.join(out, 'style.css'), 'w') as f:
        f.write((CSS % s).strip() + '\n' + MODERN_CSS + s.get('css', ''))
    if s.get('js'):
        with open(os.path.join(out, 'app.js'), 'w') as f:
            f.write(s['js'].strip() + '\n')
    for n in s['assets']:
        shutil.copy(os.path.join(ROOT, '..', n), os.path.join(out, n))
    with open(os.path.join(out, 'favicon.svg'), 'w') as f:
        f.write(favicon(s))
    with open(os.path.join(out, 'ads.txt'), 'w') as f:
        f.write('google.com, pub-3913582839475889, DIRECT, f08c47fec0942fa0\n')
    with open(os.path.join(out, 'robots.txt'), 'w') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: https://%s/sitemap.xml\n' % s['domain'])
    for code in PS_CODES:  # fichero de validación Profitshare (método recomendado)
        with open(os.path.join(out, code + '.html'), 'w') as f:
            f.write(code)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        if p['slug'] == '404':
            continue
        pr = '1.0' if p['slug'] == 'index' else ('0.9' if p.get('kind') in ('tool', 'product') else ('0.8' if p.get('kind') == 'article' else '0.4'))
        sm.append('<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (url(s, p['slug']), UPDATED, pr))
    sm.append('</urlset>')
    with open(os.path.join(out, 'sitemap.xml'), 'w') as f:
        f.write('\n'.join(sm) + '\n')
    return len(pages)


if __name__ == '__main__':
    sys.path.insert(0, ROOT)
    ids = sys.argv[1:] or SITES
    for sid in ids:
        if not os.path.exists(os.path.join(ROOT, 'site_%s.py' % sid)):
            print('skip', sid)
            continue
        n = build(sid)
        print('built', sid, n, 'pages')
