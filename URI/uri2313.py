class Triangulo:
    def ler( self ):
        self.a, self.b, self.c = [float(x) for x in input().split()]
    

    def formaTriangulo( self ):
        if self.a >= self.b + self.c or self.b >= self.c + self.a or self.c >= self.a + self.b:
            return 0
        else:
            return 1
    

    def ehRetangulo( self ):
        if self.a ** 2 == self.b ** 2 + self.c ** 2 or self.b ** 2 == self.a ** 2 + self.c ** 2 or self.c ** 2 == self.a ** 2 + self.b ** 2:
            return 1
        else:
            return 0
    

    def tipo( self ):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return "Valido-Equilatero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Valido-Isoceles"
        else:
            return "Valido-Escaleno"


a = Triangulo()
a.ler()
if a.formaTriangulo():
    print(a.tipo())
    if a.ehRetangulo():
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
