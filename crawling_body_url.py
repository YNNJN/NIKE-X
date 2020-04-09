import requests
from bs4 import BeautifulSoup
import csv


a_href = []
for i in range(1, 11):
    url = 'https://news.nike.com/collaborations/page/' + str(i)

    response = requests.get(url)
    response = response.text
    data = BeautifulSoup(response, 'html.parser')

    data = data.find('div', {'class':"col-md-10"})
    contents = data.find_all('div', {"class":"col-md-6 feature-tile__content"})

    for content in contents :
        a_tag_str = content.find_all('a')[1].__repr__()
        idx_start = 8
        idx_end = a_tag_str[9:].index('"')
        a_href.append([a_tag_str[9:idx_end+9]])

with open('body_url.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(a_href)
    


