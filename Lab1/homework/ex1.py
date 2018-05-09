import datetime
from gmail import GMail, Message
from random import choice

now = datetime.datetime.now()

html_template ='''
<p>Em chào <span style="color: #ff0000;"><strong>s&ecirc;́p</strong></span>:</p>
<p>H&ocirc;m nay trời {{weather}}, em bị {{sickness}}, s&ecirc;́p cho em nghỉ h&ocirc;m nay nhé :D Y&ecirc;u s&ecirc;́p</p>'''


sickness_list =["thương hàn", "kiết lị", "tiêu chảy cấp"]
sickness = choice(sickness_list)

html_content= html_template.replace("{{sickness}}", sickness).replace("{{weather}}", "mưa")

if now.hour >= 7 and now.minute >= 0:
    mail = GMail('c4e201708@gmail.com', 'codethechange')
    message = Message("Xin nghi om", to="vungoctan.nevents@gmail.com", html=html_content)
    mail.send(message)
