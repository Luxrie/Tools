from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse

links_intern = set()
input_url = input('DIGITE A URL: ')
nome_arquivo = input('DIGITE O NOME DO ARQUIVO TXT: ')
depth = 100

links_extern = set()

def level_crawler(input_url):
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc
            
    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml")

    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse (href)
            is_valid = bool(final_parsed_href.scheme) and bool(
                final_parsed_href.netloc)
            if is_valid:
                if current_url_domain not in href and href not in links_extern:
                    print("Externo - {}".format(href))
                    links_extern.add(href)
                if current_url_domain in href and href not in links_intern:
                    print("Interno - {}".format(href))
                    links_intern.add(href)
                    temp_urls.add(href)
    return temp_urls


if(depth == 0):
    print("Interno - {}".format(input_url))

elif(depth == 1):
    try:
        level_crawler(input_url)
    except:
        pass

else:

    queue = []
    queue.append(input_url)
    with open(nome_arquivo, 'w') as fp:
        for j in range(depth):
            for count in range(len(queue)):
                url = queue.pop(0)
                urls = level_crawler(url)
                for i in urls:
                    queue.append(i)
                    fp.write(i + '\n')
                    fp.flush()
                    
#Saul
