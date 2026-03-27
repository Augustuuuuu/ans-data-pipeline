# Pipeline de Dados ANS — Web Scraping, ETL, MySQL e Flask

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=flat&logo=vue.js&logoColor=4FC08D)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=flat&logo=pandas&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-005571?style=flat&logo=Flask)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Descrição

Este projeto foi desenvolvido como solução para um desafio técnico de um processo seletivo. A empresa solicitou que o nome não fosse divulgado, portanto o repositório é apresentado de forma anônima.

O projeto cobre um pipeline completo de dados em 4 módulos independentes:

1. **Web Scraping** — coleta automatizada de documentos PDF da ANS
2. **Transformação de Dados** — extração e conversão de PDFs para CSV com Pandas
3. **Banco de Dados** — importação e análise de +6 milhões de registros em MySQL
4. **API** — interface RESTful com Flask e frontend em Vue.js 3

## 📸 Screenshots

### Web Scraping
<img src="images_readme\download_pdfs.png" alt="Web Scraping" width="400" height="300" />

*Download dos anexos da ANS concluído*

### Transformação de Dados
<img src="images_readme\pdf_to_csv.png" alt="Transformação de Dados" width="400" height="300" />

*Extração de dados de PDF para CSV*

### Banco de Dados
<img src="images_readme\sql.png" alt="Banco de Dados" width="400" height="300" />

*Análise de dados no MySQL*

### Interface Web
<img src="images_readme\interface_de_pesquisa.png" alt="Interface Web" width="400" height="300" />

*Interface de busca de operadoras*

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- MySQL 8.0+ ou PostgreSQL 10.0+
- Node.js e npm (para o módulo de API)
- Postman (para testar a API)

## 📦 Módulos

### 1. Web Scraping (Teste01)
Acessa o site da ANS e realiza download dos anexos I e II em formato PDF, compactando-os em um único arquivo.

```bash
python webscraping_teste01.py
```

### 2. Transformação de Dados (Teste02)
Extrai dados de tabelas de PDFs e os converte para formato CSV.

```bash
python extrair_dados_teste02.py
```

### 3. Banco de Dados (Teste03)
Scripts SQL para manipulação e análise de dados das operadoras de saúde.

#### Processamento de Dados em Larga Escala
O módulo de Banco de Dados demonstra a capacidade de processar e analisar grandes volumes de dados:
- Mais de 6 milhões de registros importados e processados
- Dados históricos de demonstrações contábeis
- Informações cadastrais de operadoras ativas
- Análises complexas realizadas com eficiência

#### Preparação dos Dados
Os arquivos necessários já foram baixados e estão disponíveis na pasta `ArquivosTeste03`. Para preparar o ambiente, siga estes passos:

1. **Mover os Arquivos**
   - Copie todos os arquivos da pasta `ArquivosTeste03` para o diretório:
     ```
     C:\ProgramData\MySQL\MySQL Server 8.0\Uploads
     ```
   - Esta etapa é necessária para que o MySQL possa acessar os arquivos durante a importação

2. **Estrutura dos Arquivos**
   - Os arquivos estão organizados em duas subpastas:
     - `demonstracoes_contabeis`: contém os arquivos ZIP dos dados contábeis
     - `relatorio_cadop`: contém o arquivo CSV do relatório cadastral

3. **Extração dos Arquivos**
   - Extraia todos os arquivos ZIP dos dados contábeis
   - Mantenha o arquivo CSV do relatório cadastral como está

4. **Execução dos Scripts SQL**
   Após mover e extrair os arquivos, execute os scripts SQL na seguinte ordem:

   ```bash
   cd Manipulacao_MySQL(Teste03)
   
   # 1. Criar as tabelas
   mysql -u seu_usuario -p < create_table.sql
   
   # 2. Importar os dados
   mysql -u seu_usuario -p < dados_insert.sql
   
   # 3. Executar as queries de análise
   # Execute as queries que desejar após a importação dos dados
   ```

#### Análise de Dados
O banco de dados processou com sucesso mais de 6 milhões de registros, demonstrando a capacidade de:
- Importação eficiente de grandes volumes de dados
- Processamento de queries complexas em tempo hábil
- Análise de dados históricos e tendências
- Geração de relatórios analíticos detalhados

Abaixo estão os resultados das análises solicitadas:

1. **Top 10 Operadoras com Maiores Despesas no Último Trimestre**
   ```sql
   SELECT
       td.reg_ans,
       rc.razao_social,
       rc.nome_fantasia,
       rc.modalidade,
       rc.uf,
       td.total_despesa
   FROM
       (SELECT
           reg_ans,
           SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
       FROM
           dados
       WHERE
           descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
           AND data >= '2024-10-01'
           AND data <= '2024-12-31'
       GROUP BY
           reg_ans
       ORDER BY
           total_despesa DESC
       LIMIT 10) AS td
   JOIN
       relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
   ORDER BY
       td.total_despesa DESC;
   ```

   <img src="images_readme\resultado_pergunta1sql.png" alt="Resultado Query 1" width="800" height="400" />

2. **Top 10 Operadoras com Maiores Despesas no Último Ano**
   ```sql
   SELECT
       td.reg_ans,
       rc.razao_social,
       rc.nome_fantasia,
       rc.modalidade,
       rc.uf,
       td.total_despesa
   FROM
       (SELECT
           reg_ans,
           SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
       FROM
           dados
       WHERE
           descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
           AND data >= '2024-01-01'
           AND data <= '2024-12-31'
       GROUP BY
           reg_ans
       ORDER BY
           total_despesa DESC
       LIMIT 10) AS td
   JOIN
       relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
   ORDER BY
       td.total_despesa DESC;
   ```

   <img src="images_readme\resultado_pergunta2sql.png" alt="Resultado Query 2" width="800" height="400" />

