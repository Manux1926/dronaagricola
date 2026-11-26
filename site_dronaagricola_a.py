# Artículos y correcciones del 26 nov 2026 (build.py los carga si existe este archivo).
# Corrección importante: la aplicación de fitosanitarios con dron NO tiene todavía marco legal propio en Rumanía;
# el régimen de "operador AACR + notificación" es el del proyecto de ley pendiente en la Cámara de Diputados.

LEG_BODY = """<p>Dronele agricole se vând liber în România, iar mulți fermieri le folosesc deja. Situația legală a <strong>stropitului cu produse de protecție a plantelor</strong> este însă neclară. Iată ce se știe în noiembrie 2026, ce prevede proiectul de lege și ce poți face în siguranță până la clarificare.</p>
<div class="box info"><b>Pe scurt:</b> la nivelul UE, pulverizarea aeriană a pesticidelor este interzisă în principiu, cu derogări strict aprobate. În România nu există încă o lege specifică pentru tratamentele cu drona: proiectul adoptat de Senat în noiembrie 2025 așteaptă votul final al Camerei Deputaților. Înainte de orice tratament, cere confirmarea Oficiului Fitosanitar Județean.</div>

<h2>Regula europeană: pulverizarea aeriană este interzisă, cu derogări</h2>
<p>Directiva 2009/128/CE privind utilizarea durabilă a pesticidelor interzice, ca regulă, pulverizarea aeriană. Statele membre pot acorda derogări doar în cazuri speciale, cu un plan de aplicare aprobat de autorități. Regulile au fost scrise pentru avioane și elicoptere, cu mult înainte de apariția dronelor, iar dronele intră, deocamdată, în aceeași categorie.</p>
<p>În prezent, în România, un utilizator profesionist care vrea să aplice produse prin pulverizare aeriană trebuie să depună cereri la mai multe instituții pentru aprobarea planului de aplicare, iar autoritățile au un termen de 7 zile pentru răspuns. Pentru drone, procedura este greu de aplicat în practică.</p>

<h2>Ce spune Autoritatea Națională Fitosanitară</h2>
<p>Într-un reportaj din 30 august 2026, reprezentanții autorității fitosanitare spuneau că folosirea dronelor pentru tratamente nu este reglementată în România. Reprezentanții fermierilor descriu situația ca pe o „zonă gri”: tehnologia este folosită, dar cadrul legal nu ține pasul.</p>

<h2>Proiectul de lege: adoptat de Senat, blocat la Camera Deputaților</h2>
<p>Senatul a adoptat pe 25 noiembrie 2025, fără voturi împotrivă, un proiect care reglementează tratamentele fitosanitare cu drona. Camera Deputaților este for decizional, iar legea intră în vigoare abia după votul ei, promulgare și publicarea în Monitorul Oficial. Până la ultima noastră verificare, votul final nu avusese loc.</p>
<p>Ce ar prevedea proiectul, în forma discutată public:</p>
<ul><li>dronele agricole ar fi tratate ca echipamente agricole, nu ca aeronave speciale;</li>
<li>operatorii ar trebui să aibă certificat de competență AACR, potrivit clasei de dronă;</li>
<li>tratamentele s-ar face pe baza unei notificări la Oficiul Fitosanitar Județean, cu termen de o zi în situații urgente (invazii de dăunători, terenuri greu accesibile);</li>
<li>doar cu produse autorizate pentru aplicare cu drona și cu evidența tratamentelor.</li></ul>
<p>Asociația Industriei de Protecția Plantelor (AIPROM) a cerut amendamente, iar organizațiile de apicultori și de mediu (ROMAPIS, WWF România, Greenpeace România) au cerut prudență. Forma finală se poate schimba.</p>

<h2>Ce se schimbă la nivel european</h2>
<p>Comisia Europeană a propus modificarea directivei, astfel încât statele membre să poată acorda o derogare generală de la interdicția pulverizării aeriene pentru anumite tipuri de drone, care vor fi enumerate într-un act delegat. Până la adoptarea modificării și a actului delegat, regula generală rămâne interdicția.</p>

<h2>Regulile de zbor: AACR și categoria „specifică”</h2>
<p>Separat de legislația fitosanitară, zborul în sine este reglementat de Regulamentul (UE) 2019/947. Dronele care transportă și eliberează substanțe sau care au peste 25 kg (cum sunt modelele DJI Agras) zboară în categoria <strong>„specifică”</strong>: operatorul se înregistrează la AACR și are nevoie de o autorizație de operare, pe baza unei evaluări a riscurilor. Detalii în <a href="/atestat-pilot-drona-agricola.html">ghidul despre atestatul de pilot</a>.</p>

<h2>Ce poți face legal acum</h2>
<ul><li><strong>Monitorizarea culturilor</strong> cu drone multispectrale, pentru hărți de vigoare (NDVI), stres hidric și boli. Vezi <a href="/drona-monitorizare-culturi.html">ghidul de monitorizare</a>.</li>
<li><strong>Cartarea</strong> parcelelor și a pagubelor (inclusiv pentru asigurări).</li>
<li>Pentru orice tratament fitosanitar cu drona: <strong>întreabă în scris Oficiul Fitosanitar Județean</strong> ce procedură se aplică pentru parcela și produsul tău și păstrează răspunsul.</li></ul>

<h2>Dacă vrei să cumperi acum</h2>
<p>Mulți fermieri cumpără dronele înainte de clarificarea legii, pentru monitorizare, cartare și pentru a fi pregătiți. Este o decizie de afaceri cu un risc legal real: calculează rentabilitatea și fără tratamente fitosanitare, cere dealerului condițiile scrise de service și verifică dacă asigurarea operatorului acoperă activitatea pe care o vei face.</p>
<div class="box info">Regulile se schimbă rapid. Actualizăm acest ghid la fiecare modificare; ultima verificare: 26 noiembrie 2026. Acest ghid nu este consultanță juridică.</div>
<p class="note">Surse: Directiva 2009/128/CE; reportajul Știrile ProTV din 30 august 2026; comunicatele Senatului și ale inițiatorilor proiectului (noiembrie 2025); poziția AIPROM; propunerea Comisiei Europene COM(2025) 1021; Regulamentul (UE) 2019/947 și ghidurile AACR.</p>"""

