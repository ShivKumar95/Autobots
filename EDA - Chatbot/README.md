# DataFrame Agent Chat Bot

This small Streamlit app lets you upload a CSV/XLSX and ask questions about the DataFrame using LangChain + OpenAI.

Repository structure

```
Chat Bot/
  app.py
  requirements.txt
  README.md
```

Prerequisites

- Python 3.10+ installed and on your PATH
- A free/openai API key with access to the model you intend to use

Quick setup (Windows PowerShell)

1) Create and activate a virtual environment

```powershell
# from the Chat Bot folder
python -m venv .venv
# Activate the venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r "c:\Users\shivs\Desktop\Data Science\Chat Bot\requirements.txt"
```

3) Add your OpenAI API key

Create a `.env` file in the same folder as `app.py` with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual key. The app reads this using `python-dotenv`.

4) Run the Streamlit app

```powershell
# from the Chat Bot folder
streamlit run app.py
```

5) Open the app

Streamlit will open a local URL (usually `http://localhost:8501`) — open it in your browser.

Notes and troubleshooting

- If the app raises an error about `OPENAI_API_KEY`, confirm your `.env` file is present and contains the key, and that the venv you're running in has `python-dotenv` installed.
- If you see version incompatibility errors with LangChain / OpenAI, consider creating an isolated venv and running `pip freeze > requirements.txt` to capture exact working versions.
- To generate an exact `requirements.txt` from an environment where the app works, run:

```powershell
python -m pip freeze > requirements.txt
```
