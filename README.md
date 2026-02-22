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

## Gradio UI (app.py)

Start the Gradio application with:

```bash
python app.py
```

In the application you can enter a topic or keyword (e.g. nato, sports, economy, entertainment, politics, science, technology, health, weather, culture, travel, education, business, environment) and get sentiment and clickbait analysis of news headlines.

## NewsAgent analysis results and explanations

news_agent.py saves the analysis results to the file `news_results.json`. For each news item:

- `rss_url`: RSS source URL
- `url`: news article link
- `headline`: headline
- `headline_score`: sentiment analysis of the headline
- `body_score`: sentiment analysis of the news body
- `clickbait`: whether the headline is clickbait (True = yes)

Explanations:

- `neg`: How negative the text is (0–1)
- `neu`: How neutral the text is (0–1)
- `pos`: How positive the text is (0–1)
- `compound`: Summary score (-1 = very negative, +1 = very positive)
- `clickbait`: If the sentiment scores of the headline and body differ significantly or the headline is very negative, it is considered clickbait

The results can be used to assess news quality and identify clickbait headlines.
