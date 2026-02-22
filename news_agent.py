import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

BBC_RSS_URL = 'https://feeds.bbci.co.uk/news/technology/rss.xml'

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
    def __init__(self, rss_url=BBC_RSS_URL):
        self.rss_url = rss_url
        self.nlp = NLPEngine()

    def fetch_rss(self):
        resp = requests.get(self.rss_url)
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

    def analyze(self):
        articles = self.fetch_rss()
        for art in articles[:3]: # Limit for laptop testing; expand as needed
            print(f'URL: {art['url']}')
            print(f'Headline: {art['headline']}')
            body = self.fetch_article_body(art['url'])
            headline_score = self.nlp.sentiment(art['headline'])
            body_score = self.nlp.sentiment(body)
            clickbait = abs(headline_score['compound'] - body_score['compound']) > 0.4
            print(f'Headline Sentiment: {headline_score}')
            print(f'Body Sentiment: {body_score}')
            print(f'Clickbait?: {clickbait}\n')

if __name__ == '__main__':
    nltk.download('vader_lexicon')
    agent = NewsAgent()
    agent.analyze()