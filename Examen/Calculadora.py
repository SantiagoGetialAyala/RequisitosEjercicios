class Calculadora:
    def __init__(self):
        while True:
            try:
                self.numero1 = int(input("Ingrese el primer numero entero: "))
                self.numero2 = int(input("Ingrese el segundo numero entero: "))
                break  
            except ValueError:
                print("Error: Ingresa un número entero válido.")

    def suma(self):
        resultado = self.numero1 + self.numero2
        return resultado

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado

    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        return resultado

    def division(self):
        if self.numero2 == 0:
            return "Ingresa otro valor, no se puede dividir por cero"
        resultado = self.numero1 / self.numero2
        return resultado

if __name__ == "__main__":
    calculadora = Calculadora()

    print(f"Suma: {calculadora.suma()}")
    print(f"Resta: {calculadora.resta()}")
    print(f"Multiplicación: {calculadora.multiplicacion()}")
    print(f"División: {calculadora.division()}")
