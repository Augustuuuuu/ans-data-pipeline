import pandas as pd
import os

def csv_para_insert(caminho_csv, tabela):
    df = pd.read_csv(caminho_csv, delimiter=';', dtype=str)
    colunas = ', '.join(df.columns)
    
    valores_lista = []
    for _, linha in df.iterrows():
        valores = ', '.join(f"'{str(valor).replace("'", "''")}'" if pd.notna(valor) else 'NULL' for valor in linha)
        valores_lista.append(f"({valores})")
    
    insert_sql = f"INSERT INTO {tabela} ({colunas}) VALUES \n" + ",\n".join(valores_lista) + ";"
    return insert_sql

caminho_pasta = r"C:\\Users\\augus\\OneDrive\\Documents\\GitHub\\Intuitive_Care_Test\\ArquivosTeste03"

arquivos_tabelas = {
    #"Relatorio_cadop.csv": "relatorio_cadop",
    "1T2023.csv": "dados",
    #"2t2023.csv": "dados",
    #"3T2023.csv": "dados",
    #"4T2023.csv": "dados"
}#
print("iniciando")
for arquivo, tabela in arquivos_tabelas.items():
    caminho_completo = os.path.join(caminho_pasta, arquivo)
    if os.path.exists(caminho_completo):
        sql_insert = csv_para_insert(caminho_completo, tabela)
        with open(f"{tabela}_insert.sql", "w", encoding="utf-8") as f:
            f.write(sql_insert)
        print(f"Arquivo SQL gerado: {tabela}_insert.sql")
    else:
        print(f"Arquivo não encontrado: {caminho_completo}")
