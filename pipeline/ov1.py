from overlay import render
import base64
logo='data:image/png;base64,'+base64.b64encode(open('r/logo.png','rb').read()).decode()
box=lambda l1,l2,top=700: f"<div style='position:absolute;top:{top}px;left:110px;right:110px;background:#fff;border-radius:36px;padding:38px 30px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35)'><div style='font:900 74px/1.25 Cairo;color:#0b1630'>{l1}</div><div style='font:900 74px/1.25 Cairo;color:#2563eb'>{l2}</div></div>"
end=f"""<div style='display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#fff;text-align:center;background:radial-gradient(circle at 50% 35%,#1d3b8a,#0b1630 70%)'>
<img src='{logo}' style='width:300px;height:300px;border-radius:70px;background:#fff'>
<div style='font:900 92px/1.2 Cairo;margin-top:50px'>ستوديو المحتوى</div>
<div style='font:600 50px/1.5 Cairo;opacity:.9;margin-top:10px'>أفكار، هوكات، سكربتات<br>صانع ريلز وصانع كاروسيل</div>
<div style='margin-top:60px;background:#facc15;color:#0b1630;font:900 64px/1.3 Cairo;padding:22px 60px;border-radius:30px'>$50 لأول 100 شخص</div>
<div style='font:700 48px Cairo;margin-top:40px'>بدون اشتراك شهري ✅ ومع حقوق إعادة البيع ✅</div>
<div style='margin-top:60px;background:#fff;color:#0b1630;border-radius:30px;padding:24px 50px'><div style='font:900 64px/1.3 Cairo'>اكتب <span style="color:#2563eb">ستوديو</span> في التعليقات 👇</div><div style='font:700 44px/1.4 Cairo'>وأرسل لك رابط الاشتراك</div></div></div>"""
res="<div style='position:absolute;top:120px;left:0;right:0;text-align:center'><span style='background:#facc15;color:#0b1630;font:900 64px Cairo;padding:14px 46px;border-radius:24px'>النتيجة 👇</span></div>"
render([(box('سويت كاروسيل كامل','في أقل من دقيقة 🤯'),'r/hook1.png',True),(end,'r/end.png',False),(res,'r/res.png',True)])
