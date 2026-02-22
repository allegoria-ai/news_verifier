# News Verifier

## Overview
This project fetches news articles from the BBC Technology RSS feed, scrapes the content using BeautifulSoup, and performs sentiment analysis on the articles using NLTK. The design is modular, allowing easy expansions to incorporate machine learning or Hugging Face models for more advanced analysis in the future.

## Features
- **RSS-based News Fetching:** Utilizes the [BBC Technology](https://www.bbc.co.uk/news/technology) feed to gather news articles.
- **Web Scraping:** Employs BeautifulSoup for scraping article bodies to extract relevant content.
- **Sentiment Analysis:** Implements NLP sentiment analysis using NLTK, which can easily be extended to support additional models.
- **Interactive Web Interface:** Provides a Gradio interface that allows users to interact with the news analysis bot. The app can be run using `python app.py`.

## Installation
To install the required packages, clone the repository and run:
```bash
pip install -r requirements.txt
```

## CLI Usage
You can fetch news articles and analyze their sentiment directly from the command line using:
```bash
python cli.py --fetch
python cli.py --analyze
```

## Gradio Usage
To start the Gradio web interface, simply run:
```bash
python app.py
```
Then, navigate to `http://localhost:7860` in your browser to use the interactive news analysis bot.

## Modular Design
The project's modular design allows for:
- Easy addition of new sentiment analysis models.
- Integration with different news sources and feeds.
- Customization of the Gradio interface for various user needs.

Future expansions can include the implementation of machine learning models or advanced NLP techniques. This flexibility ensures that the project can evolve with changing technology and user needs.