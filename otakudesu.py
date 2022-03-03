# Zeddnyx
# usr/python3


import requests
from bs4 import BeautifulSoup
import csv

#this for search genre
gen = 'harem'
url = 'https://otakudesu.pro/genres/{}/page//'.format(gen)
data = []
pages = 0

#to scrap page 1-7
for page in range(1,7):
	pages+=1
	print('Scrap page',pages,'key:',gen)
	req = requests.get(url+str(page))
	soup = BeautifulSoup(req.text,'html.parser')
	tag = soup.find_all('div','col-anime')

	for cari in tag:
		judul = cari.find('div','col-anime-title').text
		rate = cari.find('div','col-anime-rating').text
		genre = cari.find('div','col-anime-genre').text
		rilis = cari.find('div','col-anime-date').text
		eps = cari.find('div','col-anime-eps').text
		synopsis = cari.find('div','col-synopsis').text
		data.append([judul,rate,genre,eps,rilis,synopsis])

#to write into csv file!
head = ('Judul','Rate','Genre','Eps','Rilis','Synopsis')
writer = csv.writer(open('/storage/emulated/0/result.csv','w',newline=''))
writer.writerow(head)
for kntl in data:
	writer.writerow(kntl)

print('Scraping succes!!!')
