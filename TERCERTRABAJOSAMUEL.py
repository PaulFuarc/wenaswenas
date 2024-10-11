import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

mi_circulo = Circulo(10)

area = mi_circulo.calcular_area()
circunferencia = mi_circulo.calcular_circunferencia()

print(f"El área del círculo es: {area:.2f}")  
print(f"La circunferencia del círculo es: {circunferencia:.2f}")