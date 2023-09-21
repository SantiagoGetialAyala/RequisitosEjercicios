class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados=None):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados if subordinados is not None else []

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_contacto):
        super().__init__(nombre, edad)
        self.telefono_contacto = telefono_contacto

# Ejemplo de uso
empleado1 = Empleado("Juan", 30, 50000)
empleado2 = Directivo("Laura", 35, 70000, "Gerente", [empleado1])
cliente1 = Cliente("Pedro", 45, "123-456-7890")

# Mostrar datos de empleados y clientes
print("Empleados:")
print(f"Nombre: {empleado1.nombre}, Edad: {empleado1.edad}, Sueldo Bruto: {empleado1.sueldo_bruto}")
print(f"Nombre: {empleado2.nombre}, Edad: {empleado2.edad}, Sueldo Bruto: {empleado2.sueldo_bruto}, Categoría: {empleado2.categoria}")

print("\nClientes:")
print(f"Nombre: {cliente1.nombre}, Edad: {cliente1.edad}, Teléfono de Contacto: {cliente1.telefono_contacto}")
