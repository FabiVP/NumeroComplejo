class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = "+" if self.imaginario >= 0 else "-"
        return f"{self.real} {signo} {abs(self.imaginario)}i"

    def suma(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def resta(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def division(self, otro):
        if otro.real == 0 and otro.imaginario == 0:
            raise ValueError("No se puede dividir entre 0.")
        divisor = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
        return NumeroComplejo(real, imaginario)


# Ejemplo de uso
num1 = NumeroComplejo(4, 5)
num2 = NumeroComplejo(2, -3)

print("Suma:", num1.suma(num2))
print("Resta:", num1.resta(num2))
print("Multiplicación:", num1.multiplicacion(num2))
print("División:", num1.division(num2))

