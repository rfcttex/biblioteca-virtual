class Menu:
    
    def __init__(self,opcao=0):
        
        self.__opcao = opcao
        
    @property
    def opcao(self, nova_opcao):
        
        pass

    @opcao.setter
    
    def opcao(self, nova_opcao):
        
        self.__opcao = nova_opcao
        
    
    def __str__(self):
        return "[1]- Registar\n[2]- Pesquisar\n[3]- Vender\n[4]- Emprestar\n[5]- Sair"
        
    
    def escolha(self):
        
        op = int(input("---> "))
        
        return op