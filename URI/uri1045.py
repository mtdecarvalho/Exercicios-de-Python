class Triangulo:
    def ler( self ):
        self.a, self.b, self.c = [float(x) for x in input().split()]


    def ordenar( self ):
        if self.b >= self.a and self.b >= self.c:
            self.aux1 = self.a
            self.a = self.b
            self.b = self.aux1
        elif self.c >= self.a and self.c >= self.b:
            self.aux1 = self.a
            self.aux2 = self.b
            self.a = self.c
            self.b = self.aux1
            self.c = self.aux2


    def formaTriangulo( self ):
        if self.a >= self.b + self.c:
            return 0
        else:
            return 1


    def tipoPeloAngulo( self ):
        if self.a ** 2 == self.b ** 2 + self.c ** 2:
            return "TRIANGULO RETANGULO"
        elif self.a ** 2 > self.b ** 2 + self.c ** 2:
            return "TRIANGULO OBTUSANGULO"
        elif self.a ** 2 < self.b ** 2 + self.c ** 2:
            return "TRIANGULO ACUTANGULO"


    def tipoPelosLados( self ):
        if self.a == self.b and self.a == self.c and self.b == self.c:
            return "TRIANGULO EQUILATERO"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "TRIANGULO ISOSCELES"


if __name__ == '__main__':
    a = Triangulo()
    a.ler()
    a.ordenar()
    if a.formaTriangulo():
        print (a.tipoPeloAngulo())
        if a.tipoPelosLados() != None:
            print(a.tipoPelosLados())
    else: 
        print("NAO FORMA TRIANGULO")
