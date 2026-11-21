import base64,os,subprocess,threading
class Rec:
    def __init__(s,pg,outdir):
        s.pg=pg; s.dir=outdir; os.makedirs(outdir,exist_ok=True); s.frames=[]; s.cdp=pg.context.new_cdp_session(pg)
        s.cdp.on('Page.screencastFrame', s.on)
    def on(s,e):
        n=len(s.frames); fn=f'{s.dir}/{n:05d}.jpg'
        open(fn,'wb').write(base64.b64decode(e['data'])); s.frames.append((fn,e['metadata']['timestamp']))
        try: s.cdp.send('Page.screencastFrameAck',{'sessionId':e['sessionId']})
        except Exception: pass
    def start(s): s.cdp.send('Page.startScreencast',{'format':'jpeg','quality':92,'maxWidth':1080,'maxHeight':1920,'everyNthFrame':1})
    def stop(s,out):
        s.cdp.send('Page.stopScreencast')
        lines=[]
        fr=s.frames
        for i,(fn,t) in enumerate(fr):
            d=(fr[i+1][1]-t) if i+1<len(fr) else 0.5
            lines.append(f"file '{os.path.abspath(fn)}'\nduration {max(d,0.001):.4f}")
        lines.append(f"file '{os.path.abspath(fr[-1][0])}'")
        open(s.dir+'/list.txt','w').write('\n'.join(lines))
        subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',s.dir+'/list.txt','-vf','scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=white,fps=30','-pix_fmt','yuv420p','-c:v','libx264','-preset','veryfast','-crf','18',out],check=True)
        return fr[0][1]
