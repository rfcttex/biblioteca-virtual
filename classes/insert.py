from classes.books import *
from classes.menu import Menu
from random import randint

class Inserir:
    def __init__(self, op):
        self.op = op

    def tipo(self):
        match self.op:
            case 1:
                titulo = input("Digite o título: ")
                autor = input("Digite o Autor: ")
                
                while True:
                    try:
                        paginas = int(input("Digite o número de páginas: "))
                        break
                    except ValueError:
                        print("Por favor, digite um número inteiro válido para páginas.")
                    
                    
                while True:
                    try:
                        qtd = int(input("Digite o número de unidades: "))
                        break
                    except ValueError:
                        print("Por favor, digite um número inteiro válido para quantidade.")

                
                livro = Livro(titulo, autor, paginas, "Livro",qtd)
                livro.inserir()

            case 2:
                titulo = input("Digite o título: ")
                autor = input("Digite o Autor: ")
                
                while True:
                    try:
                        paginas = int(input("Digite o número de páginas: "))
                        break
                    except ValueError:
                        print("Por favor, digite um número inteiro válido para páginas.")
                
                tamanho = str(randint(0, 100)) + "mb"
                extensao = input("Digite a extensão: ")

                ebook = Ebook(titulo, autor, paginas, "Ebook", tamanho, extensao)
                ebook.inserir()

            case 3:
                menu = Menu()
                print(menu)

                escolha = menu.escolha()

                match escolha:
                    case 1 | 2 | 3 | 4:
                        pass  # Ainda vais implementar
                    case 5:
                        exit()
                    case _:
                        print("Opção inválida")
