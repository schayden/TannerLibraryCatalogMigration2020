from bs4 import BeautifulSoup
import requests

def get_catalog_pages():
    '''collects catalog pages from Librarything'''
    links_list = []
    count = 0
    while  count < 7770:
        url = f'https://www.librarything.com/catalog_bottom.php?view=UMPhilosophy&offset={count}'
        links_list.append(url)
        count +=50
    return links_list

def get_next_page_link(soup):
    anchors = soup.find_all('a', class_="pageShuttleButton")
    if anchors:
        for anchor in anchors:
            link = anchor['href']
       # <a class="pageShuttleButton" href="/catalog_bottom.php?view=UMPhilosophy&amp;offset=50">next page</a>
        url = "https://www.librarything.com"+link,"aaaaa"
        return url

def get_item_from_catalog(url):
    '''scrapes LibraryThing for item/attributes

    '''
    
    item_list = []
    item_dict = {}
    links_list = []
    new_list = []
    #lt-title //holds the title link from catalog tree table
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    #catalog_table = soup.find('table', id = "lt_catalog_list", class_="catalog")
    items_links = soup.findAll(class_="lt-title") #/work/21233730/book/177701030
    next_page = soup.find(class_='pageShuttleButton')
    links_list = []
    #for url in items_links:
        #links_list.append(book_link = 'https://www.librarything.com/'+url.a.get('href'))
    #<a class="pageShuttleButton" href="/catalog_bottom.php?view=UMPhilosophy&amp;offset=50">next page</a>
    for url in items_links:
        new_list.append(url.attrs['href'])


    #<a class="pageShuttleButton" href="/catalog_bottom.php?view=UMPhilosophy&amp;offset=50">next page</a>

def create_url_dict(url_list):
    d = {}
    count = 1
    for url in url_list:
        d[count] = url
        count +=1

url_list = get_catalog_pages()
item_links = []


url = 'https://www.librarything.com/catalog_bottom.php?view=UMPhilosophy&offset=0'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
items_links = soup.findAll(class_="lt-title")
#\print(item_links)