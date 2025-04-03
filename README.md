# 🧪 Desafio de Nivelamento - IntuitiveCare

Este repositório contém a solução para os testes técnicos propostos na etapa de nivelamento do processo seletivo da **IntuitiveCare**. O projeto foi desenvolvido com foco em clareza, organização, boas práticas de programação e facilidade de avaliação.

---

## 📁 Estrutura do Projeto

Abaixo está a estrutura de pastas e arquivos do repositório, organizada por áreas de conhecimento conforme solicitado no teste.
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

