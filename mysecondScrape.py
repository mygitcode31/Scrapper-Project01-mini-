# go to git bash
# git config --global user.name "Naresh Prasad Yadav"
# git config --global user.email "npy.personal@gmail.com"


# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git add .
# git commit -m "Comment"
# copy paste git code from github


# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

####################################################
# 1. change the code 
# 2. git add .
# 3. git commit -m "Comment"
# 4. git push
####################################################


import requests
import json
import csv
from bs4 import BeautifulSoup 

# URL of the website to scrape
url = "http://books.toscrape.com/"




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

def scrape_books(url):
   response = requests.get(url)
   if response.status_code != 200:
        return       # come out from function
   response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly
   
   all_books = []
   
   soup = BeautifulSoup(response.text,"html.parser")
   books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
   for book in books: 
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text 
        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  # here the price is separated from its symbol
        
        all_books.append(
            {
                "title": title,
                "currency":currency,
                "price":price,
            }
        )
   return all_books

scrape_books(url) 

#getting list dict data

def scrape_books(url):
   response = requests.get(url)
   if response.status_code != 200:
        return []      # come out from function
   response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly
   
   all_books = []
   
   soup = BeautifulSoup(response.text,"html.parser")
   books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
   for book in books: 
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text 
        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  # here the price is separated from its symbol
        
        all_books.append(
            {
                "title": title,
                "currency":currency,
                "price":price,
            }
        )
   return all_books

books = scrape_books(url) 
# print(books)

with open("books.json", 'w', encoding="utf-8") as f:
    

    json.dump(books, f, indent = 4, ensure_ascii=False)


# convert into CSV file...
def scrape_books(url):
   response = requests.get(url)
   if response.status_code != 200:
        return []      # come out from function
   response.encoding = response.apparent_encoding  # set encoding explicitily to handle special characters correctly
   
   all_books = []
   
   soup = BeautifulSoup(response.text,"html.parser")
   books = soup.find_all('article', class_= 'product_pod')  # all articles we can get 
   for book in books: 
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text 
        currency = price_text[0]
        price = float(price_text[1:])

        print(title, currency, price)  # here the price is separated from its symbol
        
        all_books.append(
            {
                "title": title,
                "currency":currency,
                "price":price,
            }
        )
   return all_books

books = scrape_books(url) 
# print(books)

with open("books.json", 'w', encoding="utf-8") as f:
    import json
    
    json.dump(books, f, indent = 4, ensure_ascii=False)
    
with open("books.csv", "w", encoding = "utf-8", newline="") as f:

    
    writer = csv.DictWriter(f, fieldnames={"title", "currency", "price"})
    writer.writeheader()
    writer.writerows(books)

print("CSV file created: books.csv")
