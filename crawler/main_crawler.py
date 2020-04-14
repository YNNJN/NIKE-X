import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv


article_dict = {}
article_list = []
idx = 0
for page in range(1, 11):
    url = 'https://news.nike.com/collaborations/page/' + str(page)

    response = requests.get(url)
    response = response.text
    data = BeautifulSoup(response, 'html.parser')

    title = data.select('h2.feature-tile__headline')
    content = data.select('p.feature-tile__copy')
    date = data.select('span.font--italic')
    data = data.find('div', {'class':"col-md-10"})
    contents = data.find_all('div', {"class":"col-md-6 feature-tile__content"})

    for i in range(len(title)):
        result_title = title[i].text
        result_content = content[i].text
        result_date = date[i].text
        idx += 1

        a_tag_str = contents[i].find_all('a')[1].__repr__()
        idx_start = 8
        idx_end = a_tag_str[9:].index('"')
        body_url = a_tag_str[9:idx_end+9]

        article_dict = {'idx': idx, 'title': result_title, 'content': result_content, 'date': result_date, 'body_url': body_url}
        article_list.append(article_dict)

    with open('articles.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ('idx', 'title', 'content', 'date', 'body_url')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in article_list:
            writer.writerow(article)


print(article_list)