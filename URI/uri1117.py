def validar():
    aux = float(input())
    sair = False
    while ( sair == False ):
        if aux < 0 or aux > 10:
            print("nota invalida")
            aux = float(input())
        else:
            sair = True
            return aux

class Notas:
    def ler( self ):
        self.nota1 = validar()
        self.nota2 = validar()


    def media( self ):
        return (self.nota1 + self.nota2) / 2


if __name__ == '__main__':
    a = Notas()
    a.ler()
    print("media = {:.2f}".format( float(a.media()) ))
