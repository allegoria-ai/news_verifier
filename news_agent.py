import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

# Use multiple RSS feeds
DEFAULT_RSS_URLS = [
    'https://feeds.bbci.co.uk/news/technology/rss.xml',
    'https://feeds.bbci.co.uk/news/world/rss.xml',
    'https://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
    'https://apnews.com/rss',
    'https://www.hs.fi/rss/uutiset.xml',
    'https://feeds.yle.fi/uutiset/v1/recent.rss'
]

class NLPEngine:
    """Modular NLP engine for sentiment/ML/NLP. Swap later as needed."""
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def sentiment(self, text):
        score = self.sia.polarity_scores(text)
        return score

    # PLACEHOLDER: Future ML/Hugging Face integration
    # def advanced_sentiment(self, text):
    #     pass


class NewsAgent:
    def __init__(self, rss_urls=None):
        self.rss_urls = rss_urls or DEFAULT_RSS_URLS
        self.nlp = NLPEngine()

    def get_headlines(self, topic=None):
        # Hakee otsikoita kaikista RSS-lähteistä, suodattaa aiheen mukaan jos annettu
        headlines = []
        for rss_url in self.rss_urls:
            articles = self.fetch_rss(rss_url)
            for art in articles:
                if topic:
                    if topic.lower() in art['headline'].lower():
                        headlines.append(art['headline'])
                else:
                    headlines.append(art['headline'])
        return headlines

    def analyze_sentiment(self, headline):
        # Palauttaa sentimenttianalyysin otsikolle
        return self.nlp.sentiment(headline)

    def detect_clickbait(self, headline):
        # Yksinkertainen clickbait-tunnistus: negatiivinen otsikko tai compound < -0.3
        score = self.nlp.sentiment(headline)
        return abs(score['compound']) > 0.4 or score['neg'] > 0.2

    def fetch_rss(self, rss_url):
        resp = requests.get(rss_url)
        soup = BeautifulSoup(resp.content, 'xml')
        articles = []
        for item in soup.find_all('item'):
            headline = item.title.text
            link = item.link.text
            articles.append({'headline': headline, 'url': link})
        return articles

    def fetch_article_body(self, url):
        try:
            resp = requests.get(url, timeout=6)
            html = BeautifulSoup(resp.text, 'html.parser')
            paragraphs = [p.get_text() for p in html.find_all('p')]
            return '\n'.join(paragraphs)
        except Exception as e:
            return ''

    def analyze(self, save_to_file=False, max_articles=3):
        results = []
        for rss_url in self.rss_urls:
            print(f"\n=== RSS Feed: {rss_url} ===")
            articles = self.fetch_rss(rss_url)
            for art in articles[:max_articles]:
                print(f"URL: {art['url']}")
                print(f"Headline: {art['headline']}")
                body = self.fetch_article_body(art['url'])
                headline_score = self.nlp.sentiment(art['headline'])
                body_score = self.nlp.sentiment(body)
                # Improved clickbait logic: also check headline negativity
                clickbait = (
                    abs(headline_score['compound'] - body_score['compound']) > 0.4 or
                    headline_score['neg'] > 0.2
                )
                print(f"Headline Sentiment: {headline_score}")
                print(f"Body Sentiment: {body_score}")
                print(f"Clickbait?: {'Yes' if clickbait else 'No'}")
                print("-"*40)
                results.append({
                    'rss_url': rss_url,
                    'url': art['url'],
                    'headline': art['headline'],
                    'headline_score': headline_score,
                    'body_score': body_score,
                    'clickbait': clickbait
                })
        if save_to_file:
            with open('news_results.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print("\nTulokset tallennettu tiedostoon news_results.json")

if __name__ == '__main__':
    nltk.download('vader_lexicon')
    print("Anna RSS-osoitteet pilkulla eroteltuna (tai paina Enter käyttääksesi oletuslähteitä):")
    user_input = input()
    if user_input.strip():
        rss_urls = [url.strip() for url in user_input.split(',') if url.strip()]
    else:
        rss_urls = None
    agent = NewsAgent(rss_urls)
    agent.analyze(save_to_file=True, max_articles=3)