from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

catalog_page_links =  []
split_list = []
nlist = []
return_list = []
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
count = 0
#for item in nlist:

 #   f.write
    #print(item)
#with open("LibraryThing_Catalog_Urls.txt", 'w') as f:
 #   for item in nlist:
  #      f.write(item)
#print(len(nlist))
for url in nlist:
    s_url = url.strip().replace(',',"").replace("'","").replace('[',"")
    response = requests.get(s_url).text
    soup = BeautifulSoup(response, "html.parser")
    a = soup.find(class_='leftnav workleftnav alwaysblue noline')
    b = a.findAll('li')
    c = b[2]
    anchors = c.find('a')
    link = 'https://librarything.com'+anchors['href']
    return_list.append(link)
    count +=1
    print(link,count)
    time.sleep(2)
with open ("work_details_urls.txt", 'w') as f:
    for url in return_list:
        f.write(url)
#print(link)
#url = nlist[1].strip().replace(',',"").replace("'","").replace('[',"")
#print(url)
#for url in nlist[1]:
    #print(url)
#response = requests.get(url).text
#soup = BeautifulSoup(response, "html.parser")
#a = soup.find(class_='leftnav workleftnav alwaysblue noline')
#b = a.findAll('li')
#c = b[2]
#anchors = c.find('a')
#link = 'https://librarything.com/'+anchors['href']
#print(link)