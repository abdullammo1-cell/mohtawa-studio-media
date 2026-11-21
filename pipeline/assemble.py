"""Assemble final reels: python3 assemble.py <workdir> '<json specs>'
spec: [name, raw_video, vo_wav, kind(demo|tool|chat), hook_png_or_null]
- demo: slows the recording to fit the voice + hook box for the first 3 seconds
- tool: holds the last frame to fit the voice + "made in a minute with the tool" box
- chat: as is (the voice is a short intro)
All of them end with the end card (assets/c.mp4) and audio is stereo AAC 48k"""
import subprocess,sys,json,os
W=sys.argv[1]; specs=json.loads(sys.argv[2]); R='/home/claude/work/r/'
os.chdir(W)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def run(a): subprocess.run(a,check=True)
for n,raw,vo,kind,hook in specs:
    rd,vd=dur(raw),dur(vo)
    target=max(rd, vd-3.0) if kind!='chat' else rd
    enc=['-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p']
    if kind=='demo':
        vf=f"[0:v]setpts=PTS/{rd/target:.4f},fps=30[v];[v][1:v]overlay=0:0:enable='lt(t,3)'[o]"
        run(['ffmpeg','-v','error','-y','-i',raw,'-i',hook,'-filter_complex',vf,'-map','[o]',*enc,f'{n}_main.mp4'])
    elif kind=='tool':
        pad=max(0,target-rd)
        vf=f"[0:v]fps=30,tpad=stop_mode=clone:stop_duration={pad:.2f}[v];[v][1:v]overlay=0:0:enable='gt(t,{max(2,target-3.5):.2f})'[o]"
        run(['ffmpeg','-v','error','-y','-i',raw,'-i',R+'made.png','-filter_complex',vf,'-map','[o]',*enc,f'{n}_main.mp4'])
    else:
        run(['ffmpeg','-v','error','-y','-i',raw,'-vf','fps=30,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','18',f'{n}_main.mp4'])
    open('L.txt','w').write(f"file '{n}_main.mp4'\nfile '{R}c.mp4'\n")
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','L.txt','-i',vo,'-filter_complex','[1:a]apad[a]','-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ac','2','-ar','48000','-shortest',f'{n}.mp4'])
    print(n, round(rd,1), round(vd,1), '->', round(dur(f'{n}.mp4'),1))
