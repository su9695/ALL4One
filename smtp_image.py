# Simple Mail Transfer Protocol
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

mail_host='smtp.qq.com'
mail_user='411649157'
mail_passwd='xumaiyuewrinbjci'

sender='411649157@qq.com'
recivers=['411649157@qq.com','2355840532@qq.com']


message=MIMEMultipart('related')
message['From']=Header('苏大强','utf-8')
message['To']=Header('all_tests','utf-8')
message['Subject']=Header('html带图片的测试邮件','utf-8')
# 邮件正文
msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://omp.888ly.cn">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
fp = open(r'C:\Users\suqiangqiang\Desktop\pythonL\pythonLearn\other\8080.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID','<image1>')
message.attach(msgImage)


try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_passwd)
    smtpObj.sendmail(sender,recivers,message.as_string())
    print('html带图片的测试邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败',e)