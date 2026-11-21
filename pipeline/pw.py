import os, mimetypes
from playwright.sync_api import sync_playwright
FONTS='/home/claude/fonts'
def setup(page):
    def handle(route):
        u=route.request.url
        if 'fonts.googleapis.com' in u:
            return route.fulfill(body=open(f'{FONTS}/fonts.css').read(), content_type='text/css')
        if 'localfonts.test' in u:
            p=FONTS+'/'+u.split('localfonts.test/')[1]
            return route.fulfill(body=open(p,'rb').read(), content_type='font/woff2')
        if u.startswith('file://') or u.startswith('data:') or u.startswith('blob:'):
            return route.continue_()
        return route.abort()
    page.route('**/*', handle)
