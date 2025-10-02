# 📘 YouTube Transcript Notes API

A **FastAPI-based backend service** that extracts YouTube video transcripts, processes them with **Google Gemini AI**, and generates **point-wise, structured notes**.  
Perfect for students, researchers, and content creators who want **concise, high-value notes** instead of watching entire videos.

* * *

## 🚀 Features

*   **🎥 YouTube URL Support** – Input any valid YouTube video link.
    
*   **📝 Transcript Extraction** – Uses [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) to fetch transcripts.
    
*   **🤖 AI-Powered Summaries** – Summarizes transcripts into **organized, detailed notes** using **Google Gemini**.
    
*   **⚡ FastAPI Backend** – Lightweight, high-performance API with automatic Swagger docs.
    
*   **🌐 CORS Enabled** – Ready for integration with frontend apps (React, Vue, Next.js, etc.).
    
*   **📦 Simple Deployment** – Works with `uvicorn`, Docker, or any ASGI server.
    

* * *

## 📂 Project Structure

`# ├── app/index.py # FastAPI app with endpoints

# ├── requirements.txt # Python dependencies

# ├── README.md # Project documentation`

* * *

## 🛠️ Installation

### 1️⃣ Clone Repo

`[https://github.com/shriyanshkush/YoutubeVideoSummarizer]`

### 2️⃣ Create Virtual Environment

`python -m venv venv source venv/bin/activate   # macOS/Linux venv\Scripts\activate      # Windows`

### 3️⃣ Install Dependencies

`pip install -r requirements.txt`

### 4️⃣ Setup Environment Variables

Create a `.env` file:

`GEMINI_API_KEY=your_google_gemini_api_key_here`

* * *

## 📌 API Endpoints

### 1\. Health Check

**`GET /`**

`{   "ok": true }`

### 2\. Summarize YouTube Video

**`GET /summarize?youtube_url=<URL>`**

#### Example Request:

`curl "http://127.0.0.1:8000/summarize?youtube_url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"`

#### Example Response:

`{   "video_id": "dQw4w9WgXcQ",   "notes": "- Introduction: ... \n- Main Ideas: ... \n- Examples: ... \n- Conclusion: ..." }`

* * *

## ⚙️ Tech Stack

*   **Backend Framework** → FastAPI
    
*   **Transcript Extraction** → [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
    
*   **AI Summarization** → Google Gemini API
    
*   **CORS Middleware** → Built-in FastAPI support
    
*   **Server** → Uvicorn
    

* * *

## 📌 Use Cases

*   🎓 **Students** – Get notes from long lecture videos.
    
*   📰 **Researchers** – Summarize interviews, speeches, or debates.
    
*   🎥 **Creators** – Convert your video transcripts into blog-style notes.
    
*   💼 **Professionals** – Save time by extracting meeting or presentation highlights.
    

* * *

## 🔮 Future Enhancements

*   🔊 Add **audio-to-text** transcript fallback (for videos without transcripts).
    
*   📤 Export summaries as **PDF/Markdown**.
    
*   🔍 Topic tagging & keyword extraction.
    
*   🖥️ Frontend UI with copy/download/share options.
    

* * *

## 🏆 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your idea.

* * *

## 📄 License

MIT License © 2025
