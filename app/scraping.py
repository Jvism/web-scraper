import requests as req
from bs4 import BeautifulSoup as bs

def soup_recover(url):
    request = req.get(url)
    return bs(request.text,features="html.parser")

def urls_extract(soup):
    
    urls = []
    for article in soup.find_all('article'):
        for url in article.find_all('a',limit=1):
            urls.append('https://books.toscrape.com/catalogue/' + url['href'])

    return urls

def extract_data(soup):

    data_book = []
    for article in soup.find_all('article'):
        for url in article.find_all('a',limit=1):
            urls.append('https://books.toscrape.com/catalogue/' + url['href'])

    return data_book

url_web = 'https://books.toscrape.com/'
urls_books = []
number_pages = 50

for page in range(number_pages):
    urls_books.extend(urls_extract(soup_recover(url_web + 'catalogue/page-' + str(page+1) + '.html')))

print (len(urls_books))