import smtplib
from email.mime.text import MIMEText
from flask import current_app
import random

def post_email(email):
    msg_from = current_app.config['EMAIL_FROM'] # 发送方
    passwd = current_app.config['EMAIL_PASSWD'] # 授权码
    msg_to = email # 接收方
    random_num = "".join(random.sample('0123456789', 5)) # 随机数
    subject = current_app.config['EMAIL_SUBJECT']# 邮件主题
    content = '''
        <p style="font-size:25px">亲爱的用户：您好！</p>
        <span style="font-size:25px">您正在注册账号，请在验证码输入框中输入：</span>
        <span style="color:blue;font-size:30px">%s</span>
        <span style="font-size:25px">，以完成操作</span>
    ''' % random_num
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465) # 邮件服务器及端口号
        s.login(msg_from, passwd) # 登录SMTP服务器
        s.sendmail(msg_from, msg_to, msg.as_string()) # 发邮件 转换为字符串
        return ('发送成功！', random_num)
    except Exception:
        return ('抱歉！您的邮件发送失败，请重试', False)
    finally:
        s.quit() #退出
