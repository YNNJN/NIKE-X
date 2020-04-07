import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

article_dict = {}
article_list = []
for i in range(1, 11):
    url = 'https://news.nike.com/collaborations/page/' + str(i)

    response = requests.get(url)
    response = response.text
    data = BeautifulSoup(response, 'html.parser')

    title = data.select('h2.feature-tile__headline')
    content = data.select('p.feature-tile__copy')
    date = data.select('span.font--italic')
    
    for i in range(len(title)):
        result_title = title[i].text
        result_content = content[i].text
        result_date = date[i].text

        article_dict = {'title': result_title, 'content': result_content, 'date': result_date}
        article_list.append(article_dict)

    with open('articles.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ('title', 'content', 'date')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in article_list:
            writer.writerow(article)


print(article_list)