from ArticleLink import getArticleLinks
from ArticleMeta import getArticleMeta
import os.path
import urllib3
import threading

urllib3.disable_warnings()

targetDir = './output/'

urls = {
    "osdi2018": "https://dblp.uni-trier.de/db/conf/osdi/osdi2018.html",
    "osdi2020": "https://dblp.uni-trier.de/db/conf/osdi/osdi2020.html",
    "osdi2021": "https://dblp.uni-trier.de/db/conf/osdi/osdi2021.html",
    "osdi2022": "https://dblp.uni-trier.de/db/conf/osdi/osdi2022.html",

    "sigcomm2018": 'https://dblp.uni-trier.de/db/conf/sigcomm/sigcomm2018.html',
    "sigcomm2019": 'https://dblp.uni-trier.de/db/conf/sigcomm/sigcomm2019.html',
    "sigcomm2020": 'https://dblp.uni-trier.de/db/conf/sigcomm/sigcomm2020.html',
    "sigcomm2021": 'https://dblp.uni-trier.de/db/conf/sigcomm/sigcomm2021.html',
    "sigcomm2022": 'https://dblp.uni-trier.de/db/conf/sigcomm/sigcomm2022.html',

    "sigmod2018": "https://dblp.uni-trier.de/db/conf/sigmod/sigmod2018.html",
    "sigmod2019": "https://dblp.uni-trier.de/db/conf/sigmod/sigmod2019.html",
    "sigmod2020": "https://dblp.uni-trier.de/db/conf/sigmod/sigmod2020.html",
    "sigmod2021": "https://dblp.uni-trier.de/db/conf/sigmod/sigmod2021.html",
    "sigmod2022": "https://dblp.uni-trier.de/db/conf/sigmod/sigmod2022.html",
}

def fetchPapers(key):
    file = targetDir + key + '.md'
    if os.path.exists(file):
        print(key, 'already done')
    else:
        print(key, 'started')
        count = 0
        url = urls.get(key)
        with open(targetDir + key + '.md', 'w', encoding='utf-8') as f:
            links = getArticleLinks(url)
            for link in links:
                title, content = getArticleMeta(link)
                if title:
                    count += 1
                    f.write('# ' + str(count) + '. ' + title + '\n\n')
                    f.write(content + '\n\n')
                    print(key, 'have finished', count)
        print(key, 'done with', count, 'articles')

if __name__ == "__main__":
    for key in urls:
        fetchPapers(key)
        # t = threading.Thread(target=fetchPapers, args=(key,))
        # t.start()





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