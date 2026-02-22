# Quick Setup: Activate Virtual Environment

It’s recommended to activate your Python virtual environment before running any code. This keeps your dependencies isolated and your project safe.

**For Linux/macOS:**

```bash
./activate.sh
` `` 
*(If you get a permission error, run: `chmod +x activate.sh` first.)*

**For Windows:**
```bat
activate.bat
```

This will:

- Create the `.venv` folder if needed
- Activate the virtual environment
- Install dependencies from requirements.txt

You can now run:

```bash
python news_agent.py
# Or
python app.py
```

## Gradio-käyttöliittymä (app.py)

Käynnistä Gradio-sovellus komennolla:

```bash
python app.py
```

Sovelluksessa voit syöttää aiheen tai avainsanan (esim. nato, sports, economy, entertainment, politics, science, technology, health, weather, culture, travel, education, business, environment) ja saat uutisotsikoiden sentimentti- ja clickbait-analyysin.

## NewsAgent analyysin tulokset ja selitykset

news_agent.py tallentaa analyysitulokset tiedostoon `news_results.json`. Jokaiselle uutiselle:

- `rss_url`: RSS-lähteen osoite
- `url`: uutisen linkki
- `headline`: otsikko
- `headline_score`: otsikon sentimenttianalyysi
- `body_score`: uutisen rungon sentimenttianalyysi
- `clickbait`: onko otsikko clickbait (True = kyllä)

Selitykset:

- `neg`: Kuinka negatiivinen teksti on (0–1)
- `neu`: Kuinka neutraali teksti on (0–1)
- `pos`: Kuinka positiivinen teksti on (0–1)
- `compound`: Yhteenvetopiste (-1 = hyvin negatiivinen, +1 = hyvin positiivinen)
- `clickbait`: Jos otsikon ja rungon sentimenttipisteet eroavat paljon tai otsikko on hyvin negatiivinen, sitä pidetään clickbaitina

Tuloksia voi käyttää uutisten laadun arviointiin ja clickbait-otsikoiden tunnistamiseen.