PAGES = [
{
    'slug': 'atestat-pilot-drona-agricola',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Atestat pilot dronă agricolă: ce certificate îți trebuie',
    'kind': 'article',
    'short': 'Atestat pilot dronă',
    'desc': 'Ce certificate AACR îți trebuie pentru o dronă agricolă: A1/A3, A2, STS, categoria specifică, autorizația de operare și pașii de înregistrare, explicați pe înțeles.',
    'h1': 'Atestat de pilot pentru drona agricolă: ce certificate îți trebuie',
    'lead': 'Certificatele AACR, categoriile de zbor și de ce o dronă de stropit nu se pilotează doar cu atestatul de „hobby”.',
    'body': """<p>Mulți fermieri cumpără o dronă agricolă convinși că ajunge un curs scurt sau atestatul online folosit pentru dronele de filmat. Pentru dronele de stropit și împrăștiat, regulile sunt mai stricte, pentru că sunt grele și eliberează substanțe din aer. Iată cum funcționează sistemul european, aplicat în România de Autoritatea Aeronautică Civilă Română (AACR).</p>

<h2>Cele trei categorii de zbor</h2>
<div class="tw"><table class="t"><tr><th>Categorie</th><th>Risc</th><th>Exemple</th><th>Ce îți trebuie</th></tr>
<tr><td>„Deschisă” (A1, A2, A3)</td><td>scăzut</td><td>drone de filmat, drone de monitorizare sub 25 kg, în raza vizuală</td><td>înregistrare operator + certificat A1/A3, eventual A2</td></tr>
<tr><td>„Specifică”</td><td>mediu</td><td>drone care eliberează substanțe, drone peste 25 kg, zbor dincolo de raza vizuală</td><td>declarație pe scenariu standard (STS) sau autorizație de operare de la AACR</td></tr>
<tr><td>„Certificată”</td><td>ridicat</td><td>transport de persoane, mărfuri periculoase</td><td>certificarea dronei și a operatorului</td></tr></table></div>
<p>Regula europeană (Regulamentul UE 2019/947) încadrează în categoria specifică orice zbor care <strong>eliberează material</strong> sau folosește o dronă cu masa maximă la decolare de <strong>peste 25 kg</strong>. Dronele de stropit DJI Agras îndeplinesc ambele condiții, deci intră în categoria specifică.</p>

<h2>Pasul 1: înregistrarea ca operator UAS</h2>
<p>Orice persoană fizică sau firmă care operează o dronă de acest tip se înregistrează ca operator pe platforma online a AACR și primește un număr de operator, care se afișează pe dronă. Înregistrarea este a operatorului, nu a pilotului: o fermă poate avea mai mulți piloți sub același operator.</p>

<h2>Pasul 2: certificatele de pilot</h2>
<ul><li><strong>A1/A3:</strong> curs și examen online pe platforma AACR. Este baza pentru orice altă calificare și ajunge pentru dronele mici de monitorizare zburate departe de oameni.</li>
<li><strong>A2:</strong> examen teoretic suplimentar, pentru zborul mai aproape de oameni cu drone din clasa C2.</li>
<li><strong>STS:</strong> calificare pentru scenariile standard europene STS-01 și STS-02. Examenul teoretic se dă la AACR, iar partea practică se face la o entitate recunoscută de AACR. Atenție: scenariile STS sunt doar pentru drone cu marcaj de clasă C5 sau C6 și <strong>sub 25 kg</strong>.</li></ul>

<h2>Pasul 3: autorizația de operare (pentru dronele de stropit)</h2>
<p>Pentru că dronele Agras au peste 25 kg și eliberează substanțe, nu se încadrează în scenariile STS. Operatorul are nevoie de o <strong>autorizație de operare</strong> emisă de AACR, pe baza unei evaluări a riscurilor (metodologia SORA) sau a unei evaluări predefinite (PDRA), acolo unde există una potrivită. Dosarul include manualul de operațiuni, procedurile de siguranță, zona de lucru și competențele piloților. Autorizația stabilește exact ce pregătire trebuie să aibă piloții.</p>
<p>Agenția Europeană pentru Siguranța Aviației (EASA) lucrează la extinderea unei evaluări predefinite (PDRA S-01) pentru activități agricole, ceea ce ar simplifica procedura pentru drone mai mici. Pentru dronele mari, autorizația individuală rămâne calea obișnuită.</p>
{{CARDS:dji-agras-t25p,dji-agras-t50}}

<h2>Pasul 4: partea fitosanitară, separată de cea aeronautică</h2>
<p>Certificatele AACR îți dau dreptul să zbori, nu și să aplici pesticide. Aplicarea produselor de protecție a plantelor destinate utilizatorilor profesionali cere instruirea prevăzută de legislația fitosanitară. Iar tratamentele cu drona nu au încă un cadru legal clar în România: proiectul de lege care le reglementează așteaptă votul Camerei Deputaților. Situația actualizată este în <a href="/legislatie-drone-agricole-2026.html">ghidul de legislație</a>.</p>

<h2>Ce verifici la un curs sau la un prestator</h2>
<ul><li>Entitatea de instruire este <strong>recunoscută de AACR</strong> pentru categoria specifică? Lista oficială este pe site-ul AACR.</li>
<li>Instruirea practică se face pe tipul de dronă pe care îl vei folosi?</li>
<li>La un prestator: are autorizație de operare AACR valabilă pentru tipul de lucrare și asigurare de răspundere civilă?</li>
<li>Dealerul te ajută cu dosarul de autorizare? Unii dealeri includ instruirea în pachet; cere în scris ce primești.</li></ul>

<h2>Cât durează</h2>
<p>Certificatul A1/A3 se obține online în câteva zile. Calificarea STS și, mai ales, autorizația de operare pot dura săptămâni, în funcție de complexitatea dosarului. Dacă vrei să lucrezi în sezonul următor, începe procedura iarna, nu în martie.</p>
<p>Vrei să vezi dacă merită drona proprie sau un prestator? Folosește <a href="/calculator-cost-hectar.html">calculatorul de cost pe hectar</a>.</p>
<p class="note">Surse: Regulamentul (UE) 2019/947 și Regulamentul (UE) 2020/639 (scenarii standard); EASA, pagina despre categoria specifică; ghidurile AACR privind calificarea STS și instruirea piloților la distanță. Acest ghid nu înlocuiește informațiile oficiale AACR.</p>""",
    'faq': [
        ('Ce atestat îmi trebuie pentru o dronă agricolă de stropit?',
         'Pe lângă înregistrarea ca operator la AACR și certificatul de pilot A1/A3, ai nevoie de o autorizație de operare în categoria specifică, pentru că dronele de stropit eliberează substanțe și au de obicei peste 25 kg. Autorizația stabilește pregătirea cerută piloților.'),
        ('Ajunge certificatul STS pentru o dronă DJI Agras?',
         'Nu. Scenariile standard STS sunt pentru drone cu marcaj de clasă C5 sau C6, sub 25 kg. Dronele Agras sunt mai grele, așa că au nevoie de o autorizație de operare emisă de AACR.'),
        ('Am nevoie de atestat pentru o dronă de monitorizare a culturilor?',
         'Da, cel puțin înregistrarea ca operator și certificatul A1/A3, obținute online pe platforma AACR. În funcție de clasa dronei și de cât de aproape zbori de oameni, poate fi nevoie și de certificatul A2.'),
    ],
},
{
    'slug': 'drona-monitorizare-culturi',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Dronă pentru monitorizarea culturilor: NDVI și hărți',
    'kind': 'article',
    'short': 'Monitorizare culturi',
    'desc': 'Cum folosești o dronă multispectrală pentru monitorizarea culturilor: hărți NDVI, stres hidric, boli, aplicare variabilă. Ce poate DJI Mavic 3 Multispectral și cât costă.',
    'h1': 'Dronă pentru monitorizarea culturilor: hărți NDVI pe înțeles',
    'lead': 'Partea din agricultura cu drone care este deja simplă, legală și ieftină: să vezi din aer ce se întâmplă în lan.',
    'body': """<p>Când se vorbește despre drone agricole, toată lumea se gândește la stropit. Dar cea mai accesibilă utilizare, fără incertitudinile legale ale tratamentelor fitosanitare, este <strong>monitorizarea</strong>: o dronă mică zboară deasupra parcelei și face hărți care arată unde plantele cresc bine și unde au probleme, cu zile sau săptămâni înainte să se vadă cu ochiul liber.</p>

<h2>Ce este o dronă multispectrală</h2>
<p>O cameră obișnuită vede trei culori: roșu, verde, albastru. O cameră multispectrală măsoară separat și lumina din benzi pe care ochiul nu le vede, mai ales <strong>infraroșul apropiat</strong> și „marginea roșie” (red edge). Plantele sănătoase reflectă mult infraroșu și absorb roșul; plantele stresate de secetă, boli sau lipsă de azot își schimbă acest raport. Din aceste măsurători se calculează indici de vegetație.</p>

<h2>NDVI și ceilalți indici, pe scurt</h2>
<ul><li><strong>NDVI</strong> (indicele de vegetație cu diferență normalizată): cel mai folosit indice, arată vigoarea și densitatea vegetației. Pe hartă, zonele verzi sunt viguroase, cele galbene și roșii au probleme.</li>
<li><strong>NDRE</strong> (cu banda red edge): mai sensibil în culturile dese și în fazele avansate, când NDVI „se saturează”.</li>
<li><strong>Harta RGB de înaltă rezoluție:</strong> o fotografie detaliată a întregii parcele, utilă pentru goluri de răsărire, buruieni, daune de la grindină sau animale sălbatice.</li></ul>

<h2>Exemplu: DJI Mavic 3 Multispectral</h2>
<p>Mavic 3 Multispectral (Mavic 3M) este drona de monitorizare cea mai răspândită în agricultură. Are o cameră RGB de 20 MP cu senzor 4/3 și obturator mecanic, plus patru camere multispectrale de 5 MP (verde, roșu, red edge și infraroșu apropiat), cu un senzor de lumină pe partea de sus, care corectează diferențele de iluminare între zboruri. Modulul RTK oferă poziționare la nivel de centimetru, fără puncte de control la sol.</p>
<p>Producătorul indică până la 43 de minute de zbor și până la 200 de hectare cartate într-un singur zbor. În practică, cu rezerva de siguranță a bateriei, timpul util de zbor este mai mic, în jur de 25 de minute după experiența unor utilizatori academici. Drona cântărește sub 1 kg cu modulul RTK. În România, prețul orientativ este de circa 4.500 de euro.</p>
{{CARDS:dji-mavic-3-multispectral}}

<h2>Ce faci concret cu hărțile</h2>
<ol><li><strong>Fertilizare variabilă:</strong> harta NDVI se transformă într-o hartă de aplicare, iar distribuitorul de îngrășăminte (sau drona de împrăștiat) pune mai mult azot unde plantele sunt slabe și mai puțin unde sunt deja viguroase.</li>
<li><strong>Cercetare țintită în câmp:</strong> în loc să mergi pe toată parcela, mergi direct la zonele cu probleme și vezi ce se întâmplă: boală, dăunători, apă stagnantă, compactare.</li>
<li><strong>Evaluarea răsăririi:</strong> golurile din cultură se văd clar pe harta RGB, iar decizia de reînsămânțare se ia pe cifre.</li>
<li><strong>Dosare de daune:</strong> hărțile cu dată și coordonate exacte ajută la documentarea pagubelor pentru asigurări.</li></ol>

<h2>Dronă sau imagini din satelit?</h2>
<p>Imaginile din satelit (de exemplu cele gratuite Sentinel-2) au rezoluție de ordinul a 10 m pe pixel și depind de nori. Drona oferă rezoluție de câțiva centimetri, zboară sub nori și o poți trimite exact în ziua în care ai nevoie. Pentru ferme mari, o combinație funcționează bine: satelitul arată tendința generală, iar drona verifică zonele cu probleme.</p>

<h2>Ce îți trebuie legal</h2>
<p>Pentru o dronă de monitorizare sub 1 kg, de regulă zbori în categoria „deschisă”: te înregistrezi ca operator la AACR și obții online certificatul de pilot A1/A3. În funcție de clasa marcată pe dronă și de cât de aproape zbori de oameni sau de clădiri, poate fi nevoie și de certificatul A2. Verifică eticheta de clasă de pe drona ta și zonele de zbor restricționate. Detalii în <a href="/atestat-pilot-drona-agricola.html">ghidul despre atestatul de pilot</a>.</p>

<h2>Merită?</h2>
<p>Pentru o fermă de câteva sute de hectare care face fertilizare variabilă, o dronă multispectrală se poate amortiza prin economia de îngrășământ și prin problemele prinse la timp. Pentru suprafețe mici, un prestator care face zboruri de monitorizare la cerere este de obicei mai ieftin. Indiferent de variantă, contează softul: hărțile trebuie să ajungă în formatul pe care îl citește utilajul tău de aplicare.</p>
<p>Compară toate modelele de drone agricole pe <a href="/">pagina principală</a> sau citește <a href="/legislatie-drone-agricole-2026.html">situația legală a stropitului cu drona</a>.</p>
<p class="note">Surse: fișa tehnică DJI Mavic 3M (ag.dji.com, enterprise.dji.com); Universitatea din Edinburgh, flota de drone de cercetare (timp util de zbor); ghidurile AACR pentru categoria deschisă.</p>""",
    'faq': [
        ('Ce este o hartă NDVI?',
         'O hartă care arată vigoarea vegetației, calculată din lumina roșie și infraroșie reflectată de plante. Zonele cu valori mici indică plante stresate de secetă, boli, dăunători sau lipsă de nutrienți.'),
        ('Câte hectare poate monitoriza o dronă într-un zbor?',
         'Pentru DJI Mavic 3 Multispectral, producătorul indică până la 200 de hectare pe zbor. Suprafața reală depinde de înălțimea de zbor, de rezoluția dorită și de rezerva de baterie.'),
        ('Este legal să monitorizez culturile cu drona?',
         'Da. Monitorizarea nu implică aplicarea de substanțe, deci se face după regulile obișnuite de zbor: înregistrare ca operator la AACR și certificat de pilot potrivit categoriei în care zbori.'),
    ],
},
]

