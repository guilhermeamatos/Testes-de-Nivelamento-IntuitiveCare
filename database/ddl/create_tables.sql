CREATE DATABASE db_guilherme;

\connect db_guilherme

CREATE TABLE IF NOT EXISTS operadora (
    registro_ans            VARCHAR(300) PRIMARY KEY,
    cnpj                    VARCHAR(20)        NOT NULL,
    razao_social            VARCHAR(255)       NOT NULL,
    nome_fantasia           VARCHAR(255),
    modalidade              VARCHAR(50),
    representante           VARCHAR(255),
    data_registro_ans       DATE
);

CREATE TABLE IF NOT EXISTS operadora_endereco (
    id_endereco             SERIAL PRIMARY KEY,
    registro_ans            VARCHAR(300) NOT NULL,
    logradouro              VARCHAR(255),
    numero                  VARCHAR(50),
    complemento             VARCHAR(50),
    bairro                  VARCHAR(100),
    cidade                  VARCHAR(100),
    uf                      VARCHAR(2),
    cep                     VARCHAR(10),
    regiao_de_comercializacao VARCHAR(100),
    
    CONSTRAINT fk_operadora_endereco
        FOREIGN KEY (registro_ans)
        REFERENCES operadora (registro_ans)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS operadora_contato (
    id_contato              SERIAL PRIMARY KEY,
    registro_ans            VARCHAR(300) NOT NULL,
    ddd                     VARCHAR(4),
    telefone                VARCHAR(50),
    fax                     VARCHAR(15),
    endereco_eletronico     VARCHAR(255),
    
    CONSTRAINT fk_operadora_contato
        FOREIGN KEY (registro_ans)
        REFERENCES operadora (registro_ans)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id_demonstracao         SERIAL PRIMARY KEY,
    data                    DATE        NOT NULL,
    reg_ans                 VARCHAR(300) NOT NULL,
    cd_conta_contabil       VARCHAR(50),
    descricao               VARCHAR(255),
    vl_saldo_inicial        NUMERIC(18,2),
    vl_saldo_final          NUMERIC(18,2),
    
    CONSTRAINT fk_operadora_demonstracoes
        FOREIGN KEY (reg_ans)
        REFERENCES operadora (registro_ans)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);