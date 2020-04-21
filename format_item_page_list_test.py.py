from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

catalog_page_links =  []
split_list = []
nlist = []
with open('catalog_page_urls.txt', 'r') as f:
    catalog_page_links.append(f.read())
#catalog_page_links.split(',')
for item in catalog_page_links:
    split_list.append(item.split(','))
one = str(split_list).split()
for item in one:
    nlist.append(item)
for item in nlist:
    item = item.replace(',',"")
    item+"\n"
del nlist[-1]
for item in nlist:

    f.write
    print(item)
with open("LibraryThing_Catalog_Urls.txt", 'w') as f:
    for item in nlist:
        f.write(item)
#print(len(nlist))