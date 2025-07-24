# Sistema de Controle de Loja

## Descrição

Este projeto consiste em um sistema desktop para controle de vendas em uma loja, desenvolvido em Python utilizando a biblioteca Tkinter para interface gráfica, arquitetura MVC para organização do código e banco de dados MySQL para persistência dos dados. O sistema visa facilitar a gestão de clientes, produtos, usuários e vendas, proporcionando uma solução robusta e escalável para pequenos comércios.

## Funcionalidades

- Autenticação de usuários com controle de acesso
- Cadastro, edição e exclusão de clientes
- Cadastro, edição e exclusão de produtos com controle de estoque
- Registro de vendas com múltiplos itens e cálculo automático do total
- Visualização do histórico de vendas
- Interface gráfica intuitiva e responsiva desenvolvida em Tkinter
- Estrutura modular baseada no padrão MVC para melhor manutenção e escalabilidade

## Tecnologias Utilizadas

- Linguagem: Python 3.x
- Interface Gráfica: Tkinter
- Banco de Dados: MySQL
- Arquitetura: MVC (Model-View-Controller)
- Controle de Versão: Git e GitHub

## Estrutura do Projeto

projeto_avaliador/
├── app/
│ ├── controllers/ # Controladores da aplicação
│ ├── models/ # Modelos de dados e acesso ao banco
│ ├── views/ # Telas e componentes da interface
│ ├── database/ # Scripts e configuração do banco de dados
│ └── main.py # Ponto de entrada da aplicação
├── docs/
│ ├── requisitos.txt # Documento com requisitos funcionais e não funcionais
│ ├── algoritmo.txt # Descrição das funcionalidades em formato algorítmico
│ ├── DER.md # Modelo Entidade-Relacionamento
│ └── modelo_banco.png # Diagrama visual do banco de dados
├── .env # Arquivo com variáveis de ambiente (configurações sensíveis)
├── README.md # Documentação principal do projeto
└── .gitignore # Configurações para o Git

bash
Copiar
Editar

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/projeto_avaliador.git
Acesse a pasta do projeto:

bash
Copiar
Editar
cd projeto_avaliador
(Opcional) Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure o arquivo .env com suas credenciais MySQL:

ini
Copiar
Editar
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
Importe o script SQL para criação do banco e tabelas:

bash
Copiar
Editar
mysql -u seu_usuario -p nome_do_banco < app/database/banco.sql
Execução
Execute a aplicação utilizando:

bash
Copiar
Editar
python app/main.py
Após o login, você poderá acessar as funcionalidades do sistema através da interface gráfica.

Contribuição
Contribuições são bem-vindas. Para colaborar:

Faça um fork do projeto.

Crie uma branch específica para sua alteração (git checkout -b feature/nome-da-feature).

Realize os commits com mensagens claras.

Envie um pull request para análise.

Licença
Distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

Autor
Seu Nome
Contato: seu.email@exemplo.com