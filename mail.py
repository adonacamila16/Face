# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
from email.message import EmailMessage


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender-mail', 'sender passwrd')
email = EmailMessage()
email['from'] = 'sender-mail'
email['to'] = 'Reciever-mail'
email['subject'] = 'subject'
email.set_content('content-message')
server.send_message(email)
