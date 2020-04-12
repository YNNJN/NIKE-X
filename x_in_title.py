import csv
import nltk
import re
from textblob import TextBlob


with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    collabos = []
    for info in reader:
        title = info[0]
        if title.find(' ' + 'x' + ' ') >= 0:
            collabos.append(title)

    for i in range(len(collabos)):
        collabos[i] = collabos[i].replace(' x ', 'x')
        
    collabo_noun_phrases = []
    for collabo in collabos:
        collabo = TextBlob(collabo)
        collabo_noun_phrases.append(collabo.noun_phrases)

    # print(collabo_noun_phrases)
    
with open('x_in_title.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for noun in collabo_noun_phrases:
        writer.writerow([noun])



