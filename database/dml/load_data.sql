
\COPY operadora(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, representante, data_registro_ans) FROM './database/data/operadora.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY operadora_contato(ddd, telefone, fax, endereco_eletronico, registro_ans) FROM './database/data/contato.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY operadora_endereco(logradouro, numero, complemento, bairro, cidade, uf, cep, registro_ans) FROM './database/data/endereco.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');

\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/1T2023_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/2T2023_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/3T2023_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/4T2023_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');

\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/1T2024_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/2T2024_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/3T2024_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
\COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM './database/data/4T2024_validos.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', ENCODING 'UTF8');
