# 🧪 Desafio de Nivelamento - IntuitiveCare

Este repositório contém a solução para os testes técnicos propostos na etapa de nivelamento do processo seletivo da **IntuitiveCare**. O projeto foi desenvolvido com foco em clareza, organização, boas práticas de programação e facilidade de avaliação.

---

## 📁 Estrutura do Projeto

Abaixo está a estrutura de pastas e arquivos do repositório, organizada por áreas de conhecimento conforme solicitado no teste.

intuitivecare-nivelamento/
├── .gitignore
├── requirements.txt
├── .env.example
├── README.md
│
├── web_scraping/
│   ├── main.py
│   ├── utils.py
│   ├── README.md
│   └── downloaded_pdfs/
│       ├── anexo_I.pdf
│       └── anexo_II.pdf
│
├── data_transform/
│   ├── extract_table.py
│   ├── transform_data.py
│   ├── README.md
│   ├── Teste_SeuNome.zip
│   └── data/
│       ├── input/
│       │   └── anexo_I.pdf
│       └── output/
│           └── rol_procedimentos.csv
│
├── database/
│   ├── README.md
│   ├── ddl/
│   │   └── create_tables.sql
│   ├── dml/
│   │   └── insert_data.sql
│   ├── queries/
│   │   └── analytics.sql
│   └── data/
│       ├── operadoras_ativas.csv
│       ├── demonstracoes_2023.csv
│       └── demonstracoes_2024.csv
│
├── api_vue/
│   ├── README.md
│   ├── backend/
│   │   ├── app.py
│   │   ├── utils.py
│   │   └── operadoras.csv
│   ├── frontend/
│   │   └── src/
│   └── postman/
│       └── api_tests.postman_collection.json
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

