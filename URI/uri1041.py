class Pontos:
    def ler ( self ):
        self.x, self.y = [float(x) for x in input().split()]

    def origem( self ):
        if self.x == 0 and self.y == 0:
            return 1
        else: 
            return 0

    def EixoX( self ):
        if self.y == 0:
            return 1
        else:
            return 0

    def EixoY( self ):
        if self.x == 0:
            return 1
        else:
            return 0
    
    def obterQuadrante( self ):
        if self.origem():
            return "Origem"
        elif self.EixoY():
            return "Eixo Y"
        elif self.EixoX():
            return "Eixo X"
        elif self.x > 0 and self.y > 0:
            return "Q1"
        elif self.x > 0 and self.y < 0:
            return "Q4"
        elif self.x < 0 and self.y > 0:
            return "Q2"
        else: 
            return "Q3"

if __name__ == '__main__':

    pontos = Pontos()
    pontos.ler()
    print(pontos.obterQuadrante())
