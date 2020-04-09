import csv

with open('data/body_url.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for link in reader:
        link = ''.join(map(str, link))
        url = 'https://news.nike.com' + link
        print(url)
