import requests
print(type(requests))
print(dir(requests))
from bs4 import BeautifulSoup
response = requests.get('https://venolearn.com')
print(response)
print(response.status_code)
print(response.encoding)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(response.content)
print(response.headers)
print("*****************************************")
print(response.cookies)
print("_________________________________________")
soup = BeautifulSoup(response.text, "lxml")
title = soup.title
print(title)
print("_________________________________________")
print(soup.find_all("img"))
print("__________________________________________")
for link in soup.find_all('img',src=True):
    if link['src'].startswith('http'):
        print(link['src'])
print("__________________________________________")
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))






