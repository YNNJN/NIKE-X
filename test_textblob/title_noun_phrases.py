import csv
import nltk_test
from textblob import TextBlob


with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    title_noun_phrases = []
    for info in reader:
        title = TextBlob(info[0]).lower()
        print(title)
        
#         title_noun_phrases.append(title.noun_phrases)
    
# with open('title_noun_phrases.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for noun in title_noun_phrases:
#         writer.writerow([noun])



