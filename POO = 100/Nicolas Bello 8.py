class Empleado:
    def __init__(self, nombre, puesto, salario_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_mensual = salario_mensual

    def obtener_salario_anual(self):
        return self.salario_mensual * 12

    def aplicar_aumento(self, porcentaje_aumento):
        if 0 < porcentaje_aumento <= 100:
            aumento = self.salario_mensual * (porcentaje_aumento / 100)
            self.salario_mensual += aumento
            return f"Salario de {self.nombre} aumentado en {porcentaje_aumento}%. Nuevo salario mensual: ${self.salario_mensual:.2f}."
        else:
            return "El porcentaje de aumento debe estar entre 0 y 100."

    def mostrar_info(self):
        return f"Empleado: {self.nombre} | Puesto: {self.puesto} | Salario Mensual: ${self.salario_mensual:.2f} | Salario Anual: ${self.obtener_salario_anual():.2f}"


empleado1 = Empleado("Nicolas Bello", "Desarrollador", 3000)
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(10))
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(5))
print(empleado1.mostrar_info())
print(empleado1.aplicar_aumento(-2))

empleado2 = Empleado("Santiago Neira", "Diseñador", 2500)
print(empleado2.mostrar_info())
print(empleado2.aplicar_aumento(15))
print(empleado2.mostrar_info())
