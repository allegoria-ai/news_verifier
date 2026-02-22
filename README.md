## Quick Setup: Activate Virtual Environment
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