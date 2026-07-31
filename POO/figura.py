class Figura:
    def __init__(self,color):
        self.color = color

    def area(self):
        return 0

    def perimetro(self):
        return 0

    def __str__(self):
        return f"{type(self).__name__}"


class Rectangulo(Figura):
    def __init__(self, color, b,a):
        super().__init__(color)
        self.base = b
        self.altura = a

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, color, b,a,lado_uno,lado_dos,lado_tres):
        super().__init__(color)
        self.base = b
        self.altura = a
        self.lado_uno = lado_uno
        self.lado_dos = lado_dos
        self.lado_tres = lado_tres

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado_uno + self.lado_dos + self.lado_tres

