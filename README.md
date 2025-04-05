# 🧪Testes de Nivelamento - IntuitiveCare

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
│   ├── csv_transformer.py
│   ├── main.py
│   ├── pdf_extractor.py
│   └── tests
│       ├── test_csv_transformer.py
│       └── test_pdf_extractor.py
├── database
│   ├── analytics
│   │   ├── ano.sql
│   │   └── trimestre.sql
│   ├── ddl
│   │   └── create_tables.sql
│   ├── dml
│   │   └── load_data.sql
│   ├── etl
│   │   ├── demonstracoes_data_cleaner.py
│   │   └── operadora_splitter.py
│   └── scraper
│       ├── __init__.py
│       └── scraper_data.py
├── encodin.py
├── requirements.txt
└── web_scraping
    ├── __init__.py
    ├── config.py
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
- PostgreSQL (para testes de banco)
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

### Testando a API com Postman

Você pode testar nossa API utilizando a Postman Collection disponível no link abaixo:

[API IntuitiveCare](https://yetrh3.postman.co/workspace/yetrh-Workspace~4b370f49-ad4c-49d8-9850-0ef50ca2a2c4/collection/23359082-bb27e278-df54-4aee-8805-bcf907d3af1e?action=share&creator=23359082
)

# Deploy na AWS

Foi realizado o deploy de uma aplicação **Python** (back-end) e **Vue.js** (front-end) na AWS, disponibilizando a funcionalidade de **busca textual** pelas operadoras.

## Endereço de Acesso

- **IP Público**: [http://3.133.135.191/](http://3.133.135.191/)

A aplicação está acessível neste endereço, onde é possível realizar a busca e visualizar os resultados retornados pelo back-end.

---

### Observações Importantes

1. **Arquitetura**:
   - **Front-end (Vue.js)**: Responsável pela interface da aplicação.
   - **Back-end (Python)**: Gera os resultados da busca textual pelas operadoras.

2. **Nginx**: Configurado como servidor web e proxy reverso para encaminhar as requisições ao back-end.

## Testes de Web Scraping e Transformação de Dados

Foram implementados casos de teste para as etapas de **Web Scraping** e **Transformação de Dados**. Para executar os testes, basta seguir as instruções abaixo:

### 1. Web Scraping

```bash
cd .\web_scraping\
python -m unittest discover
```
### 1. Transformação de Dados
```bash
cd .\data_transform
python -m unittest discover
```
# Experimento de Performance

Foi realizado um experimento para testar a efetividade de uma solução utilizando paralelismo para melhorar a performance de execução do script `demonstracoes_data_cleaner.py`. Foi implementada uma versão com 4 threads disponíveis no arquivo `demonstracoes_data_cleaner_multi_thread.py`.

**Resultados:**

- **Média Versão Paralela:** 1:32 (92 segundos)
- **Média Versão Sequencial:** 1:51 (111 segundos)
- **Melhoria de Performance:** Aproximadamente 17%





