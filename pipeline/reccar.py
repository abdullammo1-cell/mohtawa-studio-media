import os,json,sys
from playwright.sync_api import sync_playwright
from pw import setup
from screencast import Rec
state={"onboarded":True,"view":"car","profile":{"name":"عبدالله","handle":"mohtawa_studio","niche":"صناعة المحتوى","audience":"أصحاب المشاريع ومقدمي الخدمات","problem":"","result":"","offer":"","keyword":"","context":"","auto":{}}}
TAP=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tap.js')).read()
TOPIC=sys.argv[1]; PTS=open(sys.argv[2]).read().strip(); OUT=sys.argv[3]; SHOTS=len(sys.argv)>4
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--autoplay-policy=no-user-gesture-required'])
    ctx=b.new_context(viewport={'width':405,'height':720}, device_scale_factor=2.667)
    ctx.add_init_script("localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(state)))
    ctx.add_init_script(TAP)
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1500)
    rec=Rec(pg,OUT+'_fr'); rec.start(); pg.wait_for_timeout(700)
    pg.click('[data-act=carTpl][data-val=dark]'); pg.wait_for_timeout(600)
    inp=pg.locator('main input, main textarea').nth(0); inp.scroll_into_view_if_needed(); inp.click(); inp.type(TOPIC,delay=40); pg.wait_for_timeout(300)
    pg.click('[data-act=carStruct][data-val=steps]'); pg.wait_for_timeout(400)
    ta=pg.locator('main textarea').nth(0)
    ta.scroll_into_view_if_needed(); ta.click(); ta.type(PTS,delay=22); pg.wait_for_timeout(400)
    pg.click('[data-act=genCar]'); pg.wait_for_timeout(1500)
    for i in range(1,5):
        pg.click(f'[data-act=selSlide][data-val="{i}"]'); pg.wait_for_timeout(700)
    if SHOTS: pg.screenshot(path=OUT+'_a.png')
    pg.locator('[data-act=carToReel]').scroll_into_view_if_needed(); pg.wait_for_timeout(500)
    pg.click('[data-act=carToReel]'); pg.wait_for_timeout(1800)
    if SHOTS: pg.screenshot(path=OUT+'_b.png'); print(pg.evaluate("document.querySelector('main').innerText.slice(0,600)"))
    try:
        pg.evaluate("document.querySelector('[data-act=playReel]').scrollIntoView({block:'center'})"); pg.wait_for_timeout(500)
        pg.evaluate("document.querySelector('[data-act=playReel]').click()")
    except Exception as e: print('noplay',e)
    pg.wait_for_timeout(9000)
    if SHOTS: pg.screenshot(path=OUT+'_c.png')
    rec.stop(OUT+'.mp4'); ctx.close(); b.close()
