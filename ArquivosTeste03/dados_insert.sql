/* Importando os dados do csv 1T2023 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2023.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 2T2023 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2t2023.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 3T2023 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2023.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 4T2023 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 1T2024 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2024.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 2T2024 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2T2024.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 3T2024 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2024.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;

/* Importando os dados do csv 4T2024 */
LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2024.csv"
INTO TABLE dados
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final);

select count(*) from dados;