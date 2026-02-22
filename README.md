# Quick Setup: Activate Virtual Environment

It’s recommended to activate your Python virtual environment before running any code. This keeps your dependencies isolated and your project safe.

**For Linux/macOS:**

```bash
./activate.sh
```
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

---

## Gradio App Interface (app.py)

Start the Gradio application with:

```bash
python app.py
```

In the app, you can input a topic or keyword (such as: 'nato', 'sports', 'economy', 'entertainment', 'politics', 'science', 'technology', 'health', 'weather', 'culture', 'travel', 'education', 'business', 'environment') and receive sentiment and clickbait analysis of news headlines.

---

## NewsAgent Analysis Results and Explanations

news_agent.py saves the analysis results to the file `news_results.json`. For each news item:
- `rss_url`: the RSS source address
- `url`: news link
- `headline`: headline text
- `headline_score`: sentiment analysis of the headline
- `body_score`: sentiment analysis of the article body
- `clickbait`: whether the headline is considered clickbait (True = yes)

Explanation of fields:
- `neg`: How negative the text is (0–1)
- `neu`: How neutral the text is (0–1)
- `pos`: How positive the text is (0–1)
- `compound`: Overall score (-1 = very negative, +1 = very positive)
- `clickbait`: If headline and body sentiment scores differ significantly or the headline is highly negative, it is considered clickbait.

You can use these results to assess news quality and identify clickbait headlines.

---

## Additional Recommendations

- Always maintain up-to-date documentation (README, requirements.txt, code comments).
- Use Python virtual environments for every project.
- Expand code comments to clarify purpose and logic in each file.
- For more detailed information or files, visit: [news_verifier on GitHub](https://github.com/allegoria-ai/news_verifier).