# Crypto Regime Detection & Alerting System

Et Python-basert system for å oppdage markedsregimer (Calm, Stressed, Crisis) ved hjelp av volatilitetsanalyse på kryptodata.

## Hva gjør dette prosjektet?

- Henter historiske prisdata fra CoinGecko API
- Beregner volatilitet og klassifiserer markedet i tre regimer:
  - **CALM** – Lav volatilitet (rolig marked)
  - **STRESSED** – Moderat til høy volatilitet
  - **CRISIS** – Ekstrem volatilitet
- Genererer enkle varsler ved regime-endringer
- Visualiserer regime-endringer over tid

## Struktur
