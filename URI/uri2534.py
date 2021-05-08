class Vetor:
    v = []
    def ler( self, N ):
        self.qtd = N 
        for i in range(0, self.qtd):
            self.v[i] = input()
