FORM = 'https://formspree.io/f/mjywywjw'

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
function f(x){return Math.round(x).toLocaleString('ro-RO')}
var c=$('#calc');if(!c)return;
function run(){
 var ha=+$('#ha').value||0,tr=+$('#tr').value||0,pd=+$('#pd').value||0,ani=+$('#ani').value||1,op=+$('#op').value||0,pr=+$('#pr').value||0,tc=+$('#tc').value||0,rate=+$('#rate').value||0,ore=+$('#ore').value||0;
 var haTot=ha*tr;
 var amort=pd/ani;
 var dronaAn=amort+op*haTot, dronaHa=haTot?dronaAn/haTot:0;
 var prestAn=pr*haTot, tractAn=tc*haTot;
 $('#rD').textContent=f(dronaHa)+' lei/ha';$('#rP').textContent=f(pr)+' lei/ha';$('#rT').textContent=f(tc)+' lei/ha';
 var be=(pr-op)>0?amort/(pr-op):Infinity;
 $('#rBE').textContent=isFinite(be)?f(be)+' ha/an':'—';
 var zile=rate*ore>0?haTot/(rate*ore):0;
 $('#rZile').textContent=zile?zile.toFixed(1).replace('.',',')+' zile de lucru/an':'—';
 $('#rTab').innerHTML=[['Hectare tratate pe an',f(haTot)+' ha'],['Amortizare dronă pe an',f(amort)+' lei'],['Cost anual: dronă proprie',f(dronaAn)+' lei'],['Cost anual: prestator cu dronă',f(prestAn)+' lei'],['Cost anual: tractor + erbicidator',f(tractAn)+' lei']].map(function(r){return '<tr><td>'+r[0]+'</td><td class="n">'+r[1]+'</td></tr>'}).join('');
 var best=Math.min(dronaAn,prestAn,tractAn);var lbl=best===dronaAn?'drona proprie':(best===prestAn?'prestatorul cu dronă':'tractorul');
 $('#rVerd').innerHTML='La '+f(haTot)+' ha tratate pe an, varianta cea mai ieftină este <b>'+lbl+'</b>. '+(isFinite(be)?'Drona proprie începe să fie mai ieftină decât prestatorul de la aproximativ <b>'+f(be)+' ha tratate pe an</b>.':'');
}
c.addEventListener('input',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Calculator: dronă proprie, prestator sau tractor?</h2>
<div class="grid3">
<div><label class="f" for="ha">Suprafață tratată (ha)</label><input id="ha" type="number" min="0" value="300"></div>
<div><label class="f" for="tr">Tratamente pe an</label><input id="tr" type="number" min="0" value="4"></div>
<div><label class="f" for="pd">Prețul pachetului cu dronă (lei, cu TVA)</label><input id="pd" type="number" min="0" step="1000" value="250000"></div>
<div><label class="f" for="ani">Amortizare (ani)</label><input id="ani" type="number" min="1" value="5"></div>
<div><label class="f" for="op">Cost operare dronă <small>(lei/ha: energie, piese, operator)</small></label><input id="op" type="number" min="0" value="25"></div>
<div><label class="f" for="pr">Preț prestator cu dronă <small>(lei/ha, din oferta primită)</small></label><input id="pr" type="number" min="0" value="80"></div>
<div><label class="f" for="tc">Cost tractor + erbicidator <small>(lei/ha)</small></label><input id="tc" type="number" min="0" value="110"></div>
<div><label class="f" for="rate">Productivitate dronă <small>(ha/oră)</small></label><input id="rate" type="number" min="0" step="0.5" value="12"></div>
<div><label class="f" for="ore">Ore efective de zbor pe zi</label><input id="ore" type="number" min="0" value="6"></div>
</div>
<div class="res"><div class="big"><div class="kpi main"><span>Dronă proprie</span><b id="rD">–</b></div><div class="kpi"><span>Prestator cu dronă</span><b id="rP">–</b></div><div class="kpi"><span>Tractor</span><b id="rT">–</b></div><div class="kpi"><span>Prag de rentabilitate</span><b id="rBE">–</b></div></div>
<p id="rVerd" style="margin:12px 0 4px"></p><p class="note" style="margin:0">Timp de lucru estimat: <b id="rZile">–</b></p>
<div class="tw"><table class="t" id="rTab"></table></div></div></form></div>"""

LEAD = """<section class="sec"><div class="box info"><h2 style="margin-top:0">Cauți un prestator sau o ofertă de dronă?</h2>
<p>Spune-ne zona și suprafața. Te punem în legătură cu prestatori și dealeri autorizați din regiunea ta. Fără obligații.</p>
<form action="%s" method="POST"><input type="hidden" name="_subject" value="Cerere DronaAgricola">
<div class="grid3"><div><label class="f" for="lj">Județ</label><input id="lj" name="judet" type="text" required></div>
<div><label class="f" for="lh">Hectare</label><input id="lh" name="hectare" type="number" min="1" required></div>
<div><label class="f" for="le">E-mail</label><input id="le" name="email" type="email" required></div></div>
<div class="grid2" style="margin-top:10px"><div><label class="f" for="lt">Ce te interesează</label><select id="lt" name="interes"><option>Prestator (stropit cu drona)</option><option>Cumpăr dronă</option><option>Cartografiere / monitorizare</option></select></div>
<div><label class="f" for="lc">Cultura principală</label><input id="lc" name="cultura" type="text" placeholder="ex. floarea-soarelui, vie"></div></div>
<p class="note">Datele sunt folosite doar pentru a-ți răspunde și a te pune în legătură cu un prestator, conform <a href="/politica-confidentialitate.html">politicii de confidențialitate</a>.</p>
<button class="btn" type="submit">Trimite cererea</button></form></div></section>""" % FORM

CALC_BODY = TOOL + """
<section class="sec"><h2>Cum citești rezultatul</h2>
<ul><li><strong>Sub câteva sute de hectare tratate pe an</strong>, prestatorul este aproape întotdeauna mai ieftin decât o dronă proprie.</li>
<li><strong>Peste pragul de rentabilitate</strong>, drona proprie câștigă, mai ales dacă faci și fertilizare granulară, semănat de culturi de acoperire sau prestări pentru vecini.</li>
<li><strong>Tractorul rămâne competitiv</strong> pe parcele mari și plane, cu volum mare de soluție la hectar.</li></ul>
<p>Prețurile de pornire pentru fiecare model le găsești pe <a href="/#modele">pagina de modele</a>.</p></section>"""


def drone_svg(label, arms=4, big=False, color='#2b3440', mapper=False):
    """Ilustrație generică (vedere de sus) — nu e fotografia produsului."""
    import math
    cx, cy = 160, 100
    L = 78 if big else 66
    rr = 30 if big else 25
    g = []
    for k in range(arms):
        a = math.pi / arms + 2 * math.pi * k / arms
        x, y = cx + L * math.cos(a), cy + L * 0.62 * math.sin(a)
        g.append('<line x1="%d" y1="%d" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="7" stroke-linecap="round"/>' % (cx, cy, x, y, color))
        g.append('<ellipse cx="%.0f" cy="%.0f" rx="%d" ry="%d" fill="#fff" fill-opacity=".55" stroke="%s" stroke-opacity=".35" stroke-width="2"/>' % (x, y, rr, rr * 0.62, color))
        g.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s"/>' % (x, y, color))
    if mapper:
        body = '<rect x="132" y="80" width="56" height="40" rx="14" fill="%s"/><circle cx="160" cy="123" r="9" fill="#1c2430" stroke="#7fb3d5" stroke-width="3"/>' % color
    else:
        body = ('<rect x="122" y="72" width="76" height="56" rx="16" fill="%s"/>' % color +
                '<rect x="136" y="82" width="48" height="30" rx="9" fill="#e9eef2"/><rect x="136" y="%d" width="48" height="%d" rx="9" fill="#7fb85a"/>' % (82 + 12, 18))
    return ('<svg viewBox="0 0 320 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ilustrație %s">' % label +
            '<ellipse cx="160" cy="190" rx="110" ry="10" fill="#000" fill-opacity=".07"/>' + ''.join(g) + body +
            '<text x="160" y="%d" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-weight="800" font-size="15" fill="#fff">%s</text></svg>' % (124 if not mapper else 106, '' if mapper else label))


TITAN = 'https://www.titanmachinery.ro/en/precizion-farming/drones.html'
AGRI_T50 = 'https://agricover.ro/en/agricultural-drones/dji-agras-t50-drone'
AGRI_M3M = 'https://agricover.ro/en/agricultural-drones/dji-mavic-3m-drone'

PRODUCTS = [
    {'slug': 'dji-agras-t25p', 'cmp_label': 'Agras T25P', 'name': 'DJI Agras T25P', 'brand': 'DJI', 'ribbon': 'Pentru vii și livezi',
     'title': 'DJI Agras T25P: preț în România, specificații, păreri', 'meta': 'DJI Agras T25P pe înțeles: 20 L la stropit, 25 kg la împrăștiat, preț orientativ de la ~10.100 € în România, pentru ce fermă se potrivește și unde îl cumperi.',
     'tagline': 'Cea mai compactă dronă Agras: o poate opera și transporta un singur om.',
     'best_for': 'vii, livezi, parcele mici și terenuri în pantă; ferme sub ~200 ha tratate pe an sau prestatori la început de drum.',
     'price': 'de la ~10.100 €', 'price_eur': 10138, 'price_note': 'Pachet cu 2 baterii, fără generator, conform ofertelor publicate pe piața din România. Confirmă prețul și TVA-ul la dealer.',
     'link': TITAN, 'link_label': 'Cere oferta la dealer', 'store': 'pagina de drone a dealerului autorizat Titan Machinery România',
     'art': drone_svg('20 L', 4, False),
     'keys': [('Rezervor stropire', '20 L'), ('Împrăștiere', '25 kg'), ('Debit', '16–24 L/min'), ('Greutate', '33 kg')],
     'desc': """<p>T25P este răspunsul DJI pentru fermierii care nu au nevoie de o dronă de 50 sau 100 de litri. Este pliabilă, încape în portbagajul unei camionete și, cu 33 kg cu tot cu baterie, poate fi descărcată de o singură persoană. Asta contează enorm în vii și livezi, unde lucrezi pe parcele mici, cu multe mutări pe zi.</p>
<p>La stropit duce 20 kg de soluție, cu un debit de 16 L/min pe două duze sau 24 L/min cu kitul de patru duze, pe o lățime de lucru de 4–7 m. Pentru granule, sistemul de împrăștiere cu șnec (rezervor de 30 L) duce până la 25 kg, suficient pentru fertilizări localizate sau semănat de culturi de acoperire. Picăturile se reglează între 50 și 500 μm, după produs.</p>
<p>Siguranța e la nivelul modelelor mari: sistemul Safety System 3.0 cu radar și viziune pentru ocolirea obstacolelor, foarte util printre stâlpii de vie sau pe lângă linii electrice.</p>
<h2>Merită pentru tine?</h2><p>Da, dacă tratezi suprafețe mici și fragmentate sau vrei să intri pe piața de prestări fără o investiție mare. Nu, dacă ai sute de hectare de culturi mari: acolo un T50 sau T55 face de două ori mai mult cu aceeași echipă.</p>""",
     'pros': ['Cel mai mic preț de intrare din gama Agras', 'Ușor de transportat și operat de o singură persoană', 'Bun în pante, vii și livezi', 'Același ecosistem DJI (aplicație, service, baterii)'],
     'cons': ['Rezervor mic: multe realimentări pe culturi mari', 'Lățime de lucru mai îngustă (4–7 m)', 'Productivitate mult sub T50/T55'],
     'specs': [('Rezervor stropire', '20 kg (sarcină utilă)'), ('Debit maxim', '16 L/min (2 duze) · 24 L/min (4 duze)'), ('Lățime de stropire', '4–7 m'), ('Mărime picături', '50–500 μm'), ('Împrăștiere', '25 kg · rezervor 30 L · șnec 4.0'), ('Greutate', '26 kg fără baterie · 33 kg cu baterie'), ('Siguranță', 'Safety System 3.0')],
     'src': 'Sursa specificațiilor: fișa tehnică oficială DJI Agriculture (ag.dji.com/t25p).',
     'spec': {'tank': [20, '20 L'], 'flow': [24, '16–24 L/min'], 'width': [7, '4–7 m'], 'sptank': [30, '30 L'], 'sprate': None, 'weight': [33, '33 kg'], 'price': [10138, '~10.100 €'], 'ideal': 'Vii, livezi, parcele mici'}},
    {'slug': 'dji-agras-t50', 'cmp_label': 'Agras T50', 'name': 'DJI Agras T50', 'brand': 'DJI', 'ribbon': 'Cel mai vândut',
     'title': 'DJI Agras T50: preț în România, specificații, păreri', 'meta': 'DJI Agras T50: 40 L la stropit, 50 kg la împrăștiat, până la ~21 ha/oră. Preț orientativ în România de la ~15.500 €, pentru cine merită și unde îl cumperi.',
     'tagline': 'Calul de povară al fermelor mari: 40 L de soluție și 50 kg de granule pe zbor.',
     'best_for': 'culturi mari (cereale, floarea-soarelui, porumb, rapiță), ferme de câteva sute de hectare și prestatori.',
     'price': 'de la ~15.500 €', 'price_eur': 15525, 'price_note': 'Pachet cu 3 baterii și generator, înainte de reduceri, conform ofertelor publicate în România. Confirmă prețul și TVA-ul la dealer.',
     'link': AGRI_T50, 'link_label': 'Vezi oferta Agricover', 'store': 'pagina modelului la dealerul autorizat Agricover',
     'art': drone_svg('40 L', 8, True),
     'keys': [('Rezervor stropire', '40 L'), ('Împrăștiere', '50 kg'), ('Debit', '16–24 L/min'), ('Productivitate', 'până la 21 ha/h')],
     'desc': """<p>T50 este modelul pe care îl vezi cel mai des la prestatorii din România, și pe bună dreptate: echilibrează capacitatea, productivitatea și prețul. Sistemul coaxial cu opt rotoare îl ține stabil cu 40 kg de soluție sau 50 kg de granule.</p>
<p>La stropit, sistemul dublu de atomizare dă 16 L/min pe două duze, sau 24 L/min cu kitul opțional de patru duze, pe o lățime de 4–11 m. La împrăștiere, rezervorul de 75 L și discul cu canale spiralate scot până la 108 kg/min, adică în jur de 1,5 tone de granule pe oră. Producătorul indică până la 21 ha/oră la stropit pe teren favorabil; în practică, cu realimentări și schimburi de baterii, calculează mai prudent.</p>
<p>Are radare cu fază (față și spate) pentru urmărirea terenului până la pante de 50°, mod de livadă și aplicare cu doză variabilă pe baza hărților de prescripție.</p>
<h2>Merită pentru tine?</h2><p>Este alegerea sigură dacă ai sau vrei să faci prestări pe câteva sute de hectare pe an. Dacă vei lucra mai ales în vii mici, T25P e mai practic; dacă vrei capacitate maximă, uită-te la T70P sau T100.</p>""",
     'pros': ['Raport foarte bun capacitate/preț', 'Stropit și împrăștiere pe aceeași platformă', 'Urmărire teren până la 50° și mod livadă', 'Cea mai mare rețea de prestatori și piese în România'],
     'cons': ['52 kg cu baterie: e nevoie de două persoane la încărcat', 'Pentru ritm continuu ai nevoie de 3 baterii și generator', 'Debitul de stropit e sub noile T55/T70P'],
     'specs': [('Rezervor stropire', '40 L · 40 kg'), ('Debit maxim', '16 L/min (2 duze) · 24 L/min (4 duze)'), ('Lățime de stropire', '4–11 m (la 3 m înălțime)'), ('Mărime picături', '50–500 μm'), ('Împrăștiere', '50 kg · rezervor 75 L · până la 108 kg/min · lățime 8 m'), ('Greutate', '39,9 kg fără baterie · 52 kg cu baterie'), ('Urmărire teren', 'pante de până la 50°')],
     'src': 'Sursa specificațiilor: fișa tehnică oficială DJI Agriculture (ag.dji.com/t50).',
     'spec': {'tank': [40, '40 L'], 'flow': [24, '16–24 L/min'], 'width': [11, '4–11 m'], 'sptank': [75, '75 L'], 'sprate': [108, '108 kg/min'], 'weight': [52, '52 kg'], 'price': [15525, '~15.500 €'], 'ideal': 'Culturi mari, prestatori'}},
    {'slug': 'dji-agras-t55', 'cmp_label': 'Agras T55', 'name': 'DJI Agras T55', 'brand': 'DJI', 'ribbon': 'Nou 2026',
     'title': 'DJI Agras T55: specificații, preț și diferențe față de T50', 'meta': 'DJI Agras T55, lansat în iulie 2026: 50 L la stropit, până la 50 L/min, 55 kg la împrăștiat. Ce aduce nou față de T50, pentru cine e și cum ceri ofertă.',
     'tagline': 'Urmașul T50: mai ușor, 50 L și un debit de până la 50 L/min.',
     'best_for': 'ferme medii și mari care vor un singur aparat pentru stropit, fertilizat și transport, cu setare rapidă.',
     'price': 'Preț la cerere', 'price_note': 'Model lansat global la 1 iulie 2026. Prețul pentru România se obține de la dealerii autorizați DJI Agras.',
     'link': 'https://ag.dji.com/t55', 'link_label': 'Fișa oficială', 'store': 'fișa oficială DJI Agriculture; oferta o ceri de la un dealer autorizat',
     'art': drone_svg('50 L', 4, True),
     'keys': [('Rezervor stropire', '50 L'), ('Împrăștiere', '55 kg'), ('Debit', '40–50 L/min'), ('Greutate', '45 kg')],
     'desc': """<p>Lansat global la 1 iulie 2026, T55 este practic noul „standard” DJI pentru fermele de mărime medie. Trece de la designul cu opt rotoare la patru brațe cu elice de 62 de inci, ceea ce îl face mai ușor: 45 kg cu rezervorul de 50 L și bateria DB1050, față de 52 kg la T50.</p>
<p>Debitul este marele salt: 40 L/min cu cele două duze centrifugale standard și până la 50 L/min cu patru duze de ceață, gândite pentru livezi. Lățimea efectivă rămâne 4–11 m. Sistemul de împrăștiere DS80L are rezervor de 80 L, duce 55 kg și descarcă până la 400 kg/min, iar kitul de ridicare transportă 40 kg pe cablu de 10 m.</p>
<p>Are un radar cu unde milimetrice care generează până la 250.000 de puncte pe secundă și mânere suplimentare pe cadru, ca un singur om să-l poată urca în mașină. Telecomanda este compatibilă cu T70P și T100.</p>
<h2>Merită pentru tine?</h2><p>Dacă alegi acum între un T50 și un T55, cere oferte pentru ambele: T55 lucrează mai repede la volume mari de soluție, iar T50 poate fi mai ieftin pe stocuri sau la mâna a doua.</p>""",
     'pros': ['Debit de până la 50 L/min, de peste două ori mai mare decât T50', 'Mai ușor decât T50, mai simplu de transportat', 'Stropit, împrăștiere și ridicare de sarcini', 'Telecomandă compatibilă cu T70P și T100'],
     'cons': ['Model nou: preț și disponibilitate variabile la dealeri', 'Încă puține unități second-hand', 'Sistemul de împrăștiere nu e compatibil cu cel de la T25P/T70P/T100'],
     'specs': [('Rezervor stropire', '50 L · 50 kg'), ('Debit maxim', '40 L/min (2 duze) · 50 L/min (4 duze de ceață)'), ('Lățime de stropire', '4–11 m'), ('Mărime picături', '50–500 μm'), ('Împrăștiere', '55 kg · rezervor 80 L · până la 400 kg/min · lățime 3–10 m'), ('Ridicare', '40 kg · cablu 10 m'), ('Greutate', '45 kg (cu rezervor 50 L și baterie DB1050)'), ('Baterie', 'DB1050: 20 Ah, 8,3 kg')],
     'src': 'Sursa: fișa tehnică oficială DJI (ag.dji.com/t55) și comunicatul de lansare DJI din 1 iulie 2026.',
     'spec': {'tank': [50, '50 L'], 'flow': [50, '40–50 L/min'], 'width': [11, '4–11 m'], 'sptank': [80, '80 L'], 'sprate': [400, '400 kg/min'], 'weight': [45, '45 kg'], 'price': 'La cerere', 'ideal': 'Ferme medii și mari'}},
    {'slug': 'dji-agras-t70p', 'cmp_label': 'Agras T70P', 'name': 'DJI Agras T70P', 'brand': 'DJI',
     'title': 'DJI Agras T70P: specificații, preț și pentru cine e', 'meta': 'DJI Agras T70P: rezervor de 70 L, 40 L/min, viteză de 20 m/s și 100 L la împrăștiere. Pentru ce ferme merită, diferențe față de T50 și T100.',
     'tagline': '70 de litri și 40 L/min: pentru prestatorii care vor hectare multe pe zi.',
     'best_for': 'prestatori profesioniști și ferme de peste 1.000 ha tratate pe an.',
     'price': 'Preț la cerere', 'price_note': 'Prețul pentru România se obține de la dealerii autorizați DJI Agras.',
     'link': 'https://ag.dji.com/t70p', 'link_label': 'Fișa oficială', 'store': 'fișa oficială DJI Agriculture; oferta o ceri de la un dealer autorizat',
     'art': drone_svg('70 L', 8, True, '#22303c'),
     'keys': [('Rezervor stropire', '70 L'), ('Împrăștiere', 'rezervor 100 L'), ('Debit', '40 L/min'), ('Viteză', '20 m/s')],
     'desc': """<p>T70P este treapta dintre T50/T55 și uriașul T100. Rezervorul de 70 L și debitul de 40 L/min (cu 87,5% mai mult decât T50) îl fac potrivit pentru tratamente la volum mare de soluție pe suprafețe întinse, iar viteza de lucru de până la 20 m/s scurtează timpul pe parcelele lungi.</p>
<p>La împrăștiere are rezervor de 100 L și o lățime de 10 m, cu descărcare de până la 400 kg/min. Poate ridica 65 kg cu kitul de transport, util în livezi și în zone fără acces cu utilaje.</p>
<h2>Merită pentru tine?</h2><p>Merită dacă faci prestări la scară și echipa ta poate ține ritmul la realimentare (apă, soluție, baterii). Pentru o fermă obișnuită, T55 oferă un debit similar la un gabarit mai mic.</p>""",
     'pros': ['Capacitate mare: mai puține realimentări', 'Debit de 40 L/min la stropit', 'Viteză de lucru de 20 m/s', 'Kit de ridicare de 65 kg'],
     'cons': ['Aparat mare: transport și logistică mai complicate', 'Cere generator și baterii mai multe pentru lucru continuu', 'Fără preț public în România'],
     'specs': [('Rezervor stropire', '70 L'), ('Debit maxim', '40 L/min'), ('Viteză maximă de lucru', '20 m/s'), ('Împrăștiere', 'rezervor 100 L · până la 400 kg/min · lățime 10 m'), ('Ridicare', '65 kg'), ('Elice', '62 inch')],
     'src': 'Sursa: informațiile oficiale DJI Agriculture despre Agras T70P.',
     'spec': {'tank': [70, '70 L'], 'flow': [40, '40 L/min'], 'width': None, 'sptank': [100, '100 L'], 'sprate': [400, '400 kg/min'], 'weight': None, 'price': 'La cerere', 'ideal': 'Prestatori, >1.000 ha/an'}},
    {'slug': 'dji-agras-t100', 'cmp_label': 'Agras T100', 'name': 'DJI Agras T100', 'brand': 'DJI', 'ribbon': 'Cel mai mare',
     'title': 'DJI Agras T100: preț, specificații și când merită', 'meta': 'DJI Agras T100: 100 L la stropit, 150 L la împrăștiat, lățime de până la 13 m și LiDAR. Pentru ce ferme are sens și unde ceri ofertă în România.',
     'tagline': 'Vârful gamei: 100 L de soluție, 150 L la împrăștiere și LiDAR.',
     'best_for': 'ferme foarte mari, prestatori cu flotă și lucrări de împrăștiere la volum mare.',
     'price': 'Preț la cerere', 'price_note': 'Disponibil prin dealerii autorizați din România (de ex. Titan Machinery). Prețul depinde mult de pachet.',
     'link': TITAN, 'link_label': 'Cere oferta la dealer', 'store': 'pagina de drone a dealerului autorizat Titan Machinery România',
     'art': drone_svg('100 L', 8, True, '#1b2631'),
     'keys': [('Rezervor stropire', '100 L'), ('Împrăștiere', 'rezervor 150 L'), ('Debit', '30–40 L/min'), ('Lățime', 'până la 13 m')],
     'desc': """<p>T100 este cea mai mare dronă agricolă DJI. Duce 100 L la stropit, are lățime de lucru de 5–13 m și debit de 30 L/min pe două duze sau 40 L/min pe patru. La împrăștiere, rezervorul de 150 L descarcă până la 400 kg/min, iar kitul de ridicare duce 80 kg.</p>
<p>Pentru siguranță folosește LiDAR și sistemul de viziune Penta-Vision. Din iulie 2026 există și varianta cu sistem de stropit cu baterie dublă, care crește timpul de zbor la sarcină egală, cu un rezervor de 90 L.</p>
<p>Dealerii din România oferă pachete cu stație de încărcare, generator și prima inspecție de service la 300 de ore de funcționare.</p>
<h2>Merită pentru tine?</h2><p>Doar dacă ai volum mare de lucru și echipă pentru logistică. Pentru majoritatea fermelor, două drone mai mici (de ex. T50/T55) dau mai multă flexibilitate decât un singur T100.</p>""",
     'pros': ['Cea mai mare capacitate din piață la DJI', 'Lățime de lucru de până la 13 m', 'LiDAR și Penta-Vision pentru obstacole', 'Ideal pentru împrăștiere la volum mare'],
     'cons': ['Investiție mare și logistică grea', 'Nu e practic pe parcele mici', 'Consum mare de energie: generator obligatoriu'],
     'specs': [('Rezervor stropire', '100 L (90 L în varianta cu baterie dublă)'), ('Debit maxim', '30 L/min (2 duze) · 40 L/min (4 duze)'), ('Lățime de stropire', '5–13 m'), ('Împrăștiere', 'rezervor 150 L · până la 400 kg/min'), ('Ridicare', '80 kg'), ('Siguranță', 'LiDAR + Penta-Vision')],
     'src': 'Sursa: informațiile oficiale DJI Agriculture despre Agras T100 și comunicatul DJI din 1 iulie 2026.',
     'spec': {'tank': [100, '100 L'], 'flow': [40, '30–40 L/min'], 'width': [13, '5–13 m'], 'sptank': [150, '150 L'], 'sprate': [400, '400 kg/min'], 'weight': None, 'price': 'La cerere', 'ideal': 'Ferme foarte mari, flote'}},
    {'slug': 'xag-p150-max', 'name': 'XAG P150 Max', 'brand': 'XAG', 'ribbon': 'Alternativa la DJI',
     'title': 'XAG P150 Max: specificații, preț și comparație cu DJI', 'meta': 'XAG P150 Max, principala alternativă la DJI Agras: rezervor de 80 L, 32 L/min, 300 kg/min la împrăștiere și control a două drone de un singur pilot.',
     'tagline': 'Principalul rival al DJI: 80 L, sisteme modulare și zbor în roi.',
     'best_for': 'ferme mari și prestatori care vor o alternativă la DJI sau lucrează deja cu ecosistemul XAG.',
     'price': 'Preț la cerere', 'price_note': 'În SUA kitul de bază s-a vândut în jur de 21.700 $. În România, cere ofertă de la un distribuitor XAG.',
     'link': 'https://www.xa.com/en/p150max', 'link_label': 'Fișa oficială', 'store': 'fișa oficială XAG; oferta o ceri de la un distribuitor',
     'art': drone_svg('80 L', 4, True, '#3a3f45'),
     'keys': [('Rezervor stropire', '80 L'), ('Împrăștiere', 'rezervor 115 L'), ('Debit', '32 L/min'), ('Lățime', '5–10 m')],
     'desc': """<p>XAG este al doilea mare producător de drone agricole, iar P150 Max este modelul său de vârf. Sistemul de stropit RevoSpray 5 are un rezervor inteligent de 80 L și două duze centrifugale care dau 32 L/min, cu picături între 60 și 500 μm și lățime de lucru de 5–10 m.</p>
<p>Punctul forte este modularitatea: același aparat schimbă în câteva minute sistemul de stropit cu cel de împrăștiere (rezervor de 115 L, până la 300 kg/min), cu cartografierea sau cu transportul de marfă. Un singur operator poate controla două drone simultan, ceea ce dublează productivitatea unei echipe.</p>
<p>Viteza maximă este de 20 m/s, iar producătorul raportează 20–24 ha/oră în condiții tipice de stropit.</p>
<h2>Merită pentru tine?</h2><p>Merită dacă găsești un distribuitor cu service aproape de tine: rețeaua XAG în România este mult mai mică decât cea DJI, iar disponibilitatea pieselor contează mai mult decât o diferență de specificații.</p>""",
     'pros': ['Rezervor de 80 L și debit de 32 L/min', 'Sisteme modulare schimbabile rapid', 'Un pilot poate opera două drone', 'Construcție robustă, protecție IPX6K'],
     'cons': ['Rețea de dealeri și service mai mică în România', 'Gabarit mare (peste 3 m desfăcut)', 'Mai puține drone second-hand pe piață'],
     'specs': [('Rezervor stropire', '80 L (RevoSpray 5)'), ('Debit maxim', '32 L/min'), ('Lățime de stropire', '5–10 m'), ('Mărime picături', '60–500 μm'), ('Împrăștiere', 'rezervor 115 L · până la 300 kg/min'), ('Greutate', '56 kg (cu RevoSpray și baterii)'), ('Viteză maximă', '20 m/s')],
     'src': 'Sursa: fișa tehnică oficială XAG (xa.com/en/p150max).',
     'spec': {'tank': [80, '80 L'], 'flow': [32, '32 L/min'], 'width': [10, '5–10 m'], 'sptank': [115, '115 L'], 'sprate': [300, '300 kg/min'], 'weight': [56, '56 kg'], 'price': 'La cerere', 'ideal': 'Alternativă la DJI'}},
    {'slug': 'dji-mavic-3-multispectral', 'name': 'DJI Mavic 3 Multispectral', 'brand': 'DJI', 'compare': False, 'ribbon': 'Monitorizare culturi',
     'title': 'DJI Mavic 3 Multispectral: preț, ce face și pentru cine', 'meta': 'DJI Mavic 3M pentru agricultură: cameră RGB de 20 MP și 4 camere multispectrale, până la 200 ha pe zbor, RTK. Preț orientativ în Europa ~4.500 €.',
     'tagline': 'Drona care îți arată unde are nevoie cultura de tratament, înainte să stropești.',
     'best_for': 'agricultură de precizie: hărți NDVI, aplicare cu doză variabilă, monitorizarea culturilor și consultanță.',
     'price': '~4.500 €', 'price_eur': 4480, 'price_note': 'Preț orientativ în magazinele din UE. Disponibil în România și prin Agricover și Titan Machinery.',
     'link': AGRI_M3M, 'link_label': 'Vezi oferta Agricover', 'store': 'pagina modelului la dealerul autorizat Agricover',
     'art': drone_svg('M3M', 4, False, '#39424c', mapper=True),
     'keys': [('Acoperire', 'până la 200 ha/zbor'), ('Cameră RGB', '20 MP'), ('Multispectral', '4 × 5 MP'), ('Poziționare', 'RTK')],
     'desc': """<p>Mavic 3 Multispectral nu stropește: este „ochiul” fermei. Combină o cameră RGB de 20 MP (senzor 4/3) cu patru camere multispectrale de 5 MP (verde, roșu, red edge și infraroșu apropiat), din care obții hărți de vegetație de tip NDVI sau GNDVI.</p>
<p>Acoperă până la 200 de hectare într-un zbor, iar modulul RTK inclus dă poziționare la nivel de centimetru fără puncte de control la sol. Hărțile rezultate pot fi transformate în hărți de prescripție pe care o dronă Agras le aplică cu doză variabilă, adică pui îngrășământ sau tratament doar unde e nevoie.</p>
<h2>Merită pentru tine?</h2><p>Este cea mai ieftină cale de a intra în agricultura de precizie și se amortizează rapid dacă reduce chiar și puțin cantitatea de input pe sute de hectare. Pentru prestatori, este un serviciu în plus pe care îl pot vinde.</p>""",
     'pros': ['Preț mic față de dronele de stropit', 'Până la 200 ha cartografiate pe zbor', 'RTK inclus: precizie fără puncte la sol', 'Lucrează cu hărțile de prescripție DJI'],
     'cons': ['Nu stropește și nu împrăștie', 'Ai nevoie de software (DJI Terra / SmartFarm) și timp de analiză', 'Rezultatele depind de condițiile de lumină'],
     'specs': [('Cameră RGB', '20 MP, senzor 4/3'), ('Camere multispectrale', '4 × 5 MP (G, R, RE, NIR)'), ('Acoperire', 'până la 200 ha pe zbor'), ('Poziționare', 'modul RTK, precizie centimetrică'), ('Transmisie', 'O3 Enterprise, până la 8 km (CE)')],
     'src': 'Sursa: informațiile oficiale DJI și paginile dealerilor autorizați.',
     'spec': {}},
]

COMPARE_ROWS = [
    ('Rezervor stropire', 'tank', 'max'), ('Debit maxim stropire', 'flow', 'max'), ('Lățime maximă de stropire', 'width', 'max'),
    ('Rezervor împrăștiere', 'sptank', 'max'), ('Debit împrăștiere', 'sprate', 'max'), ('Greutate cu baterie', 'weight', 'min'),
    ('Preț de pornire', 'price', 'min'), ('Ideal pentru', 'ideal'),
]
HOME_BODY = """<div class="picks">
<a href="/dji-agras-t25p.html"><span>Vii, livezi, parcele mici</span><b>DJI Agras T25P →</b></a>
<a href="/dji-agras-t50.html"><span>Culturi mari, prestări</span><b>DJI Agras T50 →</b></a>
<a href="/dji-agras-t55.html"><span>Nou în 2026</span><b>DJI Agras T55 →</b></a>
<a href="/dji-mavic-3-multispectral.html"><span>Hărți NDVI, precizie</span><b>Mavic 3 Multispectral →</b></a></div>
<section class="sec" id="modele"><h2>Dronele agricole pe care le recomandăm în 2026</h2>
<p>Am ales modelele care se vând și au service în România, plus principala alternativă la DJI. Fiecare are o pagină cu descriere detaliată, specificații, avantaje, limite și linkul direct către dealer.</p>
{{PRODUCTS}}</section>
{{COMPARE}}
<section class="sec"><h2>Înainte să stropești: drona care vede cultura</h2>
<div class="split"><div>{{EXTRA_PRODUCTS}}</div><div><p>O dronă multispectrală îți arată, pe hartă, zonele în care cultura e stresată, bolnavă sau are nevoie de azot. Din harta respectivă faci o prescripție, iar drona de stropit aplică doza variabil: mai mult unde trebuie, deloc unde nu e nevoie.</p>
<p>Pentru o fermă de câteva sute de hectare, economia de input poate acoperi rapid prețul dronei. Pentru prestatori, cartografierea este un serviciu în plus pe care îl pot factura.</p></div></div></section>
<section class="sec"><h2>Cum alegi în 3 întrebări</h2>
<div class="grid3"><div class="box info" style="margin:0"><b>1. Câte hectare tratezi pe an?</b><p class="note" style="margin:6px 0 0">Sub ~200 ha: T25P sau un prestator. Câteva sute: T50/T55. Peste 1.000 ha: T70P, T100 sau două drone.</p></div>
<div class="box info" style="margin:0"><b>2. Ce cultură și ce teren?</b><p class="note" style="margin:6px 0 0">Vii, livezi și pante cer o dronă ușoară și manevrabilă. Culturile mari și plane răsplătesc rezervorul mare.</p></div>
<div class="box info" style="margin:0"><b>3. Unde e cel mai apropiat service?</b><p class="note" style="margin:6px 0 0">Un sezon pierdut costă mai mult decât diferența de preț. Alege dealerul cu piese și service aproape de tine.</p></div></div></section>
<section class="sec"><div class="box"><b>Nu știi dacă merită să cumperi?</b> Folosește <a href="/calculator-cost-hectar.html">calculatorul de cost pe hectar</a>: compară drona proprie cu un prestator și cu tractorul, cu cifrele fermei tale.</div>
<div class="box"><b>Ce spune legea în 2026.</b> Aplicarea produselor de protecție a plantelor cu drona se face cu operatori autorizați de AACR și pe baza unei notificări la Oficiul Fitosanitar Județean. <a href="/legislatie-drone-agricole-2026.html">Detalii →</a></div></section>
""" + LEAD + """
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/cat-costa-o-drona-agricola.html"><span class="tag">Prețuri</span><b>Cât costă o dronă agricolă</b><span>Ce conține un pachet și costurile la care nu te gândești.</span></a>
<a class="c" href="/dji-agras-comparatie.html"><span class="tag">Comparație</span><b>DJI Agras: ce model alegi</b><span>Diferențele care contează în practică.</span></a>
<a class="c" href="/drona-vs-tractor.html"><span class="tag">Analiză</span><b>Dronă sau tractor?</b><span>Avantaje, limite și când merită fiecare.</span></a>
<a class="c" href="/legislatie-drone-agricole-2026.html"><span class="tag">Lege</span><b>Legislația dronelor agricole 2026</b><span>AACR, notificarea fitosanitară și ce se schimbă.</span></a></div>
<p class="disc">Ilustrațiile sunt schematice, nu fotografii ale produselor. Prețurile sunt orientative și se pot schimba; confirmă oferta la dealer. Unele linkuri pot fi de afiliere: dacă cumperi prin ele putem primi un comision, fără cost în plus pentru tine.</p></section>"""

FAQ = [
    ('Am voie să stropesc cu drona în România?', 'Da, în condițiile actuale: cu un operator care are certificat de competență AACR, pe baza unei notificări transmise Oficiului Fitosanitar Județean și numai cu produse de protecție a plantelor autorizate pentru aplicare cu drona. Regulile sunt în curs de simplificare, așa că verifică stadiul legii înainte de sezon.'),
    ('Cât costă o dronă agricolă?', 'Pachetele de bază pornesc de la aproximativ 9.100 de euro fără TVA, iar modelele mari, cu baterii suplimentare, stație de încărcare și generator, pot ajunge la circa 60.000 de euro.'),
    ('Câte hectare stropește o dronă pe oră?', 'Depinde de model, de doza de soluție la hectar și de forma parcelei. Pentru DJI Agras T50, producătorul indică până la 21,3 ha/oră pe teren drept; în practică, cu realimentări și schimburi de baterii, randamentul este mai mic.'),
]

ART_LEG = """<p>România este una dintre piețele importante din UE pentru dronele agricole, dar regulile de folosire sunt încă în schimbare. Iată ce se aplică acum și ce urmează.</p>
<h2>Regula de bază: operator AACR + notificare fitosanitară</h2>
<p>Fermierii, persoane fizice sau juridice, pot aplica produse de protecție a plantelor cu drona doar prin operatori autorizați de Autoritatea Aeronautică Civilă Română (AACR) și pe baza unei notificări transmise Oficiului Fitosanitar Județean. Operatorul trebuie să aibă certificat de competență AACR pentru clasa de dronă folosită.</p>
<h2>Ce produse se pot aplica</h2><p>Doar produsele autorizate în acest scop de Autoritatea Națională Fitosanitară, pe baza unor studii de eficiență și siguranță pentru aplicarea aeriană cu aparate fără pilot. În situații speciale, precum invazii de dăunători sau terenuri greu accesibile, notificările pot fi depuse cu o zi înainte.</p>
<h2>Ce se schimbă: proiectul din Senat și regulile UE</h2>
<ul><li>În Comisia pentru agricultură a Senatului se află un proiect care ar introduce un regim de <strong>„simplă notificare”</strong>, condiționat de folosirea produselor autorizate și de înregistrarea dronelor la AACR.</li>
<li>La nivel european se lucrează la relaxarea regulilor pentru stropitul cu drone; procedura ar urma să se încheie între finalul lui 2026 și începutul lui 2027, iar actele delegate privind tipurile de drone eligibile vor fi pasul decisiv.</li>
<li>Organizațiile de apicultori și de mediu (ROMAPIS, WWF România, Greenpeace România) au cerut prudență la aplicarea aeriană a pesticidelor. Merită să anunți apicultorii din zonă înainte de tratamente.</li></ul>
<h2>Pașii practici înainte de sezon</h2><ol><li>Alegi un prestator cu operatori certificați sau îți certifici propriul operator.</li><li>Verifici dacă produsul folosit este autorizat pentru aplicare cu drona.</li><li>Transmiți notificarea la Oficiul Fitosanitar Județean în termenul cerut.</li><li>Păstrezi evidența tratamentelor (registrul de tratamente).</li><li>Verifici asigurarea de răspundere civilă a operatorului.</li></ol>
<div class="box info">Regulile se schimbă rapid. Actualizăm acest ghid la fiecare modificare; ultima verificare: noiembrie 2026.</div>"""

ART_PRET = """<p>Prețul unei drone agricole depinde mai puțin de drona propriu-zisă și mai mult de pachet: câte baterii primești, ce stație de încărcare, dacă include generator, stație RTK, instruire și service.</p>
<h2>Intervale de preț în 2026</h2>
<div class="tw"><table class="t"><tr><th>Categorie</th><th>Preț orientativ</th><th>Pentru cine</th></tr>
<tr><td>Pachete de bază (drone de 20–30 L)</td><td>de la ~9.100 € fără TVA</td><td>Ferme mici, vie, livezi, prestatori la început</td></tr>
<tr><td>Clasa medie (40–50 L)</td><td>zeci de mii de euro, în funcție de pachet</td><td>Ferme mari și prestatori</td></tr>
<tr><td>Clasa mare (70–100 L)</td><td>până la ~60.000 €</td><td>Prestatori cu suprafețe mari, transport de sarcini</td></tr></table></div>
<p class="note">Un exemplu public: o ofertă din octombrie 2026 pornea de la 9.138,30 euro fără TVA pentru un pachet de dronă. Pe piața second-hand apar și DJI Agras T50 la peste 60.000 de lei.</p>
<h2>Ce conține un pachet complet</h2><p>Pentru un model mare (exemplu DJI Agras T100 la un dealer din România): drona, stația de încărcare C12000, 3 baterii de zbor, telecomanda cu încărcător și baterii, modul 4G, repetor de semnal, stație RTK mobilă și un generator trifazat. Fără baterii suficiente și generator, drona stă la sol mai mult decât zboară.</p>
<h2>Costuri ascunse de luat în calcul</h2><ul><li><strong>Bateriile</strong> au un număr limitat de cicluri și sunt cea mai scumpă piesă de schimb.</li><li><strong>Certificarea operatorului</strong> și instruirea de pilotaj.</li><li><strong>Asigurarea</strong> de răspundere civilă.</li><li><strong>Service-ul</strong>: prima revizie poate fi cerută după un număr de ore sau de zile de la livrare.</li></ul>
<div class="box info">Vezi dacă drona proprie se amortizează la suprafața ta cu <a href="/calculator-cost-hectar.html">calculatorul de cost pe hectar</a>.</div>"""

ART_DJI = """<p>DJI domină piața dronelor agricole: flota sa globală a trecut de 600.000 de unități în 2026. În România, gama Agras se vinde prin dealeri autorizați. Iată cum se diferențiază modelele actuale.</p>
<h2>Gama Agras pe scurt</h2>
<div class="tw"><table class="t"><tr><th>Model</th><th>Rezervor stropit</th><th>Potrivit pentru</th></tr>
<tr><td>Agras T25 / T25P</td><td>~20 L</td><td>Parcele mici, vie, livezi; portabil, încape într-o mașină obișnuită</td></tr>
<tr><td>Agras T50</td><td>~40 L</td><td>Ferme mari și prestatori; până la 21,3 ha/oră pe teren drept, după producător</td></tr>
<tr><td>Agras T70P</td><td>~70 L</td><td>Prestatori cu volume mari</td></tr>
<tr><td>Agras T100</td><td>100 L</td><td>Suprafețe foarte mari; configurabil pentru stropit, împrăștiat granule și transport</td></tr></table></div>
<p class="note">Capacitățile sunt orientative; verifică fișa tehnică oficială și configurația exactă oferită de dealer.</p>
<h2>Cum alegi</h2><ol><li><strong>Forma parcelelor:</strong> pe parcele mici și neregulate, o dronă mai mică e mai eficientă, pentru că întoarce și realimentează des oricum.</li><li><strong>Volumul de soluție la hectar:</strong> dacă tratamentele tale cer volume mari, rezervorul contează mai mult decât viteza.</li><li><strong>Logistica:</strong> dronele mari cer generator trifazat și o echipă la sol.</li><li><strong>Service local:</strong> alege un dealer cu piese și asistență în zonă.</li></ol>
<h2>Alternative</h2><p>Pe lângă DJI există și alți producători, majoritatea asiatici, plus drone de cartografiere (de ex. DJI Mavic 3 Multispectral sau Matrice 350 RTK) folosite pentru hărți de stropire localizată, care reduc cantitatea de produs aplicat.</p>"""

ART_VS = """<p>Drona nu înlocuiește complet tractorul, dar îl bate în câteva situații clare. Iată o comparație cinstită.</p>
<h2>Unde câștigă drona</h2><ul><li><strong>Fără tasarea solului</strong> și fără urme de roți în cultură.</li><li><strong>Intră pe teren ud</strong> sau în pantă, unde tractorul nu poate.</li><li><strong>Volum mic de apă</strong> la hectar și precizie mare.</li><li><strong>Mai puțină forță de muncă:</strong> zborul se planifică pe telecomandă, iar drona revine singură la punctul de decolare.</li><li><strong>Rezultate măsurate:</strong> la stropitul viței-de-vie în România, folosirea dronei a redus cantitatea de produse de protecție cu 53%.</li></ul>
<h2>Unde câștigă tractorul</h2><ul><li>Parcele mari și plane, cu volum mare de soluție.</li><li>Produse care nu sunt autorizate pentru aplicare aeriană.</li><li>Zile cu vânt puternic, când drona nu poate lucra corect.</li></ul>
<h2>Costul pe hectar</h2><p>Un fermier citat de presă estima carburantul pentru un hectar lucrat cu utilajul la circa 100 de lei, în timp ce încărcarea bateriilor dronei costă mult mai puțin. Diferența reală depinde însă de amortizare: o dronă scumpă folosită pe puține hectare poate ieși mai scumpă decât tractorul.</p>
<div class="box info">Pune cifrele fermei tale în <a href="/calculator-cost-hectar.html">calculatorul dronă vs tractor vs prestator</a>.</div>"""

SITE = {
    'name': 'DronaAgricolă', 'domain': 'dronaagricola.online',
    'c1': '#2f6b1f', 'c2': '#6aa84f', 'accent': '#f1c232',
    'mark': '<g fill="#fff"><rect x="26" y="28" width="12" height="9" rx="3"/><rect x="10" y="31" width="44" height="3" rx="1.5"/><circle cx="12" cy="24" r="5" fill="none" stroke="#fff" stroke-width="3"/><circle cx="52" cy="24" r="5" fill="none" stroke="#fff" stroke-width="3"/></g><path d="M24 44l-3 8M32 44v9M40 44l3 8" stroke="#f1c232" stroke-width="3" stroke-linecap="round"/>',
    'tagline': 'Dronele agricole din România, pe înțeles: modele, prețuri, comparații și unde le cumperi.',
    'badges': ['7 modele analizate', 'Prețuri orientative România', 'Linkuri directe la dealeri'],
    'products': PRODUCTS, 'compare_rows': COMPARE_ROWS, 'compare_default': ['dji-agras-t25p', 'dji-agras-t50', 'dji-agras-t55'],
    'aff_short': 'Unele linkuri pot fi de afiliere; nu plătești nimic în plus.', 'side_href': '/#compara', 'side_btn': 'Compară modelele',
    'nav': [('/#modele', 'Modele'), ('/#compara', 'Compară'), ('/calculator-cost-hectar.html', 'Calculator'), ('/legislatie-drone-agricole-2026.html', 'Legislație'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator dronă vs prestator vs tractor',
    'side_title': 'Ce dronă ți se potrivește?', 'side_text': 'Pune față în față oricare trei modele: capacitate, debit, preț.',
    'about': '<p>DronaAgricolă este un site independent pentru fermierii și prestatorii din România interesați de dronele agricole: costuri reale, legislație și comparații de modele, explicate pe înțelesul tuturor.</p><h2>Sursele noastre</h2><p>Comunicări AACR și ale Autorității Naționale Fitosanitare, proiectele legislative publice, fișele tehnice ale producătorilor și ofertele publice ale dealerilor din România.</p><p>Nu vindem drone. Putem primi un comision de la prestatorii sau dealerii recomandați, fără cost suplimentar pentru tine.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Drone agricole 2026: modele, prețuri și comparație', 'kind': 'home', 'short': 'Modele și comparație',
         'desc': 'Cele mai bune drone agricole în România în 2026: DJI Agras T25P, T50, T55, T70P, T100, XAG P150 Max și Mavic 3M. Specificații, prețuri și linkuri la dealeri.',
         'h1': 'Drone agricole 2026: ce model alegi și cât costă',
         'lead': 'Modelele care contează în România, explicate pe înțeles, cu prețuri orientative, linkuri directe la dealeri și o comparație față în față.', 'body': HOME_BODY, 'faq': FAQ},
        {'slug': 'calculator-cost-hectar', 'title': 'Calculator cost stropit cu drona: dronă, prestator sau tractor', 'kind': 'tool', 'short': 'Calculator cost pe hectar', 'appcat': 'BusinessApplication',
         'desc': 'Calculează dacă merită o dronă agricolă proprie, un prestator sau tractorul: cost pe hectar, prag de rentabilitate și zile de lucru.',
         'h1': 'Calculator: dronă proprie, prestator sau tractor?', 'toolname': 'Calculator cost stropit cu drona', 'crumb': 'Calculator',
         'lead': 'Compară costul pe hectar al unei drone proprii, al unui prestator și al tractorului, cu cifrele fermei tale.', 'body': CALC_BODY},
        {'slug': 'legislatie-drone-agricole-2026', 'title': 'Legislația dronelor agricole în România (2026)', 'kind': 'article', 'short': 'Legislația 2026',
         'desc': 'Ce trebuie să știi ca să stropești legal cu drona în 2026: operator certificat AACR, notificare la Oficiul Fitosanitar, produse autorizate și proiectul din Senat.',
         'h1': 'Legislația dronelor agricole în România, 2026', 'lead': 'Reguli actuale, schimbările în pregătire și pașii practici înainte de sezon.', 'body': ART_LEG},
        {'slug': 'cat-costa-o-drona-agricola', 'title': 'Cât costă o dronă agricolă în 2026: prețuri și pachete', 'kind': 'article', 'short': 'Cât costă o dronă',
         'desc': 'Prețuri orientative pentru drone agricole în România: de la pachete de ~9.100 € fără TVA la modele de 60.000 €. Ce conține un pachet și ce costuri ascunse apar.',
         'h1': 'Cât costă o dronă agricolă în 2026', 'lead': 'Intervale de preț, conținutul unui pachet complet și costurile la care nu te gândești.', 'body': ART_PRET},
        {'slug': 'dji-agras-comparatie', 'title': 'DJI Agras T25P vs T50 vs T70P vs T100: comparație', 'kind': 'article', 'short': 'Comparație DJI Agras',
         'desc': 'Comparația modelelor DJI Agras disponibile în România: capacitate rezervor, productivitate și pentru ce fermă se potrivește fiecare.',
         'h1': 'DJI Agras T25P, T50, T70P și T100: ce model alegi', 'lead': 'Diferențele care contează în practică și criteriile de alegere.', 'body': ART_DJI},
        {'slug': 'drona-vs-tractor', 'title': 'Dronă sau tractor pentru stropit? Comparație practică', 'kind': 'article', 'short': 'Dronă sau tractor?',
         'desc': 'Când merită drona și când rămâne mai bun tractorul la tratamentele fitosanitare: tasare, pantă, volum de apă, cost pe hectar și reducerea pesticidelor.',
         'h1': 'Dronă sau tractor pentru tratamente?', 'lead': 'Avantajele reale ale dronei, limitele ei și cum compari costurile.', 'body': ART_VS},
    ]
}
