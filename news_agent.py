import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Optional: Placeholder for future ML or Hugging Face integration
class NLPEngine:
    """ Abstract NLP engine for sentiment. Swap with ML/HF models easily. """
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def sentiment(self, text):
        score = self.sia.polarity_scores(text)
        return score

# Future: Add Hugging Face/ML integration here

class NewsAgent:
    """Fetches and analyzes news about AI (hype and risks vs reality). """
    def __init__(self, topic='AI'):
        self.topic = topic
        self.nlp = NLPEngine()

    def fetch_articles(self):
        # Insert your NewsAPI key below
        api_key = 'YOUR_API_KEY'
        url = f'https://newsapi.org/v2/everything?q={self.topic}&language=en&apiKey={api_key}'
        resp = requests.get(url)
        data = resp.json().get('articles', [])
        return data

    def analyze_article(self, article):
        headline = article.get('title', '')
        url = article.get('url', '')
        try:
            resp = requests.get(url, timeout=6)
            soup = BeautifulSoup(resp.text, 'html.parser')
            body = ' '.join([p.text for p in soup.find_all('p')])
        except Exception:
            body = ''
        head_score = self.nlp.sentiment(headline)
        body_score = self.nlp.sentiment(body)
        clickbait = abs(head_score['compound'] - body_score['compound']) > 0.4
        return {
            'headline': headline,
            'headline_sentiment': head_score,
            'body_sentiment': body_score,
            'clickbait': clickbait,
            'url': url
        }

    def run(self):
        articles = self.fetch_articles()
        for article in articles[:3]:
            result = self.analyze_article(article)
            print(f"\nArticle: {result['url']}\nHeadline: {result['headline']}\nHeadline Sentiment: {result['headline_sentiment']}\nBody Sentiment: {result['body_sentiment']}\nClickbait: {result['clickbait']}")

if __name__ == '__main__':
    nltk.download('vader_lexicon')  # ensure sentiment module is ready
    agent = NewsAgent('AI')  # You can change topic here
    agent.run()