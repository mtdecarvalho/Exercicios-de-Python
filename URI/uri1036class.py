import math



class Eq2Grau:
    def ler( self ):
        self.a, self.b, self.c = [float(x) for x in input().split()]
    

    def calculoDelta( self ):
        self.delta = (self.b**2) - (4 * self.a * self.c)
        return self.delta
    

    def raizes( self ):
        if self.delta > 0:
            return 2
        elif self.delta == 0:
            return 1
        else:
            return 0
    

    def raiz1( self ):
        if self.a > 0 and self.delta > 0:
            self.x1 = ((-self.b + math.sqrt(self.delta)) / (2*self.a))
            return self.x1
        else:
            return 0
    

    def raiz2(self):
        if self.a > 0 and self.delta > 0:
            self.x2 = ((-self.b - math.sqrt(self.delta)) / (2*self.a))
            return self.x2
        else:
            return 0


if __name__ == '__main__':
    a = Eq2Grau()
    a.ler()
    delta, raizes = a.calculoDelta(), a.raizes()
    x1, x2 = a.raiz1(), a.raiz2()
    if raizes == 0 or x1 == 0 or x2 == 0:
        print("Impossivel calcular")
    else:
        print("R1 = {:.5f}\nR2 = {:.5f}".format(x1, x2))
