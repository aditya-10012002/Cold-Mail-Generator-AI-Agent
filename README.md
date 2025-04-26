# AI Cold Email Generator (Gemini API)

A compact Python project to generate professional cold emails using Google's Gemini API via the Google Gen AI SDK. Supports both CLI and lightweight Streamlit UI.

<br>

![Screenshot 2025-04-26 200641.png](<https://media-hosting.imagekit.io/a754241df9884022/Screenshot%202025-04-26%20200641.png?Expires=1840290139&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=gQOGuo1LLTFLz2vFVwX7nKRNlCSiPcKTwsT1F-c7xwfWmZnp1tWxecAUxZRNpYi~FJrcDHWIpDYrKG-nLqRngtNGvqOCRKAarHZqBY-3eyGNycxKci~01EI3bS~W6AP5QL~C-xDxM1kuE6geio-lPvqkn02bjBV4MBbiqc7sgygQbC5pEEyboemljRRrxKtTAcsaqFNzV6UXwseIG13o7sbR4GsOg8Gh31OcabfrH2CyFJV6auRg4QIIoaK7LQT3daajTCpqdFDC0H0KWIXwODz34c-a9apkpCPIlKkeo4Q-GJCPNSp5rBvrcGB-d5w8ixvZMHHzptE7zPLEy15TJQ__>)

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
