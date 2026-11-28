#!/bin/bash
# Runs every minute (launchd). Turns requests/*.json into out/*.wav with Gemini TTS.
D="$HOME/Claude Downloads/mohtawa-tts"
cd "$D" || exit 0
KEY=$(tr -d ' \n\r' < "$D/gemini_key.txt" 2>/dev/null)
[ -z "$KEY" ] && exit 0
mkdir -p requests out done
for r in requests/*.json; do
  [ -e "$r" ] || continue
  echo "$(date '+%F %T') $r" >> log.txt
  /usr/bin/python3 "$D/tts.py" "$r" "$KEY" >> log.txt 2>&1
done
