import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = 'ferqtexwinner@gmail.com'
password = 'bbea uiwx tthr hndg'

recipent = input("Correo destinatario: ")

message = MIMEMultipart()
message['From'] = email
message['To'] = recipent
message['Subject'] = input('Asunto: ')

body = input('Texto: ')
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(email, password)

smtp_server.sendmail(email, recipent, message.as_string())
smtp_server.quit()
print('Email enviado')

