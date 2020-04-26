import csv
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from googletrans import Translator

with open('data/body_contents.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    stop_words = set(stopwords.words('english'))
    stop_words.add(",")
    stop_words.add("‘")
    stop_words.add("’")
    stop_words.add('"')
    stop_words.add('“')
    stop_words.add('”')
    stop_words.add('|')
    stop_words.add('—')
    
    allnoun = []
    for contents in reader:
        for content in contents:
            translator = Translator()
            result = translator.translate(content, dest="en")
            #print(result.text)
            
            tokens=nltk.word_tokenize(result.text)
            #print(tokens)
            tagged_tokens=nltk.pos_tag(tokens)
            for word,pos in tagged_tokens:
                if word not in stop_words and pos in ['NN', 'NNP']:
                    allnoun.append(word)
    
    wordcloud = WordCloud(stopwords=stop_words).generate(' '.join(allnoun))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    Freq_dist_nltk=nltk.FreqDist(allnoun)
    Freq_dist_nltk.plot(50, cumulative=False)

    with open('translate_nltk_allnoun.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([allnoun])