# Correcciones en páginas existentes, sin reescribir el archivo grande.
import site_dronaagricola as _s
_OLD_BOX = ('<b>Ce spune legea în 2026.</b> Aplicarea produselor de protecție a plantelor cu drona se face cu operatori '
            'autorizați de AACR și pe baza unei notificări la Oficiul Fitosanitar Județean.')
_NEW_BOX = ('<b>Ce spune legea în 2026.</b> Tratamentele fitosanitare cu drona nu au încă un cadru legal clar în România: '
            'proiectul de lege adoptat de Senat așteaptă votul Camerei Deputaților. Monitorizarea și cartarea culturilor se fac '
            'după regulile obișnuite de zbor AACR.')
_CARDS = ('<a class="c" href="/atestat-pilot-drona-agricola.html"><span class="tag">AACR</span><b>Atestat de pilot pentru drona agricolă</b><span>Ce certificate și autorizații îți trebuie.</span></a>\n'
          '<a class="c" href="/drona-monitorizare-culturi.html"><span class="tag">Monitorizare</span><b>Dronă pentru monitorizarea culturilor</b><span>Hărți NDVI, fertilizare variabilă.</span></a>\n')
_OLD_FAQ_Q = 'Am voie să stropesc cu drona în România?'
_NEW_FAQ_A = ('Situația nu este clară. Regulile UE interzic în principiu pulverizarea aeriană, iar în România nu există încă o lege '
              'specifică pentru tratamentele cu drona: proiectul adoptat de Senat în noiembrie 2025 așteaptă votul Camerei Deputaților. '
              'Înainte de orice tratament, cere în scris confirmarea Oficiului Fitosanitar Județean.')
