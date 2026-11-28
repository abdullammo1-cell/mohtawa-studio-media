#!/bin/bash
# One-time setup: saves the Gemini API key and starts the background worker.
D="$HOME/Claude Downloads/mohtawa-tts"
mkdir -p "$D/requests" "$D/out" "$D/done"
if [ ! -s "$D/gemini_key.txt" ]; then
  read -s -p "Paste your Gemini API key then press Enter: " K; echo
  printf '%s' "$K" > "$D/gemini_key.txt"
fi
chmod 600 "$D/gemini_key.txt"
P="$HOME/Library/LaunchAgents/com.mohtawa.tts.plist"
mkdir -p "$HOME/Library/LaunchAgents"
cat > "$P" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
<key>Label</key><string>com.mohtawa.tts</string>
<key>ProgramArguments</key><array><string>/bin/bash</string><string>$D/worker.sh</string></array>
<key>StartInterval</key><integer>60</integer>
<key>RunAtLoad</key><true/>
</dict></plist>
PL
launchctl bootout gui/$(id -u) "$P" 2>/dev/null
launchctl bootstrap gui/$(id -u) "$P" && echo "Worker started."
echo '{"name":"test","voice":"Koda","style":"Native Gulf Arabic dialect, young male, energetic.","text":"هلا، هذا اختبار الصوت."}' > "$D/requests/test.json"
echo "Testing (up to 2 minutes)..."
for i in $(seq 1 24); do
  sleep 5
  if [ -e "$D/out/test.wav" ]; then echo "✅ Works. Voice file: $D/out/test.wav"; afplay "$D/out/test.wav" 2>/dev/null; exit 0; fi
  if [ -e "$D/out/test.err" ]; then echo "❌ Failed:"; cat "$D/out/test.err"; exit 1; fi
done
echo "No result yet. Check $D/log.txt"
