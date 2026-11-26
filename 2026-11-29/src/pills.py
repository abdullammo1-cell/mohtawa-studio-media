import sys; sys.path.insert(0,'/home/claude/work')
from overlay import render
pill=lambda t: f"<div style='position:absolute;bottom:230px;left:80px;right:80px;background:#0b1630;border-radius:30px;padding:30px 24px;text-align:center;box-shadow:0 16px 50px rgba(0,0,0,.35)'><div style='font:900 64px/1.3 Cairo;color:#fff'>{t}</div></div>"
render([(pill('مكتبة فيها <span style=\"color:#60a5fa\">100 هوك</span> جاهز'),'d8/p1.png',True),
        (pill('مقسّمة حسب <span style=\"color:#60a5fa\">النوع</span>'),'d8/p2.png',True),
        (pill('تنسخ الهوك وتحط <span style=\"color:#60a5fa\">موضوعك</span>'),'d8/p3.png',True)])
