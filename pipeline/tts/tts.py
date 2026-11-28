#!/usr/bin/env python3
"""Gemini TTS worker for mohtawa_studio.
Reads one request JSON and writes out/<name>.wav (24kHz mono) or out/<name>.err.
Request: {"name": "d11r1", "text": "...", "style": "...", "voice": "Koda", "models": [...]}"""
import json, sys, os, base64, wave, subprocess, tempfile, shutil
req_path, key = sys.argv[1], sys.argv[2]
D = os.path.dirname(os.path.abspath(__file__))
r = json.load(open(req_path))
name = r["name"]
models = r.get("models") or ["gemini-3.8-flash-tts", "gemini-2.5-flash-preview-tts", "gemini-2.5-pro-preview-tts"]
voice = r.get("voice", "Koda")
prompt = (r.get("style", "").strip() + "\n\n" + r["text"].strip()).strip()
errors = []
for m in models:
    out = ""
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(body, f); bf = f.name
    try:
        out = subprocess.run(["curl", "-s", "--max-time", "240", "-H", "Content-Type: application/json",
                              "-H", "x-goog-api-key: " + key, "-d", "@" + bf,
                              f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"],
                             capture_output=True, text=True).stdout
        os.unlink(bf)
        d = json.loads(out)
        part = d["candidates"][0]["content"]["parts"][0]["inlineData"]
        pcm = base64.b64decode(part["data"])
        rate = 24000
        mt = part.get("mimeType", "")
        if "rate=" in mt:
            rate = int(mt.split("rate=")[1].split(";")[0])
        tmp = os.path.join(D, "out", name + ".tmp")
        with wave.open(tmp, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
        os.replace(tmp, os.path.join(D, "out", name + ".wav"))
        shutil.move(req_path, os.path.join(D, "done", os.path.basename(req_path)))
        print(name, "ok", m, round(len(pcm) / 2 / rate, 1), "s")
        sys.exit(0)
    except Exception as e:
        msg = out[:300] if out else str(e)
        errors.append(f"{m}: {msg}")
open(os.path.join(D, "out", name + ".err"), "w").write("\n".join(errors))
shutil.move(req_path, os.path.join(D, "done", os.path.basename(req_path)))
print(name, "FAILED", errors)
