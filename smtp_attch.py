# Simple Mail Transfer Protocol
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host='smtp.qq.com'
mail_user='411649157'
mail_passwd='xumaiyuewrinbjci'

sender='411649157@qq.com'
recivers=['411649157@qq.com','2355840532@qq.com']

#创建一个带附件的实例
message=MIMEMultipart()
message['From']=Header('苏大强','utf-8')
message['To']=Header('all_tests','utf-8')
message['Subject']=Header('带附件的测试邮件','utf-8')
# 邮件正文
message.attach(MIMEText('这是Python 邮件发送测试……','plain','utf-8'))
# 附件1
att1=MIMEText(open(r'C:\Users\suqiangqiang\Desktop\pythonL\pythonLearn\other\all_log.txt','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attchment;filename=all_log.txt'
message.attach(att1)
# 附件2
att2=MIMEText(open(r'C:\Users\suqiangqiang\Desktop\pythonL\pythonLearn\other\testcases.xlsx','rb').read(),'base64','utf-8')
att2['Content-Type']='application/octet-stream'
att2['Content-Disposition']='attchment;filename=testcases.xlsx'

message.attach(att2)

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_passwd)
    smtpObj.sendmail(sender,recivers,message.as_string())
    print('带附件的邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败',e)