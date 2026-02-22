@echo off
REM Create venv if not present
if not exist ".venv" (
    python -m venv .venv
)
REM Activate venv
call .venv\Scripts\activate.bat
REM Install requirements if requirements.txt exists
if exist requirements.txt (
    pip install -r requirements.txt
)
echo Virtual environment activated!
echo You can now run python news_agent.py or python app.py