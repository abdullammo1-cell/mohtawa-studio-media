import os
import json,sys
from playwright.sync_api import sync_playwright
from pw import setup
from screencast import Rec
which=sys.argv[1]
state={"onboarded":True,"view":"home","profile":{"name":"عبدالله","handle":"mohtawa_studio","niche":"صناعة المحتوى","audience":"أصحاب المشاريع ومقدمي الخدمات","problem":"ما يعرفون ايش ينشرون","result":"محتوى منتظم يجيب عملاء","offer":"","keyword":"","context":"","auto":{}}}
TAP=open(os.path.join(os.path.dirname(__file__),'tap.js')).read()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':405,'height':720}, device_scale_factor=2.667)
    ctx.add_init_script("localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(state)))
    ctx.add_init_script(TAP)
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1500)
    rec=Rec(pg,f'b2/fr_{which}'); rec.start(); pg.wait_for_timeout(700)
    def scroll(n,dy=180,w=380):
        for _ in range(n): pg.mouse.move(200,400); pg.mouse.wheel(0,dy); pg.wait_for_timeout(w)
    if which=='cal':
        pg.click('[data-act=nav][data-val=cal]'); pg.wait_for_timeout(900)
        pg.click('[data-act=genCal]'); pg.wait_for_timeout(1500)
        scroll(14)
        pg.wait_for_timeout(600)
    else:
        pg.click('[data-act=nav][data-val=lib]'); pg.wait_for_timeout(900)
        pg.click('[data-act=libTab][data-val=hooks]'); pg.wait_for_timeout(1200)
        scroll(6)
        cats=pg.locator('main [data-act=hookCat]')
        print('cats',cats.count(), cats.all_inner_texts()[:10] if cats.count() else '')
        if cats.count()>3:
            pg.mouse.wheel(0,-2000); pg.wait_for_timeout(700)
            cats.nth(2).click(); pg.wait_for_timeout(1200); scroll(4)
            pg.mouse.wheel(0,-2000); pg.wait_for_timeout(600)
            cats.nth(5).click(); pg.wait_for_timeout(1200); scroll(4)
    pg.wait_for_timeout(500)
    print(pg.evaluate("document.querySelector('main').innerText.slice(0,300)"))
    rec.stop(f'b2/raw_{which}.mp4'); ctx.close(); b.close()
