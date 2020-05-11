import csv
import nltk_test
from textblob import TextBlob


with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    content_noun_phrases = []
    for info in reader:
        content = TextBlob(info[1])
        content_noun_phrases.append(content.noun_phrases)
    
with open('content_noun_phrases.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for noun in content_noun_phrases:
        writer.writerow([noun])