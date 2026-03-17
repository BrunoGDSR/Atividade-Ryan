class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def pre_ordem(no):
    if no:
        print(no.valor, end=" ")
        pre_ordem(no.esq)
        pre_ordem(no.dir)

def em_ordem(no):
    if no:
        em_ordem(no.esq)
        print(no.valor, end=" ")
        em_ordem(no.dir)

def pos_ordem(no):
    if no:
        pos_ordem(no.esq)
        pos_ordem(no.dir)
        print(no.valor, end=" ")


raiz = No(1)
raiz.esq = No(2)
raiz.dir = No(3)
pre_ordem(raiz)
