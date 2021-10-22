import requests as req
from bs4 import BeautifulSoup as bs
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def soup_recover(url):
    request = req.get(url)
    return bs(request.text,features="html.parser")

def urls_extract(soup):
    
    urls = []
    for article in soup.find_all('article'):
        url = article.find_all('a',limit=1)[0]
        urls.append('https://books.toscrape.com/catalogue/' + url['href'])

    return urls

def extract_data(soup):

    data_book = []

    for page in soup.select('.page'):

        book_information = page.find_all('td')


        title = page.find_all('h1')[0].text
        price = page.find_all('p')[0].text
        stock = book_information[5].text
        category = page.find_all('li')[2].text.split('\n')[1]
        cover = 'https://books.toscrape.com/' + page.find_all('img')[0]['src'].split('../')[2]
        upc = book_information[0].text
        product_type = book_information[1].text
        price_excl_tax = book_information[2].text
        price_incl_tax = book_information[3].text
        tax = book_information[4].text
        number_reviews = book_information[6].text

        print(book_information)

        data_book.extend([title,price,stock,category,cover,upc,product_type,price_excl_tax,price_incl_tax,tax,stock,number_reviews])

    return data_book

def export_csv(data):
    contador = 0

    file = open('books_data.csv','w',encoding="utf-8")
    file.write('"title","price","stock","category","cover","upc","product type","price (excl. tax)","price (incl. tac)","tax","availability","number of reviews"\n')

    for book_data in data:
        info = ''
        for information in book_data:
            info += '"'+ information + '"' + ','
        file.write(str(contador+1)+ ',' + info + '\n')
        clearConsole()
        print(str(round(contador*0.1,1)) + '%')

        contador += 1

    file.close()

url_web = 'https://books.toscrape.com/'
urls_books = []
number_pages = 50

for page in range(number_pages):
    urls_books.extend(urls_extract(soup_recover(url_web + 'catalogue/page-' + str(page+1) + '.html')))
    clearConsole()
    print(str(round((page)*2,1)) + '%')


data_books = []

for index,url in enumerate(urls_books):
    data_books.append(extract_data(soup_recover(url)))
    # clearConsole()
    print(str(round(index*0.1,1)) + '%')

export_csv(data_books)
