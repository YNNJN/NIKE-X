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

        contents = data.find_all('p', class_='text--p')
        for content in contents:
            for child in content.descendants:
                if child is None:
                    contents_list.append(child)
                else:
                    contents_list.append(child)
        contents_list.append('.........................................................')

with open('body_contents.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for content in contents_list:
        writer.writerow([content])
