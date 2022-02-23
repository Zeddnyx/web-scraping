# Zeddnyx
# usr/python3
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://otakudesu.pro/genres/romance/page//'
page = int(input('how page do you want to scrap? :'))
data = []
pages = 0

for page in range(1,31):
	pages+=1
	print('Scrap page',pages)
	req = requests.get(url+str(page))
	soup = BeautifulSoup(req.text,'html.parser')
	tag = soup.find_all('div','col-anime')

	for cari in tag:
		judul = cari.find('div','col-anime-title').text
		rate = cari.find('div','col-anime-rating').text
		genre = cari.find('div','col-anime-genre').text
		rilis = cari.find('div','col-anime-date').text
		eps = cari.find('div','col-anime-eps').text
		data.append([judul,rate,genre,eps,rilis])

head = ('judul','rate','genre','eps','rilis')
writer = csv.writer(open('/storage/emulated/0/result.csv','w',newline=''))
'''write new file result.csv in your file manager!!!'''
writer.writerow(head)
for kntl in data:
	writer.writerow(kntl)

print('Scraping succes!!!')
