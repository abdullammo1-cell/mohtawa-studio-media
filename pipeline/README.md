# Daily content for mohtawa_studio (ستوديو المحتوى)

## Daily output
5 reels + 3 carousels, scheduled in the Cash Process (GHL) for the day after the last scheduled day.
Times (UTC): reels 07:00, 11:00, 14:30, 17:00, 19:30 | carousels 09:00, 13:00, 18:00

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
4. Demos: `python3 recdemo.py cal|hooks|ideas` (30-day plan / hooks library / 100-ideas library, ideas used 2026-11-27, hooks used 2026-11-29), rec5.py = reel maker, `python3 reccar.py "<topic>" points.txt out` = carousel maker + "حوّله إلى ريل" (used 2026-11-26)
5. Voiceover: Gemini TTS in Google AI Studio (built-in browser on the Mac), voice Koda, style:
   "Native Gulf Arabic dialect (Saudi/Emirati colloquial, not Modern Standard). Young male content creator, energetic, confident and friendly, fast-paced Instagram reel delivery."
   Put the 5 scripts in 5 blocks, generate, then Download -> the file lands in ~/Downloads as "Generated Audio <date> - <time>.wav"
   New AI Studio UI (Nov 2026): Create new dialog -> blocks alternate Speaker 1/2, so set BOTH speakers to Koda in Speaker settings, and set Style on each block (the Style button keeps the name "Style", use nth(i)).
   If the Download click leaves only a hidden temp file in ~/Downloads (.XXXX.com.anthropic.claudefordesktop.XXXX), it is the complete WAV: copy it out and use it.
   Warning: two downloads in the same minute overwrite each other. Wait for the minute to change between downloads.
   2026-11-29: with the Claude app not open on the Mac (unattended run), Download saved nothing to ~/Downloads, so day 8 went out silent (text reels + demo with caption pills, src/pills.py). Silent track: ffmpeg anullsrc as the vo wav.
   Split: the cuts between blocks are silences of ~0.5-0.8s; match them to each script's character count (rate ~14 chars/second)
6. Assembly: `python3 assemble.py <dir> '<specs json>'`
7. Push to the repo under a new dated folder, then create-post in GHL (type reel / post)

## Writing rules (Abdullah's voice, Gulf dialect)
هذي not هال | شيء with hamza | تريد not تبي | الآن not الحين | مش not مو | no "…" ellipsis | $50 written this way
Every post ends with: اكتب كلمة "ستوديو" في التعليقات وأرسل لك رابط الاشتراك 👇🏻
Offer: $50 for the first 100 people then $97, no monthly subscription, includes resell rights. No made-up claims or testimonials.
No women in the content.
