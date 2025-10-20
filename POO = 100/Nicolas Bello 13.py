class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def get_salario_anual(self):
        return self.salario * 12

    def mostrar_info(self):
        return f"Empleado: {self.nombre}, Salario mensual: ${self.salario:.2f}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def asignar_tarea(self, tarea, empleado):
        return f"{self.nombre} (Gerente de {self.departamento}) asigna '{tarea}' a {empleado.nombre}."

    def calcular_bonus(self):
        return self.salario * 0.15


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje_principal):
        super().__init__(nombre, salario)
        self.lenguaje_principal = lenguaje_principal

    def escribir_codigo(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje_principal}."

    def calcular_bonus(self):
        return self.salario * 0.10


empleado_base = Empleado("Nicolas Bello", 3000)
print(empleado_base.mostrar_info())
print(f"Salario anual de {empleado_base.nombre}: ${empleado_base.get_salario_anual():.2f}")

gerente1 = Gerente("Santiago Neira", 6000, "Marketing")
print(gerente1.mostrar_info())
print(f"Bonus de {gerente1.nombre}: ${gerente1.calcular_bonus():.2f}")
print(gerente1.asignar_tarea("Planificar campaña", empleado_base))

desarrollador1 = Desarrollador("Bello Neira", 4500, "Python")
print(desarrollador1.mostrar_info())
print(f"Bonus de {desarrollador1.nombre}: ${desarrollador1.calcular_bonus():.2f}")
print(desarrollador1.escribir_codigo())
