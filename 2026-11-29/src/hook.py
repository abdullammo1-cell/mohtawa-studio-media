import sys; sys.path.insert(0,'/home/claude/work')
from overlay import render
box=lambda l1,l2,top=700: f"<div style='position:absolute;top:{top}px;left:110px;right:110px;background:#fff;border-radius:36px;padding:38px 30px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)'><div style='font:900 74px/1.25 Cairo;color:#0b1630'>{l1}</div><div style='font:900 74px/1.25 Cairo;color:#2563eb'>{l2}</div></div>"
render([(box('100 هوك جاهز','تنسخه وتنشر 🔥'),'d8/hook1.png',True)])
