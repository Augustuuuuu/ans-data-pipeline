import tabula
import pandas as pd
import zipfile
import os

# Extrair todas as tabelas do PDF com parâmetros otimizados
print("Extraindo dados do PDF...")
tabelas = tabula.read_pdf(
    "Anexo I.pdf",
    pages='all',
    multiple_tables=True,
    guess=False,
    lattice=True,
    pandas_options={'header': 0}
)

# Concatenar todas as tabelas em um único DataFrame
df_final = pd.concat(tabelas, ignore_index=True)

# Substituir NaN por strings vazias imediatamente após a concatenação
df_final = df_final.fillna('')

# Limpar e padronizar os dados
print("Processando dados...")
# Converter todas as colunas para string e limpar espaços
for coluna in df_final.columns:
    df_final[coluna] = df_final[coluna].astype(str).str.strip()

# Manter linhas duplicadas, pois as informações repetidas no PDF devem ser preservadas no CSV para garantir a integridade dos dados.
# Portanto, não removeremos duplicatas neste caso.
# df_final = df_final.drop_duplicates()  # Esta linha foi comentada para manter as duplicatas.

# Substituir as abreviações pelas descrições completas
print("Substituindo abreviações...")
if 'OD' in df_final.columns:
    df_final['OD'] = df_final['OD'].replace({
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    })

if 'AMB' in df_final.columns:
    df_final['AMB'] = df_final['AMB'].replace({
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    })

# Salvar em CSV com formatação adequada
print("Salvando arquivo CSV...")
csv_filename = "Rol_Procedimentos.csv"
df_final.to_csv(csv_filename, 
                index=False, 
                encoding='utf-8-sig',  # Adiciona BOM para melhor compatibilidade com Excel
                sep=';',  # Usar ponto e vírgula como separador
                quoting=1)  # Usar aspas para todos os campos

# Criar arquivo ZIP
print("Criando arquivo ZIP...")
zip_filename = "Teste_Augusto.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_filename)

# Remover arquivo CSV temporário
#os.remove(csv_filename)

print("Processo concluído com sucesso!")
print(f"Arquivo ZIP criado: {zip_filename}")

# Exibir as primeiras linhas do DataFrame para verificação
print("\nPrimeiras linhas do DataFrame:")
print(df_final.head())