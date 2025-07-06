from classes.menu import *
from classes.insert import *
from classes.search import Pesquisar
from classes.config import *
from classes.sell import Vender
from classes.loan import Emprestar


def main():
    
   menu = Menu()
   
   
   while True:
   
    print(menu)
    
    escolha = menu.escolha()
    

    match escolha:
        
        case 1:
            
            print("[1]- Livro\n[2]- Ebook\n[3]- Voltar")
            op = int(input("---> "))
            
            inserir = Inserir(op)
            
            inserir.tipo()
            clear()
            
        case 2:
            
            titulo = input("Digite o título para pesquisar: ")
            pesquisa = Pesquisar()
            pesquisa.por_titulo(titulo)
            clear()

        case 3:
            
            titulo = input("Digite o título para pesquisar: ")

            vender = Vender()
            vender.vender_livro(titulo)
        
        case 4:
            
            titulo = input("Digite o título para pesquisar: ")

            emprestar = Emprestar()
            emprestar.emprestar_livro(titulo)
        
        case 5:
            
            exit()
            
            break
        
        case _ :
            
            print("Opção inválida")
        

   


if __name__ == "__main__":
    
    main()