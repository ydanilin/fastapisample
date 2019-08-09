import emails
from emails.template import JinjaTemplate as T


message = emails.html(
    subject=T('Payment Receipt No.{{ billno }}'),
    html=T('<p>Dear {{ name }}! This is a receipt...'),
    mail_from=('Dj Huj', 'manundraria@yandex.ru')
)

res = message.send(
    to=('Yuru Danilin', 'yuvede@gmail.com'),
    render={'name': 'John Brown', 'billno': '141051906163'},
    smtp={
        'host': 'smtp.yandex.ru',
        'port': 465,
        'ssl': True,
        'user': 'manundraria',
        'password': '***'
    }
)

print(f"Sending status code: {res.status_code}")