for _p in _s.SITE['pages']:
    if _p['slug'] == 'index':
        _p['body'] = _p['body'].replace(_OLD_BOX, _NEW_BOX)
        _p['body'] = _p['body'].replace('<span>AACR, notificarea fitosanitară și ce se schimbă.</span>',
                                        '<span>Ce e legal acum și ce prevede proiectul de lege.</span>')
        if '/drona-monitorizare-culturi.html' not in _p['body']:
            _p['body'] = _p['body'].replace('<div class="cards">\n', '<div class="cards">\n' + _CARDS, 1)
        _p['faq'] = [(q, _NEW_FAQ_A if q == _OLD_FAQ_Q else a) for q, a in _p.get('faq', [])]
    if _p['slug'] == 'legislatie-drone-agricole-2026':
        _p['body'] = LEG_BODY
        _p['date_ro'] = '26 noiembrie 2026'
        _p['title'] = 'Este legal stropitul cu drona în România? (2026)'
        _p['desc'] = ('Situația legală a dronelor agricole în România, noiembrie 2026: interdicția UE la pulverizarea aeriană, '
                      'proiectul de lege blocat la Camera Deputaților, regulile AACR și ce poți face legal acum.')
        _p['h1'] = 'Este legal stropitul cu drona în România? Situația în 2026'
        _p['lead'] = 'Ce spune legea acum, ce prevede proiectul adoptat de Senat și ce poți face în siguranță până la clarificare.'
