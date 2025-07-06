from classes.books import *
from classes.search import *
from classes.config import clear

#pip install email-validator
from email_validator import validate_email, EmailNotValidError


class Vender(Pesquisar):
    def __init__(self):
        super().__init__()
        self.con = Conection()

    def vender_livro(self, titulo):
        query_select = "SELECT * FROM LIVROS WHERE titulo LIKE ?"
        self.con.executar(query_select, (f"%{titulo}%",))
        resultados = self.con._Conection__cursor.fetchall()

        if not resultados:
            print("\nNenhum livro encontrado com esse título.")
            self.con.fechar()
            input("\nPrima Enter para continuar...")
            return

        print("\nLivros encontrados:")
        for livro in resultados:
            if livro[4] =="Livro":
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Tipo: {livro[4]} | Unidades: {livro[8]}")
            
            else:
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Tipo: {livro[4]}")

        try:
            id_escolhido = int(input("\nDigite o ID do livro que quer vender: "))
            livro_escolhido = next((livro for livro in resultados if livro[0] == id_escolhido), None)

            if not livro_escolhido:
                raise ValueError("ID não corresponde a nenhum livro na lista.")
        except ValueError:
            print("ID inválido.")
            self.con.fechar()
            input("\nPrima Enter para continuar...")
            return
        
        if livro_escolhido[4] =="Livro":

            unidades = livro_escolhido[8]
            if unidades <= 0:
                print("\nEste livro não tem unidades disponíveis para venda.")
            else:
                novo_total = unidades - 1
                query_update = "UPDATE LIVROS SET quantidade = ? WHERE id = ?"
                self.con.executar(query_update, (novo_total, livro_escolhido[0]))
                self.con._Conection__conn.commit()
                print(f"\nLivro '{livro_escolhido[1]}' vendido com sucesso! Unidades restantes: {novo_total}")

            self.con.fechar()
            input("\nPrima Enter para continuar...")

        else:
                
            while True:
            
                email = input("Digite o email: ")

                try:
                    valid = validate_email(email)
                    print(f"Acesso enviado para o email: {valid.email}")
                    input("\nPrima Enter para continuar...")
                    clear()

                    break

                except EmailNotValidError:
                    print("Email inválido. Tente novamente.")

   

        
