import json,sys,time
from playwright.sync_api import sync_playwright
from pw import setup
style, src, out = sys.argv[1:4]
state={"onboarded":True,"view":"video","profile":{"name":"ستوديو المحتوى","handle":"mohtawa_studio","niche":"صناعة المحتوى","auto":{}}}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--autoplay-policy=no-user-gesture-required'])
    ctx=b.new_context(viewport={'width':430,'height':932}, device_scale_factor=2, accept_downloads=True)
    ctx.add_init_script("localStorage.setItem('content_studio_v1',%s)"%json.dumps(json.dumps(state)))
    pg=ctx.new_page(); setup(pg)
    pg.goto('file:///home/claude/work/tool.html'); pg.wait_for_timeout(1000)
    pg.get_by_text(style,exact=True).first.click(); pg.wait_for_timeout(500)
    pg.get_by_text('لون',exact=True).first.click(); pg.wait_for_timeout(400)
    ta=pg.locator('main textarea').nth(0); ta.fill(open(src).read()); ta.dispatch_event('input'); pg.wait_for_timeout(800)
    pg.screenshot(path=out+'_ui.png')
    t=time.time()
    with pg.expect_download(timeout=180000) as d: pg.get_by_text('نزّل الفيديو').click()
    d.value.save_as(out); print('saved',d.value.suggested_filename, round(time.time()-t,1))
    b.close()
