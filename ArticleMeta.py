import requests
from bs4 import BeautifulSoup

def getUsenixMeta(soup):
    title = soup.find('h1', id='page-title').text
    abstract = soup.find('div', class_='field-name-field-paper-description').text
    return (title, abstract)

def getACM(soup):
    title = soup.find('h1', class_='citation__title').text
    abstract = soup.find('div', class_='abstractSection').text
    # print('acm', title, abstract)
    return (title, abstract)

def getArticleMeta(link):
    response = requests.get(link, verify = False)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print('get meta', link)
    if 'usenix' in link:
        return getUsenixMeta(soup)
    meta = soup.find('meta', property='og:url')
    if meta and 'dl.acm' in meta['content']:
        return getACM(soup)
    return (None, None)