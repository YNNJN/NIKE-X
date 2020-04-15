import requests
from bs4 import BeautifulSoup
import csv

contents_list = []
with open('data/body_url.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for link in reader:
        link = ''.join(map(str, link))
        url = 'https://news.nike.com' + link

        response = requests.get(url)
        response = response.text
        data = BeautifulSoup(response, 'html.parser')
        
        #idx = 0
        contents_dict = {}
        contents = data.find_all('p', class_='text--p')
        if contents:
            tmp = ''
            for content in contents:
                content = content.get_text()
                tmp += content
            #idx += 1
            tmp = tmp.replace('\xa0', '')
            contents_list.append(tmp)
        else:
            tmp = ''
            contents = data.find_all('p')
            for content in contents:
                content = content.get_text()
                tmp += content
            #idx += 1
            tmp = tmp.replace('\xa0', '')
            contents_list.append(tmp)

with open('body_contents.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for content in contents_list:
        writer.writerow([content])
