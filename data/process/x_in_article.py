import csv
import nltk
from textblob import TextBlob
from itertools import chain

def x_in(content_tmp):
    sucs = False
    col_list = ['','']
    if ' x ' in content_tmp:
        conx = content_tmp.replace(' x ', '-x-')
        for word in TextBlob(conx).noun_phrases:
            if '-x-' in word: # word := "a-x-b"
                col_list = word.split('-x-') # col_list의 원소는 [a,b]
                sucs = True
        
    return sucs, col_list[0], col_list[1]

rows = []
with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #header는 skip

    idx = 0
    for info in reader:
        title = info[1]
        content = info[2]
        idx += 1
        boo1, a1, b1 = x_in(title)
        boo2, a2, b2 = x_in(content)
        rows.append(str(idx)+','+a1+'-x-'+b1+','+a2+'-x-'+b2)
    #print(rows)

f = open('x_in.csv', 'w', encoding='utf-8')
for row in rows:
    f.write(row+'\n')
f.close()
