import requests
from bs4 import BeautifulSoup
import zipfile
from datetime import datetime
import os
class SiteReferido:
    def __init__(self):
        self.url_do_site = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
        self.navegador = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        self.pasta_destino = "WebScraping(Teste01)"
    # Etapa 1.1 Acesso ao site
    def acessar_site(self):
        # Acessar o site e retornar o conteúdo em HTML usando BeautifulSoup
        try:
            resposta = requests.get(self.url_do_site, headers=self.navegador)
            resposta.raise_for_status()  # Verifica se houve erro no request
            return BeautifulSoup(resposta.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Erro ao acessar o site: {e}")
            return None
    # Etapa 1.2 Download dos Anexos I e II em formato PDF
    def encontrar_pdfs (self, soup):
        # Encontrar arquivos PDF
        lista_pdfs = [] # Lista para armazenar os PDFs
        for link in soup.find_all('a', href=True): # Percorrer por todos os link da página
            href = link['href']
            if href.lower().endswith('.pdf'): # Filtrar apenas link que terminam em .pdf
                if 'anexo i' in link.text.lower() or 'anexo ii' in link.text.lower():
                    lista_pdfs.append({
                        'url': href,
                        'nome': link.text.strip() + "pdf"
                    })
        return lista_pdfs
    def baixar_pdf(self, url, nome):
        # Baixar pdfs
        print(f"Salvando o {nome} na pasta {self.pasta_destino}...")
        try:
            # Criando a pasta de destino caso ela não exista
            os.makedirs(self.pasta_destino, exist_ok=True)
            caminho_completo = os.path.join(self.pasta_destino, nome)
            resposta = requests.get(url, headers=self.navegador)
            resposta.raise_for_status()
            # Criar o arquivo
            with open(caminho_completo, 'wb') as arquivo:
                arquivo.write(resposta.content)
            print(f"PDF {nome} baixado com sucesso em {caminho_completo}")
            return caminho_completo
        except Exception as e:
            print(f"Erro ao baixar o PDF: {nome}: {e}")
            return False
        
    # Etapa 1.3 Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.).
    def compactar_pdfs(self, arquivos):
            # Criar o nome do arquivo com log de datetime
            nome_zip = f"Anexos_ANS.zip"
            caminho_zip = os.path.join(self.pasta_destino, nome_zip)
    
            try:
                with zipfile.ZipFile(caminho_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for nome_arquivo in arquivos:
                        caminho_completo = os.path.join(self.pasta_destino, nome_arquivo)
                        if os.path.exists(caminho_completo):
                            zipf.write(caminho_completo, nome_arquivo)
                        else:
                            print(f"⚠️ Arquivo não encontrado: {caminho_completo}")
                print(f"📂 Arquivo ZIP criado: {caminho_zip}")
                return nome_zip
            except Exception as e:
                print(f"❌ Erro ao criar ZIP: {e}")
# Testes isolados.

def testar_compactacao():
    # Cria arquivos PDF de exemplo para teste (não arquivos reais, só exemplos de nomes)
    arquivos_teste = ["anexo1.pdf", "anexo2.pdf", "anexo3.pdf"]
    
    # Criar arquivos vazios para simular PDFs
    for arquivo in arquivos_teste:
        with open(arquivo, 'w') as f:
            f.write("Simulação de conteúdo de PDF.")
    
    # Instancia a classe onde a função compactar_pdfs está definida
    site = SiteReferido()

    # Chama a função de compactação
    nome_zip = site.compactar_pdfs(arquivos_teste)

    # Verifica se o arquivo ZIP foi criado corretamente
    if nome_zip:
        print(f"Arquivo ZIP criado com sucesso: {nome_zip}")
        
        # Verifica se o arquivo ZIP realmente foi criado
        if os.path.exists(nome_zip):
            print(f"O arquivo ZIP {nome_zip} existe.")
        else:
            print("O arquivo ZIP não foi criado corretamente.")
    else:
        print("Falha ao criar o arquivo ZIP.")

def testar_download():
    site = SiteReferido()
    soup = site.acessar_site()

    if soup:
        pdfs = site.encontrar_pdfs(soup)
        if not pdfs:
            print("Nenhum PDF encontrado no site.")
        for pdf in pdfs:
            site.baixar_pdf(pdf['url'], pdf['nome'] + ".pdf")

def testar_encontrar_pdfs():
    site = SiteReferido()
    soup = site.acessar_site()

    if soup:
        pdfs = site.encontrar_pdfs(soup)
        print(f"PDFs encontrados: {len(pdfs)}")
        for pdf in pdfs:
            print(f"- {pdf['nome']} : {pdf['url']}")
    else:
        print("Falha no acesso ao site")

def testar_acesso():
    site = SiteReferido()
    soup = site.acessar_site()
    if soup:
        print("Acesso ao site OK!")
        print(soup.title.text if soup.title else "Sem título")
    else:
        print("Falha no acesso ao site")
def main():
    try:
        # 1.1 Acessar o site
        site = SiteReferido()
        soup = site.acessar_site()

        if not soup:
            print("Não foi possível acessar o site.")
            return
        
        print("Site acessado com sucesso!")

        # 1.2 Download dos Anexos I e II em formato PDF

        pdfs = site.encontrar_pdfs(soup)
        if not pdfs:
            print("Nenhum PDF encontrado.")
            return
        
        print(f"Encontrados {len(pdfs)} PDFs.")

        arquivos_baixados = []

        for pdf in pdfs:
            if site.baixar_pdf(pdf['url'], pdf['nome']):
                arquivos_baixados.append(pdf['nome'])

        
        # 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.).

        if arquivos_baixados:
            site.compactar_pdfs(arquivos_baixados)
    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
