import csv
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

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
            tokens=nltk.word_tokenize(content)
            #print(tokens)
            tagged_tokens=nltk.pos_tag(tokens)
            for word,pos in tagged_tokens:
                if word not in stop_words and pos in ['NN', 'NNP']:
                    allnoun.append(word)
    
    noun_dict = {}
    for noun in allnoun:
        if noun not in noun_dict:
            noun_dict[noun] = 1
        else:
            noun_dict[noun] += 1
    #print(noun_dict)

    noun_dict = dict(sorted(noun_dict.items(), key=lambda x: x[1], reverse=True))
    #print(noun_dict)

    plt.figure()
    plt.plot(range(1,31),list(noun_dict.values())[:30])
    plt.xticks(range(1,31),labels=list(noun_dict.keys())[:30])
    plt.show()


