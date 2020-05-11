import pandas as pd

article = pd.read_csv('ETL/x_in_article.csv')
body = pd.read_csv('ETL/x_in_body.csv')
x_in = pd.merge(article, body, how='left') #left outer join

x_in.to_csv('x_in_all.csv')