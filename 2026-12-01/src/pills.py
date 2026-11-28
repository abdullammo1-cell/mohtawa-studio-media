import sys; sys.path.insert(0,'/home/claude/work')
from overlay import render
box=lambda l1,l2,top=700: f"<div style='position:absolute;top:{top}px;left:110px;right:110px;background:#fff;border-radius:36px;padding:38px 30px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)'><div style='font:900 74px/1.25 Cairo;color:#0b1630'>{l1}</div><div style='font:900 74px/1.25 Cairo;color:#2563eb'>{l2}</div></div>"
pill=lambda t: f"<div style='position:absolute;bottom:230px;left:80px;right:80px;background:#0b1630;border-radius:30px;padding:30px 24px;text-align:center;box-shadow:0 16px 50px rgba(0,0,0,.35)'><div style='font:900 64px/1.3 Cairo;color:#fff'>{t}</div></div>"
B='<span style="color:#60a5fa">'
render([(box('تكتب 4 أسطر','وتطلع كاروسيل وريل 🤯'),'d10/ov/hook1.png',True),
        (pill(f'تكتب {B}الموضوع والنقاط</span> بس'),'d10/ov/p1.png',True),
        (pill(f'الشرائح {B}جاهزة</span> بضغطة'),'d10/ov/p2.png',True),
        (pill(f'و{B}حوّله إلى ريل</span> بضغطة ثانية'),'d10/ov/p3.png',True)])
