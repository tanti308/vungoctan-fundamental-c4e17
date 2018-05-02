from gmail import GMail, Message
from random import choice
# gmail = GMail('vungoctan.nevents@gmail.com','tanvn1996')
# msg = Message('Test sending email',to='c4e201708@gmail.com>',text='Cho e keo a oi vi e xong dau tien ahihihi')
# gmail.send(msg)
#dung giao thuc SMTP truy cap list mail torng tai khoan
html_template ='''
<p>Em chào <span style="color: #ff0000;"><strong>s&ecirc;́p</strong></span>:</p>
<p>H&ocirc;m nay trời {{weather}}, em bị {{sickness}}, s&ecirc;́p cho em nghỉ h&ocirc;m nay nhé :D Y&ecirc;u s&ecirc;́p</p>'''
# Database: SQL(MSS, SQLite): dung ngon ngu moi de giao tiep giua python va database; no-SQL(MongoDB, Realm): ngc lai.
# get current hour lay gio hien tai cua window de chay

sickness_list =["thương hàn", "kiết lị", "tiêu chảy cấp"]
sickness = choice(sickness_list)

html_content= html_template.replace("{{sickness}}", sickness).replace("{{weather}}", "mưa")

mail = GMail('c4e201708@gmail.com', 'codethechange')
message = Message("Xin nghi om", to="vungoctan.nevents@gmail.com", html=html_content)
mail.send(message)
