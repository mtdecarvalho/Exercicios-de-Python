class Disciplina:
    def ler( self ):
        self.codigo = int(input())
        self.nome = input()
        self.professor = input()
        self.creditos = int(input())
        self.ano = int(input())
        self.semestre = int(input())
        self.nota1 = float(input())
        self.nota2 = float(input())
        self.media = (self.nota1 + 2.0*self.nota2)/3.0


    def mostrar( self ):
        print(
            "Codigo    : {0:0>4}\n"
            "Nome      : {1}\n"
            "Professor : {2}\n"
            "Creditos  : {3}\n"
            "Ano       : {4}\n"
            "Semestre  : {5}\n"
            "Nota1     : {6:.2f}\n"
            "Nota2     : {7:.2f}\n"
            "Media     : {8:.2f}"
            .format(self.codigo, self.nome, self.professor,
            self.creditos, self.ano, self.semestre, self.nota1,
            self.nota2, self.media))


if __name__ == "__main__":
    a = Disciplina()
    a.ler()
    a.mostrar()