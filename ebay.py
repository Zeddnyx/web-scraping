import requests as req
from bs4 import BeautifulSoup as bs
import csv


key = 'camera'
url = 'https://www.ebay.com/sch/i.html?_nkw={}&_sacat=0&_pgn='.format(key)
resp = req.get(url)
sup = bs(resp.text,'html.parser')

data = []
pg = 0

for page in range(1,16):
	pg += 1
	print('Scrap page',pg)
	item = sup.find_all('li','s-item')
	for i in item:
		name = i.find('h3','s-item__title').text
		price = i.find('div','s-item__detail').text
		img = i.find('img','s-item__image-img')['src']
		data.append( [name,price,img])

head = ('Nama brand','Harga','Img brand')
w = csv.writer(open('/storage/emulated/0/result.csv','w',newline=''))
w.writerow(head)
for i in data:
	w.writerow(i)

print('Success!')