### 4. API (Teste04)
Interface web para busca de operadoras de saúde.

```bash
cd API(Teste04)
# Iniciar servidor Python
python server.py
# Em outro terminal
npm run serve
```

## 💡 Exemplos de Uso

### 1. Web Scraping
```bash
# Executar o script de web scraping
python webscraping_teste01.py

# O script irá:
# - Acessar o site da ANS
# - Baixar os Anexos I e II em PDF
# - Compactar os arquivos em um único arquivo ZIP
```

### 2. Transformação de Dados
```bash
# Executar o script de extração de dados
python extrair_dados_teste02.py

# O script irá:
# - Extrair dados da tabela do Anexo I
# - Salvar em formato CSV
# - Substituir abreviações OD e AMB
# - Compactar o arquivo CSV
```

### 3. Banco de Dados
```sql
-- Exemplo de query para análise de despesas
SELECT
    td.reg_ans,
    rc.razao_social,
    rc.nome_fantasia,
    rc.modalidade,
    rc.uf,
    td.total_despesa
FROM
    (SELECT
        reg_ans,
        SUM(vl_saldo_final - vl_saldo_inicial) AS total_despesa
    FROM
        dados
    WHERE
        descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
        AND data >= '2024-10-01'
        AND data <= '2024-12-31'
    GROUP BY
        reg_ans
    ORDER BY
        total_despesa DESC
    LIMIT 10) AS td
JOIN
    relatorio_cadop rc ON td.reg_ans = rc.registro_ANS
ORDER BY
    td.total_despesa DESC;
```

### 4. API
```bash
# Iniciar o servidor Python
cd API(Teste04)
python server.py

# Em outro terminal, iniciar o frontend Vue.js
cd API(Teste04)
cd frontend
npm run serve ou npm run dev

# Acessar a interface web em:
# http://localhost:5173/
```

#### Interface Vue.js

##### Tela de Busca
<img src="images_readme\interface_de_pesquisa_buscar.png" alt="Tela de Busca" width="800" height="450" />

*Interface inicial para busca de operadoras*

##### Tela de Resultados
<img src="images_readme\interface_de_pesquisa_resultado.png" alt="Tela de Resultados" width="800" height="450" />

*Resultados da busca com detalhes das operadoras*

#### Testando a API com Postman

1. **Importar a Coleção**
   - Abra o Postman
   - Clique em "Import" e selecione o arquivo `postman_collection.json` da pasta `API(Teste04)`

2. **Configurar o Ambiente**
   - Crie um novo ambiente no Postman
   - Adicione a variável `base_url` com o valor `http://localhost:5000`

3. **GET /operadoras/{registro_ans}**
     - Busca uma operadora específica pelo registro ANS
     - Exemplo: `http://localhost:5000/api/search?q=saúde&field=all`

4. **Exemplo de Requisição**
   ```http
   GET http://localhost:5000/api/search?q=sp&field=all
   ```

5. **Resposta Esperada**
   ```json
   {
     "operadoras": [
       {
         "registro_ans": "123456",
         "razao_social": "Operadora de Saúde Exemplo",
         "nome_fantasia": "Saúde Exemplo",
         "modalidade": "Autogestão",
         "uf": "SP"
       }
     ],
     "total": 1
   }
   ```

## 🏗️ Arquitetura e Qualidade do Código

### Organização do Projeto
- **Estrutura Modular**: Separação clara entre módulos de Web Scraping, Transformação de Dados, Banco de Dados e API
- **Clean Architecture**: Separação de responsabilidades e camadas bem definidas
- **Padrões de Projeto**: Implementação de padrões como Repository, Service e Controller

### Boas Práticas Implementadas
- **Python**:
  - PEP 8
  - Type hints
  - Docstrings
  - Tratamento de exceções
  - Logging estruturado

- **SQL**:
  - Queries otimizadas
  - Índices apropriados
  - Normalização de dados
  - Views para consultas complexas

- **Frontend**:
  - Componentização
  - Estado gerenciado
  - Responsividade
  - Acessibilidade

### Performance e Escalabilidade
- **Otimização de Queries**: Processamento eficiente de mais de 6 milhões de registros
- **Cache**: Implementação de cache para consultas frequentes
- **Paginação**: Suporte a grandes volumes de dados
- **Concorrência**: Processamento paralelo onde aplicável

### Testes e Qualidade
- **Testes Unitários**: Cobertura de funcionalidades críticas
- **Testes de Integração**: Validação de fluxos completos
- **Testes de Performance**: Monitoramento de tempos de resposta
- **Code Review**: Processo de revisão de código implementado

### Controle de Versão
- **Git Flow**: Estrutura de branches organizada
- **Commits Semânticos**: Mensagens descritivas e padronizadas
- **Pull Requests**: Processo de revisão estruturado
- **Versionamento**: Controle de versões do projeto


## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Créditos

Desenvolvido por Augusto Saboia como solução para desafio técnico de processo seletivo. Os dados utilizados são públicos e disponibilizados pela ANS (Agência Nacional de Saúde Suplementar).

## 📝 Notas Adicionais

- Os dados utilizados são públicos e disponibilizados pela ANS
- O projeto foi desenvolvido com foco em boas práticas de programação e documentação
- Para dúvidas ou sugestões, abra uma issue no repositório
