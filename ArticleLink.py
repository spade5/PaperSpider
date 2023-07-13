import requests
from bs4 import BeautifulSoup

def getDBLP(soup):
    list = soup.find_all('li', class_='inproceedings')
    for item in list:
        link = item.find('nav', class_='publ').find('a')['href']
        yield link

def getArticleLinks(url):
    response = requests.get(url, verify = False)
    soup = BeautifulSoup(response.text, 'html.parser')
    if 'dblp' in url:
        return getDBLP(soup)