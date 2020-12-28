class Impressora:
    @classmethod
    def imprimir_folha(cls, i):
        print('folha impressa ' + str(i))

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha(i)

Impressora.imprimir_folha(0)

print('==========')
Impressora.imprimir_livro(5)

impressora = Impressora()

print('==========')

impressora.imprimir_folha(0)