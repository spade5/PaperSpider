import requests
from bs4 import BeautifulSoup

urls = {
    "osdi2020": "https://dblp.uni-trier.de/db/conf/osdi/osdi2021.html"
}

def getDBLP(soup):
    list = soup.find_all('li', class_='inproceedings')
    for item in list:
        link = item.find('nav', class_='publ').find('a').href
        yield link

def getLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if 'dblp' in url:
        return getDBLP(soup)

def readLink(link):
    pass

for key in urls:
    url = urls.get(key)
    count = 1
    with open(key + '.txt', 'w', encoding='utf-8') as f:
        links = getLinks(url)
        for link in links:
            title, content = readLink(link)
            f.write(str(count) + '. ' + title + '\n\n')
            f.write(content + '\n\n')
            count += 1





# url = 'https://dblp.uni-trier.de/db/conf/osdi/osdi2020.html'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# titles = soup.find_all('div', class_='data')

# with open('papers.txt', 'w', encoding='utf-8') as f:
#     for title in titles:
#         paper_title = title.find('span', class_='title').text
#         f.write(paper_title + '\n')
        
#         abstract = title.find('div', class_='abstract')
#         if abstract:
#             f.write(abstract.text.strip() + '\n\n')