# AI Cold Email Generator (Gemini API)

A compact Python project to generate professional cold emails using Google's Gemini API via the Google Gen AI SDK. Supports both CLI and lightweight Streamlit UI.

<br>

![Screenshot 2025-04-26 200641.png](<https://ik.imagekit.io/py7zov877/Screenshot%202025-04-26%20200641.png?updatedAt=1748197967534__>)

<br>

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
