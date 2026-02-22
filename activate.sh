#!/bin/bash
set -e
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi
echo "Virtual environment activated!"
echo "You can now run python news_agent.py or python app.py"