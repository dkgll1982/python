import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart #带多个部分的邮件
from email.mime.base import MIMEBase

#参考链接：https://www.cnblogs.com/zhangxinqi/p/9113859.html

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
    # 邮件对象:
    message = MIMEMultipart()  
    message['From'] = _format_addr('Python爱好者 <%s>' % sender)        #显示发件人名称
    message['To'] = _format_addr('管理员 <%s>' % ",".join(receivers))   #msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
    message['Subject'] = title

    message.attach(MIMEText('<html><body><h1>Hello</h1>' +                  #HTML邮件
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(r'images\miaomiao.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='miaomiao.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='miaomiao.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        message.attach(mime)
    try: 
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