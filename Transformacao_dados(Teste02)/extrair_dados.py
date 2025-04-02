import tabula # Precisa ter o java instalado no seu computador
import pandas as pd
import zipfile
import os

# Extrair os dados do PDF

def extrair_tabelas_pdf(caminho_pdf):
    '''Função pra extrair tabelas de um PDF utilizando Tabula'''

    print("Iniciando a extração das tabelas do PDF...")

    try:
        tabelas = tabula.read_pdf(
            caminho_pdf,
            pages='all',
            multiple_tables=True,
            guess=False,
            lattice=True,
            pandas_options={'header': 0}
        )
        print("Tabelas extraídas com sucesso.")
        return tabelas
    except Exception as e:
        print("Erro ao extrair as tabelas:", e)
        return []
    

def processar_dados(df):
    '''Essa função tem objetivo de limpar as informações vazias das tabelas'''
    print("Processando os dados extraídos...")

    try:
        df = df.applymap(lambda x:str(x).strip()) # Percorre cada elemtno do DataFrame, converte para string e remove os espaços.
        substituicoes = {
            'OD': 'Seg. Odontológica',
            'AMB': 'Seg. Ambulatorial'
        }

        df.replace(substituicoes, inplace=True)
        print("Dados processados com sucesso.")
        return df
    except Exception as e:
        print("Erro ao processar os dados.", e)
        return df

def salvar_csv(df, nome_arquivo):
    '''Função para salvar o DataFrame como CSV'''
    print(f"Salvandos os dados no arquivo {nome_arquivo}...")
    try:
        df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig', sep=';', quoting=1)
        print(f"Arquivo {nome_arquivo} salvo com sucesso.")
        return(nome_arquivo)
    except Exception as e:
        print("Erro ao salvar o arquivo CSV:", e)


def criar_aquivo_zip(nome_csv):
    nome_zip = "Teste{Augusto_Cezar_Araujo_Saboia}.zip"

    try:
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(nome_csv)
            print(f"📂 Arquivo ZIP criado: {nome_zip}")
            return nome_zip
    except Exception as e:
        print("❌ Erro ao criar ZIP: ", e)


def principal(caminho_pdf, nome_csv):
    '''Função principal que chama todas as outras funções'''

    print("=== Iniciando o processo... ===")

    tabelas = extrair_tabelas_pdf(caminho_pdf)

    if not tabelas:
        print("Nenhuma tabela extraída. Processo Encerrado.")
        return
    

    df_final = pd.concat(tabelas, ignore_index=True).fillna('')

    df_final = processar_dados(df_final)

    salvar_csv(df_final, nome_csv)
    criar_aquivo_zip(nome_csv)

    # Remover arquivo csv
    try:
        os.remove(nome_csv)
        print(f"Arquivo temporário {nome_csv} removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover o arquivo temporário {nome_csv}", e)


if __name__ == "__main__":
    caminho_pdf = "Anexo I.pdf"
    nome_csv = "Rol_Procedimentos.csv"
    principal(caminho_pdf, nome_csv)