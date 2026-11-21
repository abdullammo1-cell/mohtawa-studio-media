import os
import json,time
from playwright.sync_api import sync_playwright
from pw import setup
from screencast import Rec
state={"onboarded":True,"view":"video","profile":{"name":"ستوديو المحتوى","handle":"mohtawa_studio","niche":"صناعة المحتوى","auto":{}}}
TAP=open(os.path.join(os.path.dirname(__file__),'tap.js')).read()
TXT='*3 أخطاء* تقتل مبيعاتك\nتسعّر بدون ما تحسب وقتك\nتقبل أي عميل\nتشتغل بدون عقد'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':405,'height':720}, device_scale_factor=2.667)
    ctx.add_init_script("localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(state)))
    ctx.add_init_script(TAP)
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1500)
    rec=Rec(pg,'r/fr5'); rec.start()
    pg.wait_for_timeout(800)
    pg.get_by_text('قائمة تتكشّف',exact=True).first.click(); pg.wait_for_timeout(900)
    ta=pg.locator('main textarea').nth(0); ta.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    ta.click(); ta.fill(''); ta.type(TXT, delay=45); pg.wait_for_timeout(600)
    pg.get_by_text('لون',exact=True).first.click(); pg.wait_for_timeout(500)
    pg.get_by_text('كبّر',exact=True).first.click(); pg.wait_for_timeout(600)
    pg.evaluate("document.querySelector('[data-act=playReel]').click()")
    pg.wait_for_timeout(9000)
    rec.stop('r/raw5.mp4'); ctx.close(); b.close()
