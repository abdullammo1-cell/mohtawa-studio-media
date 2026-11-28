# Daily content for mohtawa_studio (ستوديو المحتوى)

## Daily output
From 2026-12-02: 10 posts a day = 6 reels + 4 carousels, scheduled in the Cash Process (GHL) for the day after the last scheduled day.
Times (UTC): reels 07:00, 10:00, 13:30, 15:00, 17:00, 20:00 | carousels 08:30, 12:00, 16:00, 18:30
(Up to 2026-12-01 it was 5 reels + 3 carousels: reels 07:00, 11:00, 14:30, 17:00, 19:30 | carousels 09:00, 13:00, 18:00)
Reel mix for 6: tool demo (07:00), خطأ وصح, محادثة, a second tool demo or قائمة, قائمة تتكشّف (17:00, best slot), هوك ثابت.

## Fixed IDs
- GHL location: iYGn4djhrRTKKK1clEHB
- mohtawa_studio account: 6b01767b3e670191353a1f33_iYGn4djhrRTKKK1clEHB_17841438183385286
- userId: QUSqhiqyI5DVIiyWUdEF
- media URL: https://raw.githubusercontent.com/abdullammo1-cell/mohtawa-studio-media/main/<folder>/<file>
- Instagram takes 10 images max per carousel through GHL

## Steps
1. `bash pipeline/setup.sh`, then stage the tool from the Mac (device_stage_files) and copy it to /home/claude/work/tool.html
2. Carousels: `python3 makecar.py "<topic>" "<type>" "<template>" file.txt out_dir`
   Text format: each slide = title line (key word between *asterisks*) + body line, separated by a --- line.
   Types: نصائح أخطاء خطوات خرافات دروس "خطأ وصح" "أدوات ومصادر" قصتي "آراء جريئة"
   Templates: كلاسيك | "أسود ونص فقط" | "أبيض ونص فقط" | ملاحظات (avoid تغريدة, its text is small)
   Last slide always: "اكتب *ستوديو* في التعليقات\nوأرسل لك رابط الاشتراك في أداة ستوديو المحتوى"
3. Reels from the tool: `python3 makereel.py "<style>" text.txt out.mp4`
   خطأ وصح: first line title, then "wrong | right" (3 rows max)
   قائمة تتكشّف: title + 5 short items max
   محادثة: each line a message, + continues the same side (11 lines max)
   هوك ثابت: one line (keep ? and ! next to plain words, not after an *asterisk* word)
4. Demos: `python3 recdemo.py cal|hooks|ideas` (30-day plan / hooks library / 100-ideas library, ideas used 2026-11-27, hooks used 2026-11-29), rec5 demo used 2026-11-30 (edit TXT via sed into rec5d9.py, overlay hook + 3 pills with ffmpeg, then assemble kind chat), rec5.py = reel maker, `python3 reccar.py "<topic>" points.txt out` = carousel maker + "حوّله إلى ريل" (used 2026-11-26 and 2026-12-01, the 2026-12-01 version with hook + 3 pills, see 2026-12-01/src/pills.py)
5. Voiceover, PRIMARY (fully automatic, no browser, no download): the Mac worker in /Users/abdullahadeeb/Claude Downloads/mohtawa-tts (source in pipeline/tts/, installed once by Abdullah with install.sh, which stores his Gemini API key in gemini_key.txt; never read, copy or print that file).
   One request per reel: write /mnt/user-data/outputs/tts/<name>.json = {"name":"d11r1","voice":"Koda","style":"<style below>","text":"<script>"} and device_commit_files it to .../mohtawa-tts/requests/<name>.json.
   A launchd job runs every minute and writes .../mohtawa-tts/out/<name>.wav (24kHz mono), or out/<name>.err. Poll with device_list_dir on out/ (every ~30 s, up to ~6 min), then device_stage_files the wavs. No splitting needed.
   If nothing appears after 4 minutes, or out/ holds .err files, or gemini_key.txt is missing, use the browser fallback below, and tell Abdullah what the .err says.
   Voiceover, FALLBACK: Gemini TTS in Google AI Studio (built-in browser on the Mac), voice Koda, style:
   "Native Gulf Arabic dialect (Saudi/Emirati colloquial, not Modern Standard). Young male content creator, energetic, confident and friendly, fast-paced Instagram reel delivery."
   Put the 5 scripts in 5 blocks, generate, then Download -> the file lands in ~/Downloads as "Generated Audio <date> - <time>.wav"
   New AI Studio UI (Nov 2026): Create new dialog -> blocks alternate Speaker 1/2, so set BOTH speakers to Koda in Speaker settings, and set Style on each block (the Style button keeps the name "Style", use nth(i)).
   If the Download click leaves only a hidden temp file in ~/Downloads (.XXXX.com.anthropic.claudefordesktop.XXXX), it is the complete WAV: copy it out and use it.
   Warning: two downloads in the same minute overwrite each other. Wait for the minute to change between downloads.
   2026-11-29: with the Claude app not open on the Mac (unattended run), Download saved nothing to ~/Downloads, so day 8 went out silent (text reels + demo with caption pills, src/pills.py). Silent track: ffmpeg anullsrc as the vo wav.
   2026-11-30: AI Studio showed "Choose an account" with every Google account signed out, so day 9 went out silent too. Abdullah has to sign back in to AI Studio in the built-in browser (Claude can't enter passwords).
   2026-12-01: signed out at the scheduled run; Abdullah signed back in to the built-in browser the same day and the day-10 reels were re-made with voice (same filenames, so the GHL posts did not change). AI Studio now shows "No API key selected" but Run still works. Desktop/Content Tool and ~/Downloads were not connected at the start; device_request_folder_access granted them.
   Stats so far: comments only on tool demos (30-day plan, idea to reel) and list reels at 17:00 (trust posts = 4 comments). Keep a demo at 07:00 and a list at 17:00.
   Split: the cuts between blocks are silences of ~0.5-0.8s; match them to each script's character count (rate ~14 chars/second)
6. Assembly: `python3 assemble.py <dir> '<specs json>'`
7. Push to the repo under a new dated folder, then create-post in GHL (type reel / post)

## Writing rules (Abdullah's voice, Gulf dialect)
هذي not هال | شيء with hamza | تريد not تبي | الآن not الحين | مش not مو | no "…" ellipsis | $50 written this way
Every post ends with: اكتب كلمة "ستوديو" في التعليقات وأرسل لك رابط الاشتراك 👇🏻
Offer: $50 for the first 100 people then $97, no monthly subscription, includes resell rights. No made-up claims or testimonials.
No women in the content.
