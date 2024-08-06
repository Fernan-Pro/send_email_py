import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender(QWidget):
    def __init__(self, icon_path):
        super().__init__()
        self.init_ui(icon_path)

    def init_ui(self, icon_path):
        # Título de la ventana
        self.setWindowTitle('Enviar Correo')
        self.setStyleSheet('background-color: #282c34; color: white;')

        # Establecer el ícono de la ventana
        self.setWindowIcon(QIcon(icon_path))

        # Etiquetas y campos de texto
        self.label_email = QLabel('Tu Email:')
        self.label_email.setStyleSheet('font-size: 14px;')
        self.entry_email = QLineEdit()

        self.label_password = QLabel('Tu Password:')
        self.label_password.setStyleSheet('font-size: 14px;')
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.label_recipient = QLabel('Correo Destinatario:')
        self.label_recipient.setStyleSheet('font-size: 14px;')
        self.entry_recipient = QLineEdit()

        self.label_subject = QLabel('Asunto:')
        self.label_subject.setStyleSheet('font-size: 14px;')
        self.entry_subject = QLineEdit()

        self.label_body = QLabel('Texto:')
        self.label_body.setStyleSheet('font-size: 14px;')
        self.text_body = QTextEdit()

        # Botón para enviar el correo
        self.btn_send = QPushButton('Enviar')
        self.btn_send.setStyleSheet('background-color: #61dafb; color: #282c34; font-size: 14px;')
        self.btn_send.clicked.connect(self.send_email)

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.label_email)
        layout.addWidget(self.entry_email)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)
        layout.addWidget(self.label_recipient)
        layout.addWidget(self.entry_recipient)
        layout.addWidget(self.label_subject)
        layout.addWidget(self.entry_subject)
        layout.addWidget(self.label_body)
        layout.addWidget(self.text_body)
        layout.addWidget(self.btn_send)

        self.setLayout(layout)

    def send_email(self):
        email = self.entry_email.text()
        password = self.entry_password.text()
        recipient = self.entry_recipient.text()
        subject = self.entry_subject.text()
        body = self.text_body.toPlainText()

        try:
            message = MIMEMultipart()
            message['From'] = email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login(email, password)
            smtp_server.sendmail(email, recipient, message.as_string())
            smtp_server.quit()

            QMessageBox.information(self, "Éxito", "Email enviado correctamente.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo enviar el correo.\nError: {str(e)}")

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon_path = 'gmail.png'  # Reemplaza con la ruta de tu ícono
    window = EmailSender(icon_path)
    window.show()
    sys.exit(app.exec_())
