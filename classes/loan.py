from classes.db import Conection
from classes.search import Pesquisar 

class Emprestar(Pesquisar):

    def __init__(self):
        super().__init__()
        self.con = Conection()

    def emprestar_livro(self, titulo):
        
        query_select = "SELECT * FROM LIVROS WHERE titulo LIKE ?"
        self.con.executar(query_select, (f"%{titulo}%",))
        livros = self.con._Conection__cursor.fetchall()

        if not livros:
            print("\nNenhum livro encontrado com esse título.")
            self.con.fechar()
            input("\nPrima Enter para continuar...")
            return

        print("\nLivros encontrados:")
        for livro in livros:
            if livro[4] == "Livro":
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Tipo: {livro[4]} | Unidades: {livro[8]}")
            else:
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Tipo: {livro[4]}")

        try:
            id_escolhido = int(input("\nDigite o ID do livro que quer emprestar: "))
            livro_escolhido = next((livro for livro in livros if livro[0] == id_escolhido), None)

            if not livro_escolhido:
                raise ValueError("ID não corresponde a nenhum livro na lista.")
        except ValueError:
            print("ID inválido.")
            self.con.fechar()
            input("\nPrima Enter para continuar...")
            return

        if livro_escolhido[4] == "Livro":
            unidades = livro_escolhido[8]
            if unidades <= 0:
                print("\nEste livro não tem unidades disponíveis para empréstimo.")
                self.con.fechar()
                input("\nPrima Enter para continuar...")
                return
        else:
            print("\nEste item não é um livro físico e não pode ser emprestado.")
            self.con.fechar()
            input("\nPrima Enter para continuar...")
            return

        email = input("Digite o email do utilizador: ").strip()

        query = "SELECT * FROM UTILIZADORES WHERE email = ?"
        self.con.executar(query, (email,))
        utilizadores = self.con._Conection__cursor.fetchall()

        if utilizadores:
            utilizador = utilizadores[0]
            print(f"Utilizador encontrado: {utilizador[1]} (ID {utilizador[0]})")
        else:
            print("Utilizador não encontrado. Vamos criar um novo.")
            nome = input("Digite o nome do utilizador: ").strip()
            telefone = input("Digite o telefone do utilizador: ").strip()

            query_inserir = "INSERT INTO UTILIZADORES (nome, email, telefone) VALUES (?, ?, ?)"
            self.con.executar(query_inserir, (nome, email, telefone))
            self.con._Conection__conn.commit()

            
            utilizador_id = self.con._Conection__cursor.lastrowid
            utilizador = (utilizador_id, nome, email, telefone)
            print(f"Utilizador criado com ID {utilizador_id}")

        
        novo_total = livro_escolhido[8] - 1
        query_update = "UPDATE LIVROS SET quantidade = ? WHERE id = ?"
        self.con.executar(query_update, (novo_total, livro_escolhido[0]))

        query_inserir_emprestimo = '''
            INSERT INTO EMPRESTIMOS (id_utilizador, id_livro, devolvido)
            VALUES (?, ?, 0)
        '''
        self.con.executar(query_inserir_emprestimo, (utilizador[0], livro_escolhido[0]))

        self.con._Conection__conn.commit()

        print(f"\nLivro '{livro_escolhido[1]}' emprestado com sucesso a {utilizador[1]}!")
        print(f"Unidades restantes: {novo_total}")

        self.con.fechar()
        input("\nPrima Enter para continuar...")


      
      
        



