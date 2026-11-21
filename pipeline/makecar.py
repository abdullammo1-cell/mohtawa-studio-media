import sys,json,zipfile,os
from playwright.sync_api import sync_playwright
from pw import setup
topic, kind, tplname, src, out = sys.argv[1:6]
state={"onboarded":True,"view":"car","profile":{"name":"ستوديو المحتوى","handle":"mohtawa_studio","niche":"صناعة المحتوى","audience":"","problem":"","result":"","offer":"","keyword":"","context":"","auto":{}}}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':430,'height':932}, device_scale_factor=2, accept_downloads=True)
    ctx.add_init_script("if(!localStorage.getItem('content_studio_v1'))localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(state)))
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1000)
    pg.get_by_text(tplname,exact=True).first.click(); pg.wait_for_timeout(300)
    pg.locator('main input, main textarea').nth(0).fill(topic)
    pg.get_by_text(kind,exact=True).first.click()
    pg.get_by_text('اكتبه لي كاملاً').click(); pg.wait_for_timeout(600)
    pg.get_by_text('أو الصقه يدوياً').click()
    pg.fill('#ai-paste', open(src).read())
    pg.click('[data-act=aiImport]'); pg.wait_for_timeout(1500)
    pg.wait_for_timeout(500)
    S=json.loads(pg.evaluate("localStorage.getItem('content_studio_v1')"))
    pg.close()
    S['car']['slides'][-1]['kicker']='اكتب ستوديو 👇'
    S['view']='car'
    ctx.add_init_script("localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(S)))
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1500)
    print('kick', pg.evaluate("JSON.parse(localStorage.getItem('content_studio_v1')).car.slides.slice(-1)[0].kicker"))
    pg.screenshot(path=out+'_ui.png')
    with pg.expect_download() as d: pg.get_by_text('كل الشرائح ZIP').click()
    d.value.save_as(out+'.zip')
    os.makedirs(out,exist_ok=True); zipfile.ZipFile(out+'.zip').extractall(out)
    print(sorted(os.listdir(out)))
    b.close()
