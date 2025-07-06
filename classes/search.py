from classes.db import Conection

class Pesquisar:
    def __init__(self):
        self.__con = Conection()

    def por_titulo(self, titulo):
        query = "SELECT * FROM LIVROS WHERE titulo LIKE ?"
        self.__con.executar(query, (f"%{titulo}%",))
        resultados = self.__con._Conection__cursor.fetchall()

        if resultados:
            for livro in resultados:
                id = livro[0]
                titulo = livro[1]
                autor = livro[2]
                formato = livro[4]

                if formato == "Ebook":
                    tamanho = livro[5]
                    extensao = livro[6]
                    print(f"ID: {id} | Título: {titulo} | Autor: {autor} | Formato: {formato} | Tamanho: {tamanho} | Extensão: {extensao}")
                else:
                    estado = livro[7]
                    unidades = livro[8]
                    print(f"ID: {id} | Título: {titulo} | Autor: {autor} | Formato: {formato} | Estado: {estado} | Unidades: {unidades}")
        else:
            print("Nenhum livro encontrado com esse título.")

        input("Prima enter para continuar...")
        self.__con.fechar()
