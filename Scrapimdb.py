import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36'
headers = {"user-agent": USER_AGENT}
req = requests.get(url, headers=headers)

sup = BeautifulSoup(req.text, "html.parser")
tag = sup.find_all('div','lister-item-content')

for cari in tag:
	judul = ''.join(cari.find('h3','lister-item-header').text.strip().split('\n'))
	genre = cari.find('span','genre').text

print(judul,genre)

