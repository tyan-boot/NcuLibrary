import email
import smtplib
from .. import email_host
from .. import email_user
from .. import email_pwd


def send_mail(to_user, book_ids):
    smtp = smtplib.SMTP(email_host)
    smtp.login(email_user, email_pwd)

    books = ','.join(book_ids)
    msg = email.mime.MIMEText(books, 'text', 'utf-8')
    msg['Subject'] = email.header.Header('Book Notify', 'utf-8')

    smtp.sendmail(email_user, to_user, msg.an_string())
    smtp.quit()
