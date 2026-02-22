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
    inputs=gr.inputs.Textbox(label="Enter a topic or keyword:"),  # User input
    outputs=gr.outputs.JSON(label="Analysis Results:"),  # Output type
    title="News Verifier",  # Title of the app
    description="Input a topic or keyword to fetch and analyze headlines for sentiment and clickbait detection."  # App description
)

# Launch the Gradio interface
if __name__ == '__main__':
    iface.launch()  
