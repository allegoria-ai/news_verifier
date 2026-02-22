import gradio as gr

# Import the NewsAgent (ensure it's correctly imported from your module)
from news_agent import NewsAgent

# Initialize the NewsAgent
news_agent = NewsAgent()

# Function to fetch and analyze headlines
def analyze_headlines(topic):
    # Fetch headlines based on the topic
    headlines = news_agent.get_headlines(topic)
    results = []

    # Analyze each headline for sentiment and clickbait
    for headline in headlines:
        sentiment = news_agent.analyze_sentiment(headline)  # Placeholder for sentiment analysis
        clickbait_score = news_agent.detect_clickbait(headline)  # Placeholder for clickbait detection
        results.append({
            'headline': headline,
            'sentiment': sentiment,
            'clickbait_score': clickbait_score
        })

    return results

# Define Gradio interface
iface = gr.Interface(
    fn=analyze_headlines,  # Function to wrap
    inputs=gr.Textbox(label="Enter a topic or keyword:"),  # User input
    outputs=gr.JSON(label="Analysis Results:"),  # Output type
    title="News Verifier – Headline Sentiment & Clickbait Analysis",  # Title of the app
    description="Input a topic or keyword (e.g. nato, sports, economy, entertainment, politics, science, technology, health, weather, culture, travel, education, business, environment) to fetch and analyze headlines for sentiment and clickbait detection."
)

# Launch the Gradio interface
if __name__ == '__main__':
    iface.launch()  
