import csv
import nltk
import re
from textblob import TextBlob


with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    collabos = []
    for info in reader:
        content = info[1]
        if content.find(' ' + 'x' + ' ') >= 0:
            collabos.append(content)

    for i in range(len(collabos)):
        collabos[i] = collabos[i].replace(' x ', '-x-')
        
    collabo_noun_phrases = []
    for collabo in collabos:
        collabo = TextBlob(collabo)
        collabo_noun_phrases.append(collabo.noun_phrases)

    collabo_x = []
    for i in range(len(collabo_noun_phrases)):
        for j in range(len(collabo_noun_phrases[i])):
            if '-x-' in collabo_noun_phrases[i][j]:
                collabo_x.append(collabo_noun_phrases[i][j])

    for i in range(len(collabo_x)):
        collabo_x[i] = collabo_x[i].split('-x-')
    
with open('x_in_content.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for noun in collabo_x:
        writer.writerow(noun)



