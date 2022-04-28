import requests
from bs4 import BeautifulSoup as bs
import os

key = input('[?] Search Image : ')
resp = requests.get('https://unsplash.com/s/photos/{}'.format(key))
soup = bs(resp.text,'html.parser')
item = soup.find_all('div','mef9R')
link =[]
num = 0

os.system('clear')
print('[*] Keyword :',key)
print('[!] Source : https://unsplash.com')
print('\n[Note] The result is a top high resolution\n')
for it in item:
	tag = it.find('a')
	links = tag['href']
	link.append(links)
	for i in link:
		num += 1
		print(num,i,'\n')
