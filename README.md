# QR geografico · Parrocchia Sant'Antonio ai Cappuccini

Pagina statica per consentire a chi scansiona il QR di scegliere Google Maps, Apple Mappe oppure la condivisione del collegamento verso un'altra app supportata dal dispositivo.

## Coordinate da verificare

Le coordinate `40.9518766, 14.2973412` sono state fornite come riferimento, ma non sono verificate come punto esatto di Via Armando Diaz 74: la fonte che le riporta le associa a un altro civico e il link breve originale non ha consentito di confermare il pin. Per prudenza non sono inserite nei collegamenti della pagina: Google Maps e Apple Mappe cercano il nome e l'indirizzo. Verificate il punto in una mappa prima di aggiungere coordinate al progetto. Fino a quel controllo, non considerate certi quei numeri.

## Pubblicazione con GitHub Pages

1. Create un repository GitHub e caricate `index.html`, `styles.css`, `script.js` e questo README nella radice del branch principale.
2. Aprite **Settings → Pages** nel repository.
3. In **Build and deployment**, scegliete **Deploy from a branch**, quindi il branch principale e la cartella `/ (root)`, e salvate.
4. Attendete il completamento della pubblicazione. L'indirizzo sarà in genere `https://<utente>.github.io/<repository>/` (o `https://<utente>.github.io/` per il repository speciale dell'utente).
5. Aprite l'URL pubblico su telefono e computer e verificate i pulsanti e la posizione.

## Generazione del QR definitivo

Il QR non è incluso intenzionalmente: prima va configurato l'URL pubblico effettivo, così il codice non punta a un indirizzo locale o provvisorio.

1. Copiate `qr_config.example.json` in `qr_config.json`.
2. Inserite in `public_url` l'indirizzo HTTPS pubblicato, completo di eventuale percorso del repository e slash finale.
3. Installate il requisito: `python -m pip install -r requirements.txt`.
4. Eseguite: `python generate_qr.py`.

Lo script rifiuta valori segnaposto, URL non HTTPS e indirizzi `localhost`/locali. Genera `qr_geografico.png` e `qr_geografico.svg`, nero su bianco, con margine e correzione errori alta. Provate la scansione dal file PNG/SVG stampato o visualizzato prima di distribuirlo. `qr_config.json` è escluso dal repository per evitare di committare configurazioni locali; il QR generato può essere aggiunto al repository o usato per la stampa.

## Comportamento

- Google Maps e Apple Mappe sono scelte esplicite, tramite URL HTTPS.
- **Altre app / Condividi** richiama il pannello di condivisione del sistema, se disponibile, senza avviare un'app a forza. Se la condivisione non è supportata, prova a copiare l’indirizzo.
- La pagina resta statica e non richiede framework, server o permessi particolari.


## Indirizzo pubblicato

https://domenicomarino1011.github.io/qr-parrocchia/

La pagina è pubblicata da `main` nella cartella radice. Le modifiche future a questi file verranno distribuite tramite GitHub Pages. Il QR definitivo deve puntare all’indirizzo HTTPS qui sopra.
