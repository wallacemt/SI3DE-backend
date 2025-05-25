# Icaro - Backend

![License](https://img.shields.io/static/v1?label=license&message=MIT&color=orange) &nbsp;
![Project Version](https://img.shields.io/static/v1?label=version&message=v0.1.0&color=yellow) &nbsp;
![Pull Request Welcome](https://img.shields.io/badge/PRs-welcome-green)

---

## 🚀 Sobre o Projeto

Este é o repositório do backend da plataforma **Icaro**, um sistema inteligente de gestão de estágios. Ele é responsável
por toda a lógica de negócio, autenticação de usuários, gerenciamento de dados de vagas, estudantes e empresas, e a
interação com o banco de dados.

Desenvolvido com **Python Flask**, este backend oferece uma API RESTful robusta e escalável. A segurança dos usuários é
garantida através de **JSON Web Tokens (JWT)** para autenticação e **Argon2** para o hash seguro de senhas. O banco de
dados utilizado é o **MongoDB Cloud (Atlas)**, que proporciona flexibilidade e alta disponibilidade para o armazenamento
e recuperação de dados.

---

## 📖 Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração e Execução](#configuracao-e-execucao)
- [Integrantes da Equipe](#integrantes-da-equipe)
- [Contribuições](#contribuicoes)
- [Licença](#licenca)

---

## 🛠️ Tecnologias Utilizadas

<div align='center' id="tecnologias-utilizadas">
  <img align='center' height='49' width='49' title='Python' alt='Python' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg'/> &nbsp;
  <img align='center' height='49' width='49' title='Flask' alt='Flask' src='https://play-lh.googleusercontent.com/ekpyJiZppMBBxCR5hva9Zz1pr3MYlFP-vWTYR3eIU7HOMAmg3jCJengHJ1GFgFMyyYc'/> &nbsp;
  <img align='center' height='49' width='49' title='MongoDB' alt='MongoDB' src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg'/> &nbsp;
  <img align='center' height='49' width='49' title='JWT' alt='JWT' src='https://cdn.worldvectorlogo.com/logos/jwt-3.svg' /> &nbsp;  
  <img align='center' height='50' width='50' title='Cors' alt='cors' src='https://github.com/bush1D3v/navarro_blog_api/assets/133554156/5dcd815b-e815-453b-9f3f-71e7dbcdf71d' /> 
</div>

---

## 📂 Estrutura do Projeto

```
icaro-frontend/
├── config/                 # Configuração de encriptografia de senha e envs do projeto
├── db/                     # Configuração da conexão com o banco de dados e os modelos
├── middlewares/            # Middlewares personalizados
├── routes/                 # Rotas da aplicação
├── services/               # Serviços personalizados
├── static/                 # Arquivos estáticos (estilos, imagens, etc.)
├── utils/                  # Arquivos uteis usados no projeto
├── venv/                   # Ambiente virtual do python
├── app.py                  # Aquivo principal do backend
├── render.yaml             # Arquivo de configuração do Docker para deploy no render
├── requirements.txt        # Dependências do projeto e scripts do projeto          
├── seed_jobs_migration.py  # Arquivo para popular o banco de dados com vagas
├── .env                    # Variáveis de ambiente
├──  README.md              # Esse arquivo.
```

---


## ⚙️ Configuração e Execução

### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
* **Python** (versão 3.9 ou superior)
* **pip** (gerenciador de pacotes do Python)
* **MongoDB Atlas Account** (ou uma instância local do MongoDB)
* **Docker** e **Docker Compose** (opcional, se desejar rodar via Docker)

### 1️⃣ Clonar o Repositório

```bash
git clone [https://github.com/wallacemt/SI3DE-backend.git](https://github.com/wallacemt/SI3DE-backend.git)
cd SI3DE-backend
```
### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```


### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as seguintes variáveis (substitua pelos seus valores):

```
MONGO_URI= # URI do banco de dados
JWT_SECRET = # Chave secreta JWT
PATH_FRONTEND= # Caminho do frontend
GEMINIAI_API_KEY= # Chave de API da Geminiai
```

###  Rodar a Aplicação

Certifique-se de que o ambiente virtual está ativado.

```bash
flask run
```

# 👥 Integrantes da Equipe

- Este projeto está sendo desenvolvido por um grupo de estudantes da faculdade Uniruy Wyden.

| Nome                |  Papel no Projeto  |                                                                                                                                GitHub |                                                                                                                                                      LinkedIn |
|---------------------|:------------------:|--------------------------------------------------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Cauê Ramos Valverde |   FrontEnd/Lider   |                                                                                           [Github](https://github.com/CaueKonceRamos) | [Linkedin](https://www.linkedin.com/in/cau%C3%AA-ramos-valverde-3480a42a5/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |
| Letícia Farias      |     Marketing      |                                                                                             [Github](https://github.com/LettyFariias) |                        [Linkedin](https://www.linkedin.com/in/lettyfarias/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |
| Deivide Maciel      |      BackEnd       |                                                                                              [Github](https://github.com/deivomaciel) |                     [Linkedin](https://www.linkedin.com/in/deivide-maciel/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |
| Beatriz de Abreu    | BackEnd/Pesquisas  |                                                                                                 [Github](https://github.com/Biabreuz) |         [Linkedin](https://www.linkedin.com/in/beatriz-de-abreu-4a1450232/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |
| Gustavo             | FrontEnd/Pesquisas |                                                                                                   [Github](https://github.com/guzhzh) |       [Linkedin](https://www.linkedin.com/in/gustavo-de-jesus-d-800595297/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |
| Kaique Simões       | FrontEnd/Pesquisas | [Github](https://www.linkedin.com/in/kaiquesimoes/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |                       [Linkedin](https://www.linkedin.com/in/kaiquesimoes/?lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BpGdss%2FJ4Te%2BvLL6gSzUExA%3D%3D) |

# 🤝 Contribuições

- Contribuições, sugestões e feedbacks são muito bem-vindos! Se você encontrou um bug, tem uma ideia de melhoria ou
  deseja adicionar uma nova funcionalidade, sinta-se à vontade para nos ajudar.

- Faça um fork do repositório.

    - Clone seu repositório forked para sua máquina local.
    - Crie uma nova branch para sua feature ou correção:

  ```bash
  git checkout -b feature/minha-nova-funcionalidade
  ```

    - Faça suas alterações e commit:

  ```bash
  git commit -m 'feat: adiciona funcionalidade X'
  ```

    - Envie suas alterações para o seu fork:

  ```bash
  git push origin feature/minha-nova-funcionalidade
  ```

    - Abra um Pull Request para a branch main do repositório original, explicando suas
      mudanças. [Agradecemos sua colaboração!]

# 📜 Licença

Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE na raiz do repositório.
