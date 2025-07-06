import sqlite3

class Conection:
    def __init__(self):
        self.__caminho_db = "data\\libary.db"
        self.__conn = self.__criar_conexao()
        self.__cursor = self.__conn.cursor()
        self.__criar_tabelas()

    def __criar_conexao(self):
        return sqlite3.connect(self.__caminho_db)

    def __criar_tabela_livros(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS LIVROS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            paginas INTEGER,
            tipo TEXT,
            tamanho TEXT,
            extensao TEXT,
            estado TEXT DEFAULT 'disponível',
            quantidade INTEGER
        )
    ''')
       

    def __criar_tabela_utilizadores(self):
       self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS UTILIZADORES (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT
        );
    ''')
       
       
    
    def __criar_tabela_emprestimos(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS EMPRESTIMOS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_utilizador INTEGER,
                id_livro INTEGER,
                data_emprestimo DATE DEFAULT CURRENT_DATE,
                data_devolucao DATE,
                devolvido BOOLEAN DEFAULT 0,
                FOREIGN KEY(id_utilizador) REFERENCES UTILIZADORES(id),
                FOREIGN KEY(id_livro) REFERENCES LIVROS(id)
            );
        ''')

    def __criar_tabelas(self):

        self.__criar_tabela_livros()
        self.__criar_tabela_utilizadores()
        self.__criar_tabela_emprestimos()

        self.__conn.commit()



    def executar(self, query, params=()):
        self.__cursor.execute(query, params)
        self.__conn.commit()

    def fechar(self):
        self.__conn.close()

