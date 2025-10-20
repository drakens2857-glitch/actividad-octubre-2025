import smtplib
from email.mime.text import MIMEText

def enviar_reporte(email, contenido):
    msg = MIMEText(contenido)
    msg['Subject'] = "Reporte Semanal Biblioteca"
    msg['From'] = "biblioteca@example.com"
    msg['To'] = email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("biblioteca@example.com", "clave")
        server.send_message(msg)
