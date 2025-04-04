-- Remover o banco de dados se já existir
DROP DATABASE IF EXISTS IntuitiveCare;

-- Criar o banco de dados
CREATE DATABASE IntuitiveCare;

-- Usar o banco de dados criado
USE IntuitiveCare;

-- 1. Criar tabelas para armazenar os dados dos arquivos CSV
CREATE TABLE relatorio_cadop (
    registro_ANS VARCHAR(255) NOT NULL,
    cnpj VARCHAR(14),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(255),
    data_registro_ANS VARCHAR(255),
    PRIMARY KEY (registro_ANS)
);
ALTER TABLE relatorio_cadop CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE dados (
    data DATE,
    reg_ans VARCHAR(50) NOT NULL,
    cd_conta_contabil VARCHAR(50),
    descricao VARCHAR(255),
    vl_saldo_inicial DOUBLE,
    vl_saldo_final DOUBLE,
    PRIMARY KEY (data, reg_ans, cd_conta_contabil)
);
ALTER TABLE dados CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;