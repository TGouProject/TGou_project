import datetime
import hashlib
from Login import models
from TGou import settings


# 生成hash值
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


# 生成并保存验证码
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


# 发送邮件
def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives
    subject, from_email, to = '来自www.TGou.com的注册确认邮件', settings.EMAIL_HOST_USER, email
    text_content = ''
    html_content = """
    <p>欢迎注册<a href="http://{}/api/v1.0/TGou/confirm?code={}" target=blank>www.TGou.com</a>，这里是TGou的站点，购你想购！</p>
    <p>请点击上方链接完成注册确认！</p>
    <p>此链接有效期为{}天！</p>
    """.format(
        '127.0.0.1:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
