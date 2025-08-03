# Web Scraper Chrome Extension (Not publicly available)

Ask questions about any web page using GenAI.

## Features

- Automatically grabs the current tab's URL
- Sends your question and the URL to your FastAPI backend

## Setup

1. **Run your FastAPI backend:**

   ```
   uvicorn ChromeReader.fast_api_integration:app --reload
   ```

2. **Update the backend URL in `popup.js` if needed (default: `http://localhost:8000/scrape`).**

3. **Load the extension in Chrome:**

   - Go to `chrome://extensions`
   - Enable Developer Mode
   - Click "Load unpacked" and select the `ChromeReader` folder

4. **Click the extension icon on any page, ask a question, and get your answer!**

---


