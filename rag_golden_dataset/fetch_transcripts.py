import json
from youtube_transcript_api import YouTubeTranscriptApi

videos = {
    "3b1b_nn": "aircAruvnKk",
    "3b1b_transformers": "wjZofJX0v4M",
    "campusx_dl": "fHF22Wxuyw4",
    "codewithharry_ml": "C6YtPJxNULA"
}

for name, video_id in videos.items():
    print(f"Fetching {name}...")
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi', 'en-US', 'en-IN', 'hi-IN', 'en-GB', 'a.en', 'a.hi'])
        with open(f"{name}_transcript.json", "w", encoding="utf-8") as f:
            json.dump(transcript_data, f, ensure_ascii=False, indent=2)
            
        print(f"Success: {name}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")
