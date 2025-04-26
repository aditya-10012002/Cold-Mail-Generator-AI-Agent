# AI Cold Email Generator (Gemini API)

A compact Python project to generate professional cold emails using Google's Gemini API via the Google Gen AI SDK. Supports both CLI and lightweight Streamlit UI.

## Setup
1. Clone the repo
2. `pip install -r requirements.txt`
3. Create a `.env` file with:

   ```bash
   GEMINI_API_KEY=YOUR_API_KEY
   ```

## Usage

### CLI
```bash
python main.py --company "Acme Corp" --role "CTO" --purpose "offer AI strategy consulting" --tone Formal
```

### Web UI
```bash
streamlit run streamlit_app.py
```
