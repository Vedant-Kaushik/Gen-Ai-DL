# Smart_PDF

A LangChain-powered project for intelligent PDF analysis, question answering, summarization, and MCQ generation, with a simple Streamlit UI.

---

## 🚀 Project Overview

**Smart_PDF** lets you:

- 📄 Upload any PDF
- 📝 Get a concise summary
- ❓ Generate multiple-choice questions (MCQs)
- 💬 Ask custom questions (Q&A)
- 🖥️ Use a simple, beginner-friendly Streamlit web UI

All powered by [LangChain](https://github.com/langchain-ai/langchain), Gemini LLM, and your own prompt engineering!

---

## ✨ Features

- **PDF Summarization**: Get a clear, structured summary of your document.
- **MCQ Generation**: Instantly create quiz questions from your PDF.
- **Q&A**: Ask any question about the document and get an answer.
- **Streamlit UI**: No coding needed—just upload and click!
- **Modular Python code**: All logic in `pdfquestion.py` for easy reuse.

---

## 🛠️ Setup Instructions

1. **Clone the repo** (or copy the Smart_PDF folder):

   ```sh
   git clone https://github.com/Vedant-Kaushik/Gen-Ai-DL.git
   cd Gen-Ai-DL/webpagereader/Smart_PDF
   ```

2. **Install dependencies** (in your virtual environment):

   ```sh
   pip install -r requirements.txt
   # Or manually:
   pip install streamlit langchain langchain-community langchain-core python-dotenv pymupdf
   ```

3. **Set up your API key**

   - Create a `.env` file in this folder:
     ```env
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

4. **Add your PDF**
   - Place your PDF (e.g., `dl-curriculum.pdf`) in this folder, or upload via the UI.

---

## 🖥️ How to Run the Streamlit App

```sh
streamlit run pdf_ui.py
```

- Open [http://localhost:8501](http://localhost:8501) in your browser.
- Upload a PDF, select features, and get instant results!

---

## 🐍 How to Use the Core Python Script

You can also run the core logic directly:

```sh
python3 pdfquestion.py
```

- Edit the script to change the PDF or question as needed.
- All prompt engineering and chain logic is in this file.

---

## 📦 Folder Contents

- `pdf_ui.py` — Streamlit web UI
- `pdfquestion.py` — Core LangChain logic (imported by the UI)
- `dl-curriculum.pdf` — Example PDF (replace with your own)
- `ascii_graph.png`, `UI_image.png` — Project images/screenshots

---

## 🙌 Credits

- Built by Vedant Kaushik as a showcase for the **Gen-Ai-DL** project
- Powered by LangChain, Gemini, and Streamlit

---

## 💡 Tips

- You can import and reuse all logic from `pdfquestion.py` in your own projects.
- The UI is intentionally simple and beginner-friendly—customize as you like!

---

**Enjoy your Smart_PDF AI assistant!**
