from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

item_links = []
with open("work_details_urls.txt", 'r') as f:
    for line in f:
        striped_line = line.strip()
        item_links.extend(striped_line)
print(len(item_links))