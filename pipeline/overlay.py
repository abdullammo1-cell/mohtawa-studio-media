import sys,json
from playwright.sync_api import sync_playwright
from pw import setup
FONT=open('/home/claude/fonts/fonts.css').read()
def render(items):
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1080,'height':1920}); setup(pg)
        for html,out,transparent in items:
            pg.set_content(f"<html dir=rtl><head><link rel=stylesheet href='https://fonts.googleapis.com/x'><style>html,body{{margin:0;width:1080px;height:1920px;background:{'transparent' if transparent else '#0b1630'};font-family:Cairo}}</style></head><body>{html}</body></html>")
            pg.wait_for_timeout(600)
            pg.screenshot(path=out, omit_background=transparent)
        b.close()
