#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '555555@126.com'
sender_pass = '123456'
receivers = '529781013@qq.com'

def main():
    
    email_msg = """
    <h1>请查收邮件！</h1>
    <p>发邮件测试.</p>
    <span style='color:red;'>我飘了吗？</span>
    """
    # email_msg = "<html><body><h1>请查收邮件！</h1><p>发邮件测试.</p></body></html>" # "Hi, 我飘了吗? Sorry, This is a test email!"
    message = MIMEText(email_msg, 'html', 'utf-8')
    message['From'] = sender # Header("张总", 'utf-8')
    message['To'] = receivers #  Header("钟总", 'utf-8')

    #subject = '危险来电-邮件测试'
    message['Subject'] = Header('来自SMTP的问候-邮件测试', 'utf-8').encode() # Header(subject, 'utf-8')

    # 输入SMTP服务器地址:
    smtp_server = 'smtp.126.com'

    try:
        server = smtplib.SMTP(smtp_server, 25)  #'smtp.live.com'
        #server.set_debuglevel(1)
        server.login(sender, sender_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receivers], message.as_string())
        server.quit()  # 关闭连接
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件")
        print(e)


if __name__ == "__main__":
    main()