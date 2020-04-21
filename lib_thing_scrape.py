from bs4 import BeautifulSoup
import requests
import json
import time
import sys
import webbrowser
from selenium import webdriver

chrome_driver = r'C:\Users\Stephen Hayden\Downloads\chromedriver'

DRIVER = webdriver.Chrome(chrome_driver)


def get_catalog_pages():
    '''collects catalog pages from Librarything'''
    links_list = []
    count = 0
    while  count < 7770:
        url = f'https://www.librarything.com/catalog_bottom.php?view=UMPhilosophy&offset={count}'
        links_list.append(url)
        count +=50
    return links_list

def get_item_from_catalog(url):
    '''scrapes LibraryThing for item/attributes

    '''
    item_list = []
    item_dict = {}
    links_list = []
    new_list = []
    #lt-title //holds the title link from catalog tree table
    DRIVER.get(url)
    response = DRIVER.page_source
    soup = BeautifulSoup(response, 'html.parser')
    #print(soup)
    items_links = soup.find_all(class_="lt-title") #/work/21233730/book/177701030
    #print(item_links)
    links_list = []
    #for url in items_links:
        #links_list.append(book_link = 'https://www.librarything.com/'+url.a.get('href'))
    for url in items_links:
        book_link = 'https://www.librarything.com/'+(url.attrs['href'])
        new_list.append(book_link)

    #links list now has all of the links from one page
    #print(len(links_list))
    #print(items_links)
    return new_list

def create_url_dict(url_list):
    d = {}
    count = 1
    for url in url_list:
        d[str(count)] = url
        count +=1
    return d

if __name__ == "__main__":
    item_links = []
    url_list = get_catalog_pages()
    url_dict = create_url_dict(url_list)
    count = 1
    #for url in url_dict:
        #c_url = url_dict[str(count)]
        #item_links.extend(get_item_from_catalog(c_url))
        #print(get_item_from_catalog(c_url))
        #time.sleep(2)
        #count +=1
    #for url in url_list:
        #print(url)
    #for url in url_list:
       # item_links.extend(get_item_from_catalog(url))
       # print(len(item_links))
        #time.sleep(2)
    #print(item_links)

    f = open("catalog_page_urls.txt", "w")
    for url in url_list:
        catalog_page = get_item_from_catalog(url)
        item_links.append(catalog_page)
        print(len(item_links))
        #f.write(catalog_page)
        for item in catalog_page:
            f.write(item+",")
        time.sleep(2)
    f.close()

    #### 3/27/20 We apparently need Selenium to scrape through each page iteratively, which will be neat