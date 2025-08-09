Microphone (Live Meeting)
        ↓
  sounddevice → capture audio chunks (5–10 sec each)
        ↓
  Faster-Whisper → transcribe each chunk immediately
        ↓
  Append to transcript in memory + save to file as we go
        ↓
  Every N minutes → run local HuggingFace summarizer on collected transcript
        ↓
  Show live subtitles + final summary at the end
