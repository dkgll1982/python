import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# 第三方 SMTP 服务
mail_host = "smtp.sina.com"     # SMTP服务器
mail_user = "dkgll@sina.com"    # 用户名
mail_pass = "guoda123456789"    # 授权密码，非登录密码
 
sender = 'dkgll@sina.com'       # 发件人邮箱(最好写全, 不然会失败)
receivers = ['dkgll@qq.com']    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
title = '人生苦短'              # 邮件主题
content = '我用Python'          #邮件正文

 
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendEmail(): 
    #message = MIMEText(content, 'plain', 'utf-8')                     # 内容, 格式, 编码
    message = MIMEText('<html><body><h1>Hello</h1>' +                  #HTML邮件
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
    message['From'] = _format_addr('Python爱好者 <%s>' % sender)        #显示发件人名称
    message['To'] = _format_addr('管理员 <%s>' % ",".join(receivers))   #msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
    message['Subject'] = title
 
    try:
        #smtpObj = smtplib.SMTP(mail_host, 25)      #  
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)         # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
 
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
 
    email_client.quit()
 
if __name__ == '__main__':
    sendEmail()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)