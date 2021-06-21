# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
from email.message import EmailMessage


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('adonathomas@gmail.com', 'adona2548')
email = EmailMessage()
email['from'] = 'adonathomas@gmail.com'
email['to'] = 'adonacamila@cet.ac.in'
email['subject'] = 'Not Wearing Mask'
email.set_content('A is not wearing mask')
server.send_message(email)