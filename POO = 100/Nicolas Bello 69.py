import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ServicioEmail:
    def __init__(self, email_remitente, password):
        self.email_remitente = email_remitente
        self.password = password
        self.servidor_smtp = "smtp.gmail.com"
        self.puerto = 587

    def enviar_recordatorio_devolucion(self, email_destinatario, libro, fecha_limite):
        asunto = f"Recordatorio de devolución: {libro}"
        cuerpo = f"Estimado usuario,\n\nRecuerde devolver el libro '{libro}' antes del {fecha_limite}.\n\nGracias."
        mensaje = MIMEMultipart()
        mensaje['From'] = self.email_remitente
        mensaje['To'] = email_destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        try:
            servidor = smtplib.SMTP(self.servidor_smtp, self.puerto)
            servidor.starttls()
            servidor.login(self.email_remitente, self.password)
            servidor.send_message(mensaje)
            servidor.quit()
            return f"Correo enviado a {email_destinatario}"
        except Exception as e:
            return f"Error al enviar correo: {e}"
