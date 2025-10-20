from twilio.rest import Client

class ServicioNotificaciones:
    def __init__(self, account_sid, auth_token, numero_twilio):
        self.client = Client(account_sid, auth_token)
        self.numero_twilio = numero_twilio

    def enviar_sms(self, numero_destino, mensaje):
        try:
            message = self.client.messages.create(
                body=mensaje,
                from_=self.numero_twilio,
                to=numero_destino
            )
            return f"SMS enviado a {numero_destino}. SID: {message.sid}"
        except Exception as e:
            return f"Error al enviar SMS: {e}"

    def enviar_whatsapp(self, numero_destino, mensaje):
        try:
            message = self.client.messages.create(
                body=mensaje,
                from_='whatsapp:' + self.numero_twilio,
                to='whatsapp:' + numero_destino
            )
            return f"WhatsApp enviado a {numero_destino}. SID: {message.sid}"
        except Exception as e:
            return f"Error al enviar WhatsApp: {e}"
