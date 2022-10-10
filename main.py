import sys

sys.setrecursionlimit(1500)


class Vertice:

    def __init__(self, chave, pai=None):
        self.chave = chave
        self.pai = pai
        self.menor = None
        self.maior = None

    def __str__(self):
        return str(self.chave)

    def apresentar(self, numero_espacos=0, sentido=""):
        espacos = " " * numero_espacos
        dir = esq = ""
        if self.menor:
            self.menor.apresentar(numero_espacos + 10, sentido="/")

        print(f"{espacos}{sentido}---->[{self.chave}]")

        if self.maior:
            self.maior.apresentar(numero_espacos + 10, sentido="\\")

        return f"{str(self)}{esq}{dir}"

    def representacao_com_parenteses(self):
        dir = esq = ""
        if self.menor:
            esq = self.menor.representacao_com_parenteses()

        if self.maior:
            dir = self.maior.representacao_com_parenteses()

        return f"({str(self)}{esq}{dir})"

    def representacao_com_recuo(self, numero_espacos=0):
        dir = esq = ""

        if self.menor:
            esq = self.menor.representacao_com_recuo(numero_espacos + 4)

        if self.maior:
            dir = self.maior.representacao_com_recuo(numero_espacos + 4)

        espacos = " " * numero_espacos

        return f"{esq}{espacos}{self}\n{dir}"

    def inserir(self, chave_nova):
        print(f"inserir {chave_nova}(chave atual: {self.chave}")
        if chave_nova < self.chave:
            if self.menor:
                print(f"Insirir {chave_nova} no lado menor")
                return self.menor.inserir(chave_nova)

            self.menor = Vertice(chave_nova, self)
            return self.menor

        elif chave_nova > self.chave:
            if self.maior:
                print(f"Inserir {chave_nova} no lado maior")
                return self.maior.inserir(chave_nova)

            self.maior = Vertice(chave_nova, self)
            return self.maior

        else:
            return self

    def _remover_folha(self):
        print("Remover FOLHA. Sou folha")
        if self.pai:
            if self.pai.menor is self:
                self.pai.menor = None

            else:
                self.pai.maior = None

            self.pai = None

        return self

    def _remover_pai_de_um_filho(self):
        print("Remover Pai de 1 filho. Sou pai de 1 filho")
        meu_pai = self.pai
        meu_filho = self.maior or self.menor

        if meu_pai is None:
            meu_filho.chave, self.chave = self.chave, meu_filho.chave
            return meu_filho.remover(meu_filho.chave)
        meu_filho.pai = meu_pai

        if meu_filho.menor is self:
            meu_pai.menor = meu_filho

        else:
            meu_pai.maior = meu_filho

        self.pai = None
        self.menor = None
        self.maior = None
        return self

    def _remover_pai_de_2_filhos(self):
        print("Remover pai de 2 filhos: Sou pai de 2 Filhos")
        menor = self.menor.buscar_menor()
        self.chave, menor.chave = menor.chave, self.chave
        return menor.remover(menor.chave)

    def remover(self, chave):
        print(f"Remover {chave} (chave atual: {self.chave}")
        if chave < self.chave:
            return self.menor and self.menor.remover(chave)

        elif chave > self.chave:
            return self.maior and self.maior.remover(chave)

        else:
            if self.menor and self.maior:
                return self._remover_pai_de_2_filhos()

            if self.menor or self.maior:
                return self._remover_pai_de_um_filho()

            return self._remover_folha()

    def imprimir_percurso_pre_ordem(self):

        if self.menor:
            self.menor.imprimir_percurso_per_ordem()

        print(self)
        if self.maior:
            self.maior.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):

        if self.menor:
            self.menor.imprimir_percurso_pos_ordem()

        if self.maior:
            self.maior.imprimir_percurso_pos_ordem()

        print(self)

    def buscar(self, chave_nova):
        print("")
        print(f"Procurando {chave_nova}. Chave atual: {self.chave}")

        if chave_nova < self.chave:
            return self.menor and self.menor.buscar(chave_nova)

        elif chave_nova > self.chave:
            return self.maior and self.maior.buscar(chave_nova)

        else:
            return self

    def buscar_menor(self):
        print(f"Procurando menor {self}")
        if self.menor:
            return self.menor.buscar_menor()
        return self

    def imprimir(self):
        print("_" * 20)
        print(self.representacao_com_parenteses())
        print("_" * 20)
        print(self.representacao_com_recuo())
        print("_" * 20)
        print(self.apresentar())
        print("_" * 20)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Vertice(chave)

        else:
            self.raiz.inserir(chave)
        self.raiz.imprimir()

    def remover(self, chave):
        if self.raiz is not None:
            removido = self.raiz.remover(chave)
            if removido is self.raiz:
                self.raiz = None

        self.raiz.imprimir()


arvore = ArvoreBinariaBusca()
# inserir
arvore.inserir(14)
arvore.inserir(4)
arvore.inserir(18)
arvore.inserir(0)
arvore.inserir(21)
arvore.inserir(17)
arvore.inserir(1)
arvore.inserir(8)
arvore.inserir(13)

# remoção

arvore.remover(13)

# remover pai de 1 filhos

arvore.remover(0)

# remover pai de 2 filhos e arvore

arvore.remover(14)

arvore.remover(99999)
