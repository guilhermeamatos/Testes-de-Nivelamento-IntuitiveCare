# 🧪 Desafio de Nivelamento - IntuitiveCare

Este repositório contém a solução para os testes técnicos propostos na etapa de nivelamento do processo seletivo da **IntuitiveCare**. O projeto foi desenvolvido com foco em clareza, organização, boas práticas de programação e facilidade de avaliação.

---

## 📁 Estrutura do Projeto

Abaixo está a estrutura de diretorios e arquivos do repositório, organizada por teste um diretorio para cada teste  
```
.
├── README.md
├── api
│   ├── backend
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── requirements.txt
│   │   ├── routes
│   │   │   └── search.py
│   │   └── utils
│   │       └── csv_loader.py
│   └── frontend
│       ├── README.md
│       ├── babel.config.js
│       ├── jsconfig.json
│       ├── package-lock.json
│       ├── package.json
│       ├── public
│       │   ├── favicon.ico
│       │   └── index.html
│       ├── src
│       │   ├── App.vue
│       │   ├── assets
│       │   │   └── logo.png
│       │   ├── components
│       │   │   └── SearchOperadoras.vue
│       │   └── main.js
│       └── vue.config.js
├── data_transform
│   ├── Teste_Guilherme.zip
│   ├── csv_transformer.py
│   ├── data
│   │   └── output
│   │       └── rol_procedimentos.csv
│   ├── main.py
│   ├── pdf_extractor.py
│   └── tests
│       ├── test_csv_transformer.py
│       └── test_pdf_extractor.py
├── database
│   ├── analytics
│   │   ├── ano.sql
│   │   └── trimestre.sql
│   ├── data
│   │   ├── 1T2023_validos.csv
│   │   ├── 1T2024_validos.csv
│   │   ├── 2T2024_validos.csv
│   │   ├── 2t2023_validos.csv
│   │   ├── 3T2023_validos.csv
│   │   ├── 3T2024_validos.csv
│   │   ├── 4T2023_validos.csv
│   │   ├── 4T2024_validos.csv
│   │   ├── Relatorio_cadop.csv
│   │   ├── contato.csv
│   │   ├── endereco.csv
│   │   └── operadora.csv
│   ├── ddl
│   │   └── create_tables.sql
│   ├── dml
│   │   └── load_data.sql
│   └── etl
│       ├── demonstracoes_data_cleaner.py
│       └── operadora_splitter.py
├── encodin.py
└── web_scraping
    ├── anexos.zip
    ├── config.py
    ├── downloaded_pdfs
    │   ├── Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf
    │   └── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf
    ├── main.py
    ├── scraper.py
    ├── tests
    │   ├── test_scraper.py
    │   ├── test_utils.py
    │   └── test_web_client.py
    ├── utils.py
    └── web_client.py
```

__
## ⚙️ Requisitos

- Python 3.8+
- Node.js (para o frontend Vue)
- MySQL ou PostgreSQL (para testes de banco)
- Postman (para testes de API)

---

## 📦 Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/intuitivecare-nivelamento.git
cd intuitivecare-nivelamento
```
### 2. Instalar as dependências

Crie e ative um ambiente virtual, depois instale as dependências:

```
python -m venv venv
# No Linux/Mac:
source venv/bin/activate
# No Windows:
venv\Scripts\activate
pip install -r requirements.txt
```
## 🚀 Executar os Scripts

Para rodar cada etapa do processo manualmente, siga as instruções abaixo a partir da raiz do projeto:

### 1. Web Scraping

Navegue até a raiz do projeto e execute:

```bash
 python .\web_scraping\main.py
 ```

### 2. Transformação de dados 

Navegue até a raiz do projeto e execute:

```bash
 python .\data_transform\main.py
 ```

## 3. Banco de Dados

Para realizar essa etapa, primeiro é preciso preparar os dados antes de cadastrá-los no PostgreSQL. Isso envolve executar o web scraping e a limpeza dos dados.

### 3.1. Preparar os Dados

#### 3.1.1 Executar o Web Scraping
Este script baixa os dados e extrai os arquivos CSV necessários:

```bash
python database/scraper/scraper_data.py
```
#### 3.1.2 Executar a Limpeza dos Dados
Após o scraping, execute os scripts de limpeza para processar e formatar os dados:
```bash
python database/etl/demonstracoes_data_cleaner.py
python database/etl/operadora_splitter.py
```
#### 3.2. Cadastrar os Dados no PostgreSQL
Depois que os dados estiverem preparados, execute os scripts SQL para criar as tabelas e inserir os dados no banco de dados PostgreSQL.
```bash
psql -U seu_usuario -f .\database\ddl\create_tables.sql
psql -U seu_usuario -d db_guilherme -f .\database\dml\load_data.sql
```
### 3.3. Consultas e Análise dos Dados

Após a inserção dos dados no PostgreSQL, é hora de explorar as informações. Para realizar as consultas:

3.3.1. **Abra seu SGBD preferido:**  
   Recomendamos o uso do pgAdmin para uma interface amigável.

3.3.2. **Conecte-se ao banco de dados:**  
   Utilize o banco de dados `db_guilherme`.

3.3.3. **Execute as consultas:**  
   No diretório `database/analytics` você encontrará os scripts SQL com as consultas preparadas. Basta copiar e colar ou importar esses scripts no seu pgAdmin e executá-los para visualizar os resultados.

### 4. API

Para ver a API em plena execução, siga os passos abaixo:

#### 4.1 Iniciar o Backend

No terminal, a partir da raiz do projeto, execute:

```bash
python api/backend/app.py
```
Isso iniciará o servidor backend.

#### 4.2 Iniciar o Frontend
Abra um novo terminal, navegue até o diretório do frontend e execute:
```bash
npm install
npm run serve
```
Esses comandos instalarão as dependências do projeto Vue.js e iniciarão o servidor de desenvolvimento para o frontend.
Após a execução, acesse a URL exibida no terminal para visualizar a aplicação em funcionamento.



