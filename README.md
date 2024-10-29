🌍 Projeto de Gerenciamento de Coleções Geográficas
Este projeto é uma aplicação web desenvolvida com Flask e MongoDB que permite gerenciar coleções de informações geográficas sobre países, cidades e rios. Ele inclui funcionalidades de cadastro e listagem para cada coleção, com uma interface intuitiva e simples.

🔧 Funcionalidades
Gerenciamento de Países:

Cadastro de países com informações como nome, continente, população e PIB.
Listagem de todos os países cadastrados.
Gerenciamento de Cidades:

Cadastro de cidades com informações de nome, país, população e se é capital.
Listagem de todas as cidades cadastradas.
Gerenciamento de Rios:

Cadastro de rios com informações de nome, nascente, país e extensão no continente.
Listagem de todos os rios cadastrados.

🚀 Tecnologias Utilizadas
Backend: Flask
Banco de Dados: MongoDB
Frontend: HTML e CSS (para uma interface simples e responsiva)
Controle de Versão: Git

⚙️ Instalação e Configuração
Clone o repositório:

bash
Copiar código
git clone git@github.com:seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Instale as dependências: Certifique-se de que o Python está instalado e então execute:

bash
Copiar código
pip install -r requirements.txt
Configure o MongoDB:

Certifique-se de que o MongoDB está rodando localmente ou configure o acesso a um servidor remoto.
Altere o URI de conexão para o MongoDB, se necessário, no arquivo app.py.
Execute a aplicação:

bash
Copiar código
python app.py
Acesse a aplicação em http://127.0.0.1:5000.

📈 Próximas Implementações
 Validação de dados no frontend e backend
 Funcionalidade de busca para cada coleção
 Paginação de resultados
🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
