import csv
import nltk
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from collections import Counter
from itertools import chain
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS


with open('data/body_contents.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    nouns_list = []
    for contents in reader:
        for content in contents:
            content = TextBlob(content)
            for noun in content.noun_phrases:
                nouns_list.append(noun)

stopwords = set(STOPWORDS)
stopwords.add('nike')
stopwords.add('News')
stopwords.add('Inc Rights')
stopwords.add('para')
stopwords.add('que')
stopwords.add('da')
stopwords.add('um')
stopwords.add('em')
stopwords.add('uma')

# wordcloud = WordCloud(stopwords=stopwords).generate(' '.join(nouns_list))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()


# counts = Counter(nouns_list)
# counts = counts.most_common()

# word = [counts[i][0] for i in range(len(counts))][1:31]
# num = [counts[i][1] for i in range(len(counts))][1:31]
# xs = [i for i, _ in enumerate(word)]

# print(word)
# print(num)
# print(xs)

# # fig = go.Figure()
# # fig.add_trace(go.scatter(
# #     x = xs,
# #     y = num
# # ))
# # fig.update_layout(xaxis_type="log", yaxis_type="log")
# # fig.show()


plt.figure(figsize=(12,6))
words = nltk.Text(nouns_list, name='frequency')
print(words)
words.plot(50)
plt.show()