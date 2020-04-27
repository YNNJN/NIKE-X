import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.vogue.com/fashion-shows'
response = requests.get(url)
response = response.text
data = BeautifulSoup(response, 'html.parser')

name_list = data.find_all('li', {"class":"tab-list--item tab-list--item__brand"})
brand_name_list=[]
for i in range(len(name_list)):
    name = name_list[i].find_all('a')[0].__repr__()
    idx_end = name[9:].index('"')
    brand_name = name[69:idx_end+9]
    brand_name = brand_name.replace('-', ' ')
    brand_name_list.append(brand_name)
#print(brand_name_list)
#print(len(brand_name_list)) => 418

with open('vogue_brand.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([brand_name_list])
