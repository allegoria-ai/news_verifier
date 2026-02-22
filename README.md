# News Verifier

This project is a news agent that fetches, analyzes, and compares news about AI (hype and risks vs actual reality) from multiple sources, aiming to detect clickbait, misinformation, and bias.

## Features
- Fetches top news articles by topic from online sources
- Compares headlines to article contents to detect exaggeration/clickbait
- Analyzes tone (positive/negative/neutral)
- Designed to be easily extended to include academic/government/expert sources

## Getting Started

1. Clone this repository
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the agent:
   ```bash
   python news_agent.py
   ```

## Requirements
See requirements.txt

## Extendable
You can add more sources and smarter NLP to improve verification and summarization.

## License
[Specify license here]