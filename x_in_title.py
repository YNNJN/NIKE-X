import csv
import nltk
import re


with open('data/articles.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    collabos = []
    
    for info in reader:
        title = info[0]
        if title.find(' ' + 'x' + ' ') >= 0:
            collabos.append(title)

    locas =[]
    for i in range(len(collabos)):

        pattern = r' x '
        iterator = re.finditer(pattern, collabos[i])
        loca = []
        for match in iterator:
            loca.append(match.span()) 
        # loca = [(s,e),(s,e),(s,e),... ]
        locas.append(loca) #[loca,loca, ]

    #[print(loca) for loca in locas]
    
    for i in range(len(locas)):
        loca = locas[i]
        for (s,e) in loca:
            print(collabos[i][s:e])
        print("")

# with open('x_in_title.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for noun in title_noun_phrases:
#         writer.writerow([noun])



