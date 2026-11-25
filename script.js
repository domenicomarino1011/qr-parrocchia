const NAME = "Parrocchia Sant'Antonio ai Cappuccini";
const ADDRESS = "Via Armando Diaz 74, 80023 Caivano (NA), Italia";
const googleUrl = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(`${NAME} ${ADDRESS}`)}`;
const appleUrl = `https://maps.apple.com/?q=${encodeURIComponent(`${NAME}, ${ADDRESS}`)}`;

document.querySelector('#google-link').href = googleUrl;
document.querySelector('#apple-link').href = appleUrl;
const status = document.querySelector('#status');

document.querySelector('#other-button').addEventListener('click', async () => {
  // Web Share opens the device's supported share targets; it does not launch a chosen map app.
  if (navigator.share) {
    try { await navigator.share({ title: NAME, text: ADDRESS, url: googleUrl }); }
    catch (error) { if (error.name !== 'AbortError') status.textContent = 'Condivisione non disponibile. Puoi copiare l’indirizzo.'; }
  } else {
    try {
      await navigator.clipboard.writeText(ADDRESS);
      status.textContent = 'Indirizzo copiato: incollalo nell’app che preferisci.';
    } catch {
      status.textContent = 'Il dispositivo non supporta la condivisione qui. Usa uno dei pulsanti mappa o copia l’indirizzo manualmente.';
    }
  }
});

document.querySelector('#copy-button').addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(ADDRESS);
    status.textContent = 'Indirizzo copiato.';
  } catch {
    status.textContent = ADDRESS;
  }
});
