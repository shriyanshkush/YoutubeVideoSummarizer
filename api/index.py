from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import google.generativeai as genai
import os

# --- Configure Gemini from env ---
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(
    title="YouTube Transcript Notes API"
)

# --- Allow CORS (important for frontend apps) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_video_id(url: str):
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    path = parsed.path or ""
    if host in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
        if path.startswith("/embed/") or path.startswith("/v/"):
            parts = path.split("/")
            if len(parts) >= 3:
                return parts[2]
    if host == "youtu.be":
        return path.lstrip("/")
    return None


PROMPT = (
    "Read the full transcript below and create point-wise notes that cover the intro, "
    "main ideas, examples, and conclusion. Remove fillers, paraphrase concisely, and "
    "organize logically so the notes give the same value as watching the video.\n"
    "Final Output: Well-structured detailed notes summarizing the video’s content.\n\n"
    "Transcript:\n"
)


@app.get("/")
def health():
    return {"ok": True}


@app.get("/summarize")
def summarize(youtube_url: str = Query(..., description="Full YouTube URL")):
    try:
        video_id = get_video_id(youtube_url)
        if not video_id:
            raise HTTPException(status_code=400, detail="Invalid YouTube URL")

        # --- fetch transcript (instance style, matches your Streamlit code) ---
        try:
            ytt_api = YouTubeTranscriptApi()
            fetched = ytt_api.fetch(video_id)
            raw_data = fetched.to_raw_data()
            transcript_text = " ".join([entry["text"] for entry in raw_data])
        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            raise HTTPException(status_code=404, detail=f"No transcript available: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transcript error: {e}")

        # --- summarize with Gemini ---
        model = genai.GenerativeModel("gemini-1.5-flash")
        resp = model.generate_content(PROMPT + transcript_text)

        return {"video_id": video_id, "notes": resp.text}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
