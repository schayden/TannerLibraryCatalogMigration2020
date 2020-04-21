from bs4 import BeautifulSoup
import requests
import time
import json

item_links = []
split_list = []
with open('work_details_urls.txt', 'r') as f:
    item_links.append(f.read())

for item in item_links:
    split_list.append(item.split("https://"))
#print(split_list)
one = str(split_list).split()
nlist = []
for item in one:
    nlist.append(f"https://{item}")
tlist = []
for item in nlist:
    item = item.replace(',',"").replace("'","").replace("[",'').replace("]",'')
    tlist.append(item)
del tlist[0]
#print(len(tlist))

url = 'https://www.librarything.com/work/8770023/details/179278209'
#url = tlist[0]
return_list = []
for url in tlist:
    item_dict = {}
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    title_a = soup.find(class_="bookeditfield", id = 'bookedit_title')
    title_b = title_a.find('b').text #good
    #print(title_b)
    item_dict['title'] = title_b
    
    author_a = soup.find(class_='bookeditfield', id= 'bookedit_authorunflip')
    if author_a == None:
        item_dict['author'] = "No author"
    else:
        try:
            author_b = author_a.find('a').text #good
            item_dict['author'] = author_b
        except:
            item_dict['author'] = "No Author"
            pass
    #print(author_b)
    
    
    o_authors_b = []
    o_authors_a = soup.findAll('div', class_='bookeditPerson')
    if o_authors_a == None:
        o_authors_a = 'No other authors'
        o_authors_b = []
    else:
        o_authors_a = soup.findAll('div', class_='bookeditPerson')
        count = 0
        for a in o_authors_a:
            item = a.find('span', id = f'bookedit_person-{str(count)}').text
            b = a.find('span').text
            c = str(b)+str(item)
            o_authors_b.append(c)
            count +=1
    if o_authors_b == []:
        item_dict['Other authors'] = 'No other authors'
    else:
        item_dict['Other authors'] = o_authors_b

    pub_date = soup.find(class_='bookeditfield', id='bookedit_date').text
    #print(pub_date)
    item_dict["Publication date"] = pub_date

    lcc = soup.find(class_="bookeditfield", id = 'bookedit_lccallnumber').text
    #print(lcc)
    item_dict["LCCN"] = lcc
    print(item_dict)
    return_list.append(item_dict)
    time.sleep(2)
# // return_list will contain all items
""""multiple_author_list = []
for item in return_list:
    if item['Other authors'] != 'No other authors':
        multiple_author_list.append(item)
no_call_number_list = []
for item in return_list:
    if item['LCCN'] == '':
        no_call_number_list.append(item)
#else:
with open ("full_item_list.json", "w") as f:
    json.dump(return_list, f)
with open ("multiple_author_list.json", "w") as f:
    json.dump(multiple_author_list, f)
with open ("no_call_number.json", 'w') as f:
    json.dump(no_call_number_list, f)
 #   o_authors_a = soup.findAll(soup.findAll('div', class_='bookeditPerson'))
#title = class_= 'bookeditfield', id= 'bookedit_title'
#other_authors = bookedit_roles"""