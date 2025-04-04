import tabula # Precisa ter o java instalado no seu computador
import pandas as pd
import zipfile
import os

# Extrair os dados do PDF

def extrair_tabelas_pdf(caminho_pdf):
    '''Função pra extrair tabelas de um PDF utilizando Tabula'''

    print("Iniciando a extração das tabelas do PDF...")

    try:
        tabelas = tabula.read_pdf(caminho_pdf,pages='all',multiple_tables=True,guess=False,lattice=True,pandas_options={'header': 0})
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

def salvar_csv(df, nome_arquivo, pasta_destino):
    '''Função para salvar o DataFrame como CSV na pasta especificada'''
    print(f"Salvandos os dados no arquivo {nome_arquivo} na pasta {pasta_destino}...")
    try:
        # Criar a pasta de destino se não existir
        os.makedirs(pasta_destino, exist_ok=True)
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        df.to_csv(caminho_completo, index=False, encoding='utf-8-sig', sep=';', quoting=1)
        print(f"Arquivo {nome_arquivo} salvo com sucesso em {caminho_completo}.")
        return caminho_completo
    except Exception as e:
        print("Erro ao salvar o arquivo CSV:", e)
        return None


def criar_aquivo_zip(nome_csv, pasta_destino):
    nome_zip = "Teste{Augusto_Cezar_Araujo_Saboia}.zip"
    caminho_zip = os.path.join(pasta_destino, nome_zip)

    try:
        with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(nome_csv, os.path.basename(nome_csv)) # Adiciona o arquivo ao zip mantendo o nome base
            print(f"📂 Arquivo ZIP criado: {caminho_zip}")
            return caminho_zip
    except Exception as e:
        print("❌ Erro ao criar ZIP: ", e)
        return None


def main(caminho_pdf, nome_csv, pasta_destino):
    '''Função principal que chama todas as outras funções'''

    print("=== Iniciando o processo... ===")

    tabelas = extrair_tabelas_pdf(caminho_pdf)

    if not tabelas:
        print("Nenhuma tabela extraída. Processo Encerrado.")
        return


    df_final = pd.concat(tabelas, ignore_index=True).fillna('')

    df_final = processar_dados(df_final)

    caminho_csv_salvo = salvar_csv(df_final, nome_csv, pasta_destino)
    if caminho_csv_salvo:
        criar_aquivo_zip(caminho_csv_salvo, pasta_destino)

        # Remover arquivo csv
        #try:
        #    os.remove(caminho_csv_salvo)
        #    print(f"Arquivo temporário {caminho_csv_salvo} removido com sucesso.")
        #except Exception as e:
        #    print(f"Erro ao remover o arquivo temporário {caminho_csv_salvo}", e)
#

if __name__ == "__main__":
    caminho_pdf = "WebScraping(Teste01)/Anexo I.pdf"
    nome_csv = "Rol_Procedimentos.csv"
    pasta_destino = "Transformacao_dados(Teste02)"
    main(caminho_pdf, nome_csv,pasta_destino)