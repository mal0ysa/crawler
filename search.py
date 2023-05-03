from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Qual página você gostaria de buscar?")
keyword = input ("Qual palavra chave você gostaria de buscar?")

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
data = BeautifulSoup(html, "html.parser")

def  search_in_title(keyword, data):
    if keyword.casefold() in data.title.text.casefold():
        status = "encontrado"
    else:
        status = "não encontrado"
    return status
print(search_in_title(keyword, data))