# Simple Mail Transfer Protocol
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
# ----------1.跟发件相关的参数------
mail_host='smtp.qq.com' # 服务器
mail_user='411649157'
mail_password='xumaiyuewrinbjci'

sender='411649157@qq.com'
receivers=['411649157@qq.com','2355840532@qq.com']   # 接收邮件的list
# ----------2.编辑邮件的内容------
message=MIMEText('这是一封测试邮件','plain','utf-8')  # 邮件内容
message['From']=Header('LukeMan','utf-8')  # 发件人
message['To']=Header('苏大强','utf-8')  # 收件人
message['Subject']=Header('Python SMTP 邮件测试','utf-8') # 邮件标题
#  ----------3.发送邮件------
try:
    smtpobj=smtplib.SMTP()
    smtpobj.connect(mail_host,25) # 连接
    smtpobj.login(mail_user,mail_password) #登录
    smtpobj.sendmail(sender,receivers,message.as_string()) # 发送
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件", e)