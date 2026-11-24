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

INDEX_BODY = TOOL + """
<section class="sec"><h2>Merită o dronă agricolă în ferma ta?</h2>
<p>Dronele de stropit au intrat în fermele din România pe partea de viță-de-vie, livezi, terenuri în pantă și culturi mari unde tractorul tasează solul sau nu poate intra după ploaie. Jucătorii din piață estimează reduceri ale costurilor operaționale de 30–40% față de un utilaj clasic, plus mai puțină forță de muncă.</p>
<p>Calculul de mai sus îți arată cât costă hectarul tratat în trei variante. Pe scurt:</p>
<ul><li><strong>Sub câteva sute de hectare tratate pe an</strong>, prestatorul este aproape întotdeauna mai ieftin decât o dronă proprie.</li>
<li><strong>Peste pragul de rentabilitate</strong>, drona proprie câștigă, mai ales dacă faci și fertilizare granulară, semănat de culturi de acoperire sau prestări pentru vecini.</li>
<li><strong>Tractorul rămâne competitiv</strong> pe parcele mari și plane, cu volum mare de soluție la hectar.</li></ul></section>
<div class="box"><b>Ce spune legea în 2026.</b> Aplicarea produselor de protecție a plantelor cu drona se face cu operatori autorizați de AACR și pe baza unei notificări la Oficiul Fitosanitar Județean, cu produse autorizate pentru aplicare aeriană. Un proiect aflat în Senat propune un regim de „simplă notificare”. <a href="/legislatie-drone-agricole-2026.html">Detalii →</a></div>
""" + LEAD + """
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/legislatie-drone-agricole-2026.html"><span class="tag">Lege</span><b>Legislația dronelor agricole 2026</b><span>AACR, notificarea fitosanitară și ce se schimbă.</span></a>
<a class="c" href="/cat-costa-o-drona-agricola.html"><span class="tag">Prețuri</span><b>Cât costă o dronă agricolă</b><span>De la pachete de bază la modelele de 100 de litri.</span></a>
<a class="c" href="/dji-agras-comparatie.html"><span class="tag">Comparație</span><b>DJI Agras T25P, T50, T70P, T100</b><span>Ce model pentru ce suprafață.</span></a>
<a class="c" href="/drona-vs-tractor.html"><span class="tag">Analiză</span><b>Dronă sau tractor?</b><span>Avantaje, limite și când merită fiecare.</span></a></div></section>"""

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
<div class="box info">Vezi dacă drona proprie se amortizează la suprafața ta cu <a href="/">calculatorul de cost pe hectar</a>.</div>"""

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
<div class="box info">Pune cifrele fermei tale în <a href="/">calculatorul dronă vs tractor vs prestator</a>.</div>"""

SITE = {
    'name': 'DronaAgricolă', 'domain': 'dronaagricola.online',
    'c1': '#2f6b1f', 'c2': '#6aa84f', 'accent': '#f1c232',
    'mark': '<g fill="#fff"><rect x="26" y="28" width="12" height="9" rx="3"/><rect x="10" y="31" width="44" height="3" rx="1.5"/><circle cx="12" cy="24" r="5" fill="none" stroke="#fff" stroke-width="3"/><circle cx="52" cy="24" r="5" fill="none" stroke="#fff" stroke-width="3"/></g><path d="M24 44l-3 8M32 44v9M40 44l3 8" stroke="#f1c232" stroke-width="3" stroke-linecap="round"/>',
    'tagline': 'Totul despre dronele agricole în România: costuri pe hectar, legislație, modele și prestatori.',
    'badges': ['Legislație actualizată 2026', 'Calculator cost pe hectar', 'Fără cont'],
    'nav': [('/', 'Calculator'), ('/cat-costa-o-drona-agricola.html', 'Prețuri'), ('/dji-agras-comparatie.html', 'Modele'), ('/legislatie-drone-agricole-2026.html', 'Legislație'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Calculator dronă vs prestator vs tractor',
    'side_title': 'Cât te costă hectarul?', 'side_text': 'Compară drona proprie, prestatorul și tractorul.',
    'about': '<p>DronaAgricolă este un site independent pentru fermierii și prestatorii din România interesați de dronele agricole: costuri reale, legislație și comparații de modele, explicate pe înțelesul tuturor.</p><h2>Sursele noastre</h2><p>Comunicări AACR și ale Autorității Naționale Fitosanitare, proiectele legislative publice, fișele tehnice ale producătorilor și ofertele publice ale dealerilor din România.</p><p>Nu vindem drone. Putem primi un comision de la prestatorii sau dealerii recomandați, fără cost suplimentar pentru tine.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Drone agricole: cost pe hectar, prețuri și legislație 2026', 'kind': 'tool', 'short': 'Calculator cost pe hectar', 'appcat': 'BusinessApplication',
         'desc': 'Calculează dacă merită o dronă agricolă proprie, un prestator sau tractorul: cost pe hectar, prag de rentabilitate și zile de lucru. Plus legislația 2026.',
         'h1': 'Drone agricole: merită la ferma ta?', 'toolname': 'Calculator cost stropit cu drona',
         'lead': 'Compară în câteva secunde costul pe hectar al unei drone proprii, al unui prestator și al tractorului, cu cifrele fermei tale.', 'body': INDEX_BODY, 'faq': FAQ},
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
