from classes.db import Conection

class Publicacao:
    def __init__(self, titulo, autor, paginas, tipo):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._tipo = tipo

class Livro(Publicacao):
    def __init__(self, titulo, autor, paginas, tipo, qtd):
        super().__init__(titulo, autor, paginas, tipo)
        self.__qtd = qtd
        self.__estado = "Disponível"

    def inserir(self):
        con = Conection()
        con.executar(
            '''INSERT INTO LIVROS(titulo, autor, paginas, tipo, estado, quantidade) VALUES (?, ?, ?, ?, ?, ?)''',
            (self._titulo, self._autor, self._paginas, self._tipo, self.__estado, self.__qtd)
        )
        con.fechar()
        print("Inserido com sucesso")

class Ebook(Publicacao):
    def __init__(self, titulo, autor, paginas, tipo, tamanho, extensao):
        super().__init__(titulo, autor, paginas, tipo)
        self.__tamanho = tamanho
        self.__extensao = extensao

    def inserir(self):
        con = Conection()
        con.executar(
            '''INSERT INTO LIVROS(titulo, autor, paginas, tipo, tamanho, extensao) VALUES (?, ?, ?, ?, ?, ?)''',
            (self._titulo, self._autor, self._paginas, self._tipo, self.__tamanho, self.__extensao)
        )
        con.fechar()
        print("Inserido com sucesso")
