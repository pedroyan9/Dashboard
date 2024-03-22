import requests 
from bs4 import BeautifulSoup

# URL do Climatempo
url = "https://ge.globo.com/futebol/times/sao-paulo/noticia/2023/09/24/lista-de-campeoes-da-copa-do-brasil-sao-paulo-conquista-seu-primeiro-titulo-veja-ranking.ghtml"

# Fazendo a requisicao para a URL 
response = requests.get(url)

# Verificando se a requisicao foi bem sucedida
if response.status_code == 200:
        # Parseando o conteudo com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

        # Agora voce pode usar o objeto 'soup' para encontrar 
        # elementos na página 
        # Por exemplo, para encontrar todos os parágrafos
        # Voce pode fazer:
    paragraphs = soup.find_all('p')


    for p in paragraphs:
        print(p.get_text())
else:
    print("Nao foi possível acessar a página .")    





