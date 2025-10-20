class Empleado:
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del empleado no puede estar vacío.")
        self.nombre = nombre

    def calcular_salario(self):
        raise NotImplementedError("Las subclases deben implementar el método 'calcular_salario()'")


class Asalariado(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        if not isinstance(salario_mensual, (int, float)) or salario_mensual < 0:
            raise ValueError("El salario mensual debe ser un número no negativo.")
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual


class PorHoras(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):
        super().__init__(nombre)
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora < 0:
            raise ValueError("La tarifa por hora debe ser un número no negativo.")
        if not isinstance(horas_trabajadas, (int, float)) or horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas deben ser un número no negativo.")
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas


class Comisionista(Empleado):
    def __init__(self, nombre, ventas_totales, porcentaje_comision):
        super().__init__(nombre)
        if not isinstance(ventas_totales, (int, float)) or ventas_totales < 0:
            raise ValueError("Las ventas totales deben ser un número no negativo.")
        if not isinstance(porcentaje_comision, (int, float)) or not (0 <= porcentaje_comision <= 1):
            raise ValueError("El porcentaje de comisión debe estar entre 0 y 1 (inclusive).")
        self.ventas_totales = ventas_totales
        self.porcentaje_comision = porcentaje_comision

    def calcular_salario(self):
        return self.ventas_totales * self.porcentaje_comision


def procesar_salario(empleado):
    print(f"El salario de {empleado.nombre} es: ${empleado.calcular_salario():.2f}")


empleado_asalariado = Asalariado("Ana García", 3000)
empleado_por_horas = PorHoras("Luis Pérez", 25, 160)
empleado_comisionista = Comisionista("María López", 10000, 0.15)

procesar_salario(empleado_asalariado)
procesar_salario(empleado_por_horas)
procesar_salario(empleado_comisionista)

plantilla = [
    Asalariado("Juan Rey", 2500),
    PorHoras("Sofía Castro", 30, 120),
    Comisionista("Carlos Mesa", 5000, 0.20),
    Asalariado("Elena Díaz", 4000)
]

print("\nCálculo de salarios para toda la plantilla:")
for emp in plantilla:
    procesar_salario(emp)
