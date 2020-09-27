# Simple Mail Transfer Protocol
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

mail_host='smtp.qq.com'
mail_user='411649157'
mail_pswd='xumaiyuewrinbjci'

sender='411649157@qq.com'
recivers=['411649157@qq.com','2355840532@qq.com']

message=MIMEMultipart('mixed')
message['From']=Header('苏大强','utf-8')
message['To']=Header('allTests','utf-8')
message['Subject']=Header('这是一封给所有测试人员的带附件、html和图片格式的邮件','utf-8')

# 附件
msgattch=MIMEText(open(r'C:\Users\suqiangqiang\Desktop\pythonL\pythonLearn\other\all_log.txt','rb').read(),'base64','utf-8')
msgattch["Content-Type"] = 'application/octet-stream' 
msgattch.add_header('Content-Disposition','attchment',filename='all_log.txt')  # 没有这一项则默认不是附件
message.attach(msgattch)
# 文字
text_palin=MIMEText('Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com','plain','utf-8')
message.attach(text_palin)
# html中带图片

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://omp.888ly.cn">八爪鱼在线旅游</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msghtml=MIMEText(mail_msg,'html','utf-8')
message.attach(msghtml)

msgImage=MIMEText(open(r'C:\Users\suqiangqiang\Desktop\pythonL\pythonLearn\other\8080.jpg','rb').read(),'base64','utf-8')
msgImage.add_header('Content-ID','<image1>')
message.attach(msgImage)

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pswd)
    smtpObj.sendmail(sender,recivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败',e)