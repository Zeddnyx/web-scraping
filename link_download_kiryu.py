import requests as req
from bs4 import BeautifulSoup
import csv

url = 'https://kiryuu.id/manga/tensai-ouji-no-akaji-kokka-saisei-jutsu-sou-da-baikoku-shiyou/'
resp = req.get(url)
sup = BeautifulSoup(resp.text,'html.parser')

# this for show all link the url have

#tag = sup.find_all('a',href=True)
#links = []
#for i in tag:
#	links.append(i['href'])
#for i in links:
#	print(i)

data = []
tag = sup.find_all('ul','clstyle')
for i in tag:
	taglink = i.findAll('div','dt')
	for i in taglink:
		tag3 = i.find('a')
		link = tag3['href'] # untuk mengolah data yg mau di ambil jika tidak memakai href makan data yg di tampilkan akan banyak
		data.append([link])

head = ('link')
writer = csv.writer(open('/storage/emulated/0/result.csv','w',newline=''))
writer.writerow(head)
for kntl in data:
	writer.writerow(kntl)

print('Scraping succes!!!')

