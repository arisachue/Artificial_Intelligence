# -*- coding: utf-8 -*-

import nltk

# ch2, ex4
# from nltk.corpus import state_union

# cfd = nltk.ConditionalFreqDist(
#   (target, fileid[:4])
#   for fileid in state_union.fileids()
#   for w in state_union.words(fileid)
#   for target in ['men', 'women', 'people']
#   if w.lower().startswith(target))

# cfd.plot()

# for fileid in state_union.fileids():
#     mc = 0
#     wc = 0
#     pc = 0
#     for w in state_union.words(fileid):
#         for target in ['men', 'women', 'people']:
#             if w.lower().startswith(target):
#                 if target == "men": mc +=1
#                 if target == "women": wc +=1
#                 if target == "women": pc +=1
#     print(fileid[:4], "men:", mc, "women:", wc, "people:", pc)

# ch2, ex 5
# from nltk.corpus import wordnet as wn
# print(wn.synsets('school')[0].member_meronyms())
# print(wn.synsets('tree')[0].part_meronyms())
# print(wn.synsets('tree')[0].substance_meronyms())
# print(wn.synsets('tree')[0].member_holonyms())
# print(wn.synsets('kitchen')[0].part_holonyms())
# print(wn.synsets('ice')[0].substance_holonyms())

# ch2, ex7
# nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('however', lines=1000)

#ch 2, ex9
from nltk.corpus import brown
# gov = nltk.Text(brown.words(categories='romance'))
# rel = nltk.Text(brown.words(categories='news'))
# # news_fd = nltk.FreqDist(gov)
# # religion_fd = nltk.FreqDist(rel)
# print(gov.concordance('date'))
# print(rel.concordance('date'))

# ch2, ex12
# from nltk.corpus import cmudict
# words = [word for word,pron in cmudict.entries() ]
# wordset=set(words)
# cmu=cmudict.dict()
# print(len(words))
# print(len(wordset))
# more_than_one_pron=[word for word in wordset if len(cmu.get(word))>1]
# print(len(more_than_one_pron), len(wordset),"% words have more than one pronounciation")

# ch2, ex17
from nltk.corpus import stopwords
# freq_fd=nltk.FreqDist(brown.words(categories='romance'))
# words=[w for w in freq_fd]
# for w in words:
#     if w in stopwords.words() or not w.isalpha():
#         freq_fd.pop(w)
# ans = freq_fd.most_common(50)
# print([w for w, f in ans])

# ch2, ex18
# bigrams_without_stopwords = [(a,b) for a,b in nltk.bigrams(brown.words(categories="news")) if a not in stopwords.words('english') and a.isalpha() and b.isalpha() and b not in stopwords.words('english')]
# bigrams_without_stopwords_fd = nltk.FreqDist(bigrams_without_stopwords)
# ans = bigrams_without_stopwords_fd.most_common(50)
# print([w for w, f in ans])

# ch3 ex20
from urllib import request
# url = "https://api.weather.gov/gridpoints/LWX/89,65/forecast"
# html = request.urlopen(url).read().decode('utf8')
# print(html[2100:2200])

# ch3 ex22
# import re
# response = request.urlopen('http://news.bbc.co.uk/')
# raw = response.read().decode('utf8')
# print(re.sub(r'(<.*?>|<\/.*?>)(?s)', '', raw))

# ch2 ex27
from nltk.corpus import wordnet as wn
print("average polysemy of: ")
# nouns
synsets = wn.all_synsets("n")
lemmas = set()
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, "n"))
print("nouns: %s" % (count/len(lemmas)))
# verbs
synsets = wn.all_synsets("v")
lemmas = set()
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, "v"))
print("verbs: %s" % (count/len(lemmas)))
# adjective
synsets = wn.all_synsets("a")
lemmas = set()
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, "a"))
print("adjectives: %s" % (count/len(lemmas)))
# adverbs
synsets = wn.all_synsets("r")
lemmas = set()
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, "r"))
print("adverbs: %s" % (count/len(lemmas)))

# ch6 ex4
# from nltk.corpus import movie_reviews
# from nltk.classify import apply_features
# documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
# #construct list of most frequent words in entire corpus, define feature extractor that simply checks whether each of these words is present in a given document
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words)[:2000]
# #that is 2000 features
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains({})'.format(word)] = (word in document_words)
#     return features
# # print(document_features(movie_reviews.words('pos/cv957_8737.txt')))
# #train classifier
# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# # print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(30))