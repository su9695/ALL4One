# Simple Mail Transfer Protocol
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.qq.com'
mail_user='411649157'
mail_passwd='xumaiyuewrinbjci'

sender='411649157@qq.com'
recivers=['411649157@qq.com','2355840532@qq.com']

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://omp.888ly.cn">测试地址链接</a></p>
"""
message=MIMEText(mail_msg,'html','utf-8')
message['From']=Header('苏大强','utf-8')
message['To']=Header('all_tests','utf-8')
message['Subject']=Header('xxxx的测试邮件','utf-8')

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_passwd)
    smtpObj.sendmail(sender,recivers,message.as_string())
    print('带html格式的邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败',e)