# Biblioteca Virtual

Sistema de gestão de biblioteca virtual desenvolvido em Python que permite gerenciar livros físicos e ebooks.

## Funcionalidades

- **Registrar**: Adicionar novos livros ou ebooks ao sistema
- **Pesquisar**: Buscar publicações por título
- **Vender**: Gerir vendas de livros
- **Emprestar**: Sistema de empréstimos
- **Base de dados**: Armazenamento persistente em SQLite

## Estrutura do Projeto

```
biblioteca-virtual/
├── main.py              # Arquivo principal do sistema
├── classes/             # Módulos do sistema
│   ├── menu.py         # Interface do menu principal
│   ├── books.py        # Classes Livro e Ebook
│   ├── insert.py       # Inserção de publicações
│   ├── search.py       # Pesquisa de publicações
│   ├── sell.py         # Funcionalidades de venda
│   ├── loan.py         # Sistema de empréstimos
│   ├── config.py       # Configurações do sistema
│   └── db.py           # Conexão com base de dados
└── data/
    └── libary.db       # Base de dados SQLite
```

## Requisitos

- Python 3.10+
- SQLite (incluído no Python)

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/rfcttex/biblioteca-virtual.git
cd biblioteca-virtual
```

2. Execute o programa:
```bash
python main.py
```

## Utilização

### Menu Principal
```
[1]- Registar
[2]- Pesquisar
[3]- Vender
[4]- Emprestar
[5]- Sair
```

### Registar Publicações
- **Livro**: Título, autor, páginas e quantidade
- **Ebook**: Título, autor, páginas, tamanho e extensão

### Pesquisar
Permite buscar publicações por título no sistema.

### Vender
Sistema para processar vendas de livros físicos.

### Emprestar
Funcionalidade para gerir empréstimos de publicações.

## Classes Principais

- **Publicacao**: Classe base para livros e ebooks
- **Livro**: Herda de Publicacao, inclui quantidade e estado
- **Ebook**: Herda de Publicacao, inclui tamanho e extensão
- **Menu**: Interface do utilizador
- **Inserir**: Gestão de inserção de publicações

## Base de Dados

O sistema utiliza SQLite para armazenar:
- Informações das publicações
- Estados dos livros (disponível/emprestado)
- Histórico de transações

## Contribuições

Contribuições são bem-vindas! Por favor, faça fork do projeto e submeta um pull request.

## Licença

Liçença livre para estudo
