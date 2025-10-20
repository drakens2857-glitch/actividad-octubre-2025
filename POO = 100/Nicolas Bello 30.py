from abc import ABC, abstractmethod

class Notificacion(ABC):
    def __init__(self, destinatario, mensaje):
        if not isinstance(destinatario, str) or not destinatario.strip():
            raise ValueError("El destinatario no puede estar vacío.")
        if not isinstance(mensaje, str) or not mensaje.strip():
            raise ValueError("El mensaje no puede estar vacío.")
        self.destinatario = destinatario
        self.mensaje = mensaje

    @abstractmethod
    def enviar(self):
        pass

    def mostrar_previsualizacion(self):
        return f"Previsualización para {self.destinatario}: '{self.mensaje[:50]}...'"


class NotificacionEmail(Notificacion):
    def __init__(self, destinatario, mensaje, asunto, remitente="no-reply@ejemplo.com"):
        super().__init__(destinatario, mensaje)
        if not isinstance(asunto, str) or not asunto.strip():
            raise ValueError("El asunto no puede estar vacío.")
        self.asunto = asunto
        self.remitente = remitente

    def enviar(self):
        print(f"\n--- Enviando Email ---")
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Mensaje: {self.mensaje}")
        print(f"Email enviado exitosamente.")


class NotificacionSMS(Notificacion):
    def __init__(self, destinatario, mensaje):
        if not destinatario.isdigit() or len(destinatario) < 7:
            raise ValueError("El destinatario de SMS debe ser un número de teléfono válido.")
        super().__init__(destinatario, mensaje)

    def enviar(self):
        print(f"\n--- Enviando SMS ---")
        print(f"A: {self.destinatario}")
        print(f"Mensaje: {self.mensaje[:160]}...")
        print(f"SMS enviado exitosamente.")


class NotificacionPush(Notificacion):
    def __init__(self, destinatario, mensaje, dispositivo_id):
        super().__init__(destinatario, mensaje)
        if not isinstance(dispositivo_id, str) or not dispositivo_id.strip():
            raise ValueError("El ID del dispositivo no puede estar vacío.")
        self.dispositivo_id = dispositivo_id

    def enviar(self):
        print(f"\n--- Enviando Notificación Push ---")
        print(f"Usuario: {self.destinatario} (Dispositivo ID: {self.dispositivo_id})")
        print(f"Alerta: {self.mensaje}")
        print(f"Notificación Push enviada exitosamente.")


def despachar_notificacion(notificacion):
    print(f"Previsualizando: {notificacion.mostrar_previsualizacion()}")
    notificacion.enviar()


notificacion_bienvenida = NotificacionEmail(
    "usuario@ejemplo.com",
    "¡Bienvenido a nuestra plataforma! Gracias por registrarte. Esperamos que disfrutes de todas nuestras características.",
    "Bienvenido a la Plataforma"
)

notificacion_alerta_sms = NotificacionSMS(
    "612345678",
    "Su paquete ha sido entregado exitosamente. Código de seguimiento: ABC123XYZ. ¡Gracias por su compra!"
)

notificacion_actualizacion_app = NotificacionPush(
    "moviluser@ejemplo.com",
    "¡Nueva actualización disponible! Mejora de rendimiento y nuevas características te esperan.",
    "dev123abc456"
)

despachar_notificacion(notificacion_bienvenida)
despachar_notificacion(notificacion_alerta_sms)
despachar_notificacion(notificacion_actualizacion_app)

print("\n--- Pruebas de validación ---")
try:
    NotificacionEmail("", "Mensaje", "Asunto")
except ValueError as e:
    print(f"Error esperado: {e}")
try:
    NotificacionSMS("no-es-un-numero", "Mensaje")
except ValueError as e:
    print(f"Error esperado: {e}")
