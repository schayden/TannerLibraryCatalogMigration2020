from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver = r'C:\Users\Stephen Hayden\Downloads\chromedriver'

browser = webdriver.Chrome(chrome_driver)

browser.get('https://www.librarything.com/catalog_bottom.php?view=UMPhilosophy&offset=0')

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.findAll(class_="lt-title"))


def get_item_from_catalog(url):
    item_list = []
    item_dict = {}
    links_list = []
    new_list = []
    #lt-title //holds the title link from catalog tree table
    catalog_url = url
    response = requests.get(catalog_url).text
    soup = BeautifulSoup(response, 'html.parser')
    #print(soup)
    items_links = soup.find_all(class_="lt-title") #/work/21233730/book/177701030
    print(item_links)
    links_list = []
    #for url in items_links:
        #links_list.append(book_link = 'https://www.librarything.com/'+url.a.get('href'))
    for url in items_links:
        new_list.append(url.attrs['href'])
    #links list now has all of the links from one page
    #print(len(links_list))
    #print(items_links)
    return new_list

