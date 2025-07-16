# 🚀 Local Setup Guide for YouTube Chatbot

This guide will help you run the complete YouTube chatbot application locally without needing GitHub or any external hosting.

## 📁 Project Structure
```
youtube-chatbot/
├── backend/                 # Your existing Python backend
│   ├── main.py
│   ├── backend_fastAPI.py
│   ├── requirements.txt
│   └── README.md
├── frontend/               # New React frontend (this project)
│   ├── src/
│   ├── package.json
│   └── ...
└── LOCAL_SETUP.md         # This file
```

## 🔧 Step 1: Setup Backend (Python)

1. **Navigate to your YT_chatbot folder:**
   ```bash
   cd path/to/your/YT_chatbot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # Activate it:
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Google API key:**
   ```bash
   # Replace with your actual API key
   export GOOGLE_API_KEY="your_actual_google_api_key_here"
   
   # On Windows:
   set GOOGLE_API_KEY=your_actual_google_api_key_here
   ```

5. **Start the backend server:**
   ```bash
   uvicorn backend_fastAPI:app --reload --host 0.0.0.0 --port 8000
   ```

   You should see: `Uvicorn running on http://0.0.0.0:8000`

## 🎨 Step 2: Setup Frontend (React)

1. **In a new terminal, navigate to this frontend folder:**
   ```bash
   cd path/to/this/frontend/project
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the frontend development server:**
   ```bash
   npm run dev
   ```

   You should see: `Local: http://localhost:5173/`

## 🌐 Step 3: Access Your Application

1. **Open your browser and go to:** `http://localhost:5173`
2. **Your backend API will be running on:** `http://localhost:8000`

## 🔄 Daily Usage

Every time you want to use the application:

1. **Start Backend:**
   ```bash
   cd path/to/YT_chatbot
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   export GOOGLE_API_KEY="your_key"  # or set GOOGLE_API_KEY=your_key on Windows
   uvicorn backend_fastAPI:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start Frontend (in another terminal):**
   ```bash
   cd path/to/frontend/project
   npm run dev
   ```

3. **Open browser:** `http://localhost:5173`

## 🛠️ Troubleshooting

**Backend Issues:**
- Make sure your Google API key is set correctly
- Check if port 8000 is available
- Verify all Python dependencies are installed

**Frontend Issues:**
- Make sure Node.js is installed (version 16+)
- Check if port 5173 is available
- Try `npm install` again if there are dependency issues

**Connection Issues:**
- Ensure both servers are running
- Check that backend is accessible at `http://localhost:8000`
- Verify CORS is enabled in your FastAPI backend (it should be)

## 📱 Features

- **Sleek Black Theme:** Modern dark interface inspired by Apple's design
- **Split Screen:** YouTube video on left, chat on right
- **Real-time Chat:** Instant responses from your AI backend
- **Responsive Design:** Works on desktop, tablet, and mobile
- **Smart URL Validation:** Automatically validates YouTube URLs
- **Loading States:** Visual feedback during processing

## 🎯 Usage

1. Paste any YouTube URL in the input field
2. The video will automatically load and display
3. Ask any question about the video content
4. Get AI-powered answers based on the video transcript

Enjoy your personal YouTube AI chatbot! 🚀