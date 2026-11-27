import sys; sys.path.insert(0,'/home/claude/work')
from overlay import render
box=lambda l1,l2,top=700: f"<div style='position:absolute;top:{top}px;left:110px;right:110px;background:#fff;border-radius:36px;padding:38px 30px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)'><div style='font:900 74px/1.25 Cairo;color:#0b1630'>{l1}</div><div style='font:900 74px/1.25 Cairo;color:#2563eb'>{l2}</div></div>"
pill=lambda t: f"<div style='position:absolute;bottom:230px;left:80px;right:80px;background:#0b1630;border-radius:30px;padding:30px 24px;text-align:center;box-shadow:0 16px 50px rgba(0,0,0,.35)'><div style='font:900 64px/1.3 Cairo;color:#fff'>{t}</div></div>"
render([(box('تكتب النقاط','وتطلع ريل 🎬'),'d9/hook1.png',True),
        (pill('تكتب <span style=\"color:#60a5fa\">النقاط</span> بس'),'d9/p1.png',True),
        (pill('تختار <span style=\"color:#60a5fa\">اللون والحجم</span>'),'d9/p2.png',True),
        (pill('والريل <span style=\"color:#60a5fa\">جاهز</span> بدون مونتاج'),'d9/p3.png',True)])
