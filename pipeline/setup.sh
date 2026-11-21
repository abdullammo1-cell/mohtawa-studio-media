#!/bin/bash
# Setup for a fresh session: fonts + working directory
set -e
mkdir -p /home/claude/fonts /home/claude/work && cd /home/claude/fonts
npm pack @fontsource/cairo @fontsource/el-messiri @fontsource/tajawal @fontsource/ibm-plex-sans-arabic @fontsource/readex-pro >/dev/null 2>&1
for f in *.tgz; do mkdir -p x && tar xzf $f -C x && rm -rf "${f%.tgz}" && mv x/package "${f%.tgz}"; done
python3 - <<'PY'
import glob,os
out=[]
for pkg in glob.glob('fontsource-*'):
    if not os.path.isdir(pkg): continue
    for w in ['400','500','600','700','800','900']:
        p=f'{pkg}/{w}.css'
        if os.path.exists(p): out.append(open(p).read().replace('./files/',f'https://localfonts.test/{pkg}/files/'))
open('fonts.css','w').write('\n'.join(out)); print('fonts ok',len(out))
PY
cp /home/claude/mohtawa-studio-media/pipeline/*.py /home/claude/mohtawa-studio-media/pipeline/tap.js /home/claude/work/
mkdir -p /home/claude/work/r && cp /home/claude/mohtawa-studio-media/pipeline/assets/* /home/claude/work/r/
pip install --break-system-packages -q playwright librosa >/dev/null 2>&1 || true
echo "Now put the tool at /home/claude/work/tool.html (from the Mac: /Users/abdullahadeeb/Desktop/Content Tool/dist/content-tool.html)"
