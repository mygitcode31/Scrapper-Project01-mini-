# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

import requests
from bs4 import BeautifulSoup 

# URL of the website to scrape
url = "http://books.toscrape.com/"

# web scrapping => websites baat data tannu

def scrape_books(url):
    response = requests.get(url)
    print(response)

scrape_books(url)    # in the fuction we have to call

# get means to see the data 
# post means to send the data 

def scrape_books(url):
    response = requests.get(url)
    print(response.status_code)

scrape_books(url) 


def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    print(response.text)  # html data aauxa

scrape_books(url) 

# use BeautifulSoup4
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    
    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
    print(books)  # we can get data in list

scrape_books(url) 


# special symbol like $ pound cannot decode by python so, we can make it easy for python
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    
    response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly

    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
    print(books)  # we can get data in list

scrape_books(url) 



# in html Tags and Attributes (properties)
# for ex: </p>, </a> 
# for ex: href 

# take out title 
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    
    response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly

    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
    for book in books: 
        title = book.h3.a['title']
        print(title)
        
scrape_books(url) 

# take out title and price together
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    
    response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly

    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
    for book in books: 
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text 
        print(title, price_text)  # here the price_text type is str
        
scrape_books(url) 

# take out title currency and price in separation (tasera hoena)
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return       # come out from function
    
    response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly

    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
    for book in books: 
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text 
        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  # here the price is separated from its symbol
        
scrape_books(url) 

# homework is to convert this code in json file