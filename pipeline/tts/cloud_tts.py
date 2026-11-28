#!/usr/bin/env python3
"""Gemini TTS straight from the cloud session (needs generativelanguage.googleapis.com allowed).
Usage: GEMINI_API_KEY=... python3 cloud_tts.py out.wav "<style>" "<text>" [voice]
Writes 24kHz mono WAV. Exit 1 with the API error on failure."""
import json, sys, os, base64, wave, urllib.request
out, style, text = sys.argv[1:4]; voice = sys.argv[4] if len(sys.argv) > 4 else "Koda"
key = os.environ["GEMINI_API_KEY"].strip()
errs = []
for m in ["gemini-3.8-flash-tts", "gemini-2.5-flash-preview-tts", "gemini-2.5-pro-preview-tts"]:
    body = {"contents": [{"parts": [{"text": style.strip() + "\n\n" + text.strip()}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent",
                                 data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=240))
        p = d["candidates"][0]["content"]["parts"][0]["inlineData"]
        pcm = base64.b64decode(p["data"]); mt = p.get("mimeType", "")
        rate = int(mt.split("rate=")[1].split(";")[0]) if "rate=" in mt else 24000
        with wave.open(out, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
        print(out, "ok", m, round(len(pcm) / 2 / rate, 1), "s"); sys.exit(0)
    except urllib.error.HTTPError as e:
        errs.append(f"{m}: {e.code} {e.read()[:200]!r}")
    except Exception as e:
        errs.append(f"{m}: {e}")
print("\n".join(errs)); sys.exit(1)
