class Subsequencia:
    def setTexto( self ):
        self.texto = input()
    

    def Ocorrencias( self, substring ):
        self.contador = 0
        self.index = 0
        while self.index < len(self.texto):
            i = self.texto.find(substring, self.index)
            if i == -1:
                return self.contador
            self.contador += 1
            self.index = i + 1


casos = 0
while True:
    try:
        a = Subsequencia()
        substr = input()
        a.setTexto()
        a.Ocorrencias(substr)
        print("Caso #{0}".format( casos+1 ))
        if a.contador == 0:
            print("Nao existe subsequencia")
        else:
            print("Qtd.Subsequencias: {0}\nPos: {1}".format(a.contador, a.index))
        casos += 1
        print("")
    except EOFError:
        break
