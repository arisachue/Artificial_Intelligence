# -*- coding: utf-8 -*-

#ch5 34
# import nltk
# from nltk.corpus import brown
# from tabulate import tabulate

# tags = brown.tagged_words()
# cfd = nltk.ConditionalFreqDist(tags)

# num_tags = []
# for condition in cfd.conditions():
#     num_tags.append((condition, len(cfd[condition])))

# tags_by_num = []

# for i in range(11):
#     this_num = 0
#     for (word, num) in num_tags:
#         if num == i:
#             this_num += 1
#     tags_by_num.append((i, this_num))

# # prints a table of the integers 1-10 and the numbers of distinct words in the corpus that have those numbers of distinct tags

# print(tabulate(tags_by_num))

# # "that" is the word with the most distinct tags.
# distinct_tags = [tag for tag in cfd['that']]

# tagged_sents = brown.tagged_sents()

# # go through each sentence in the corpus. 
# # go through each tag in the sentence

# for sent in tagged_sents:
#     for (word, tag) in sent:
#         for distinct_tag in distinct_tags:
#             if distinct_tag == tag and (word == 'That' or word == 'that'):
#                 print(sent)
#                 distinct_tags.remove(distinct_tag)
#                 print("************")
#                 break

#ch2 25
# import nltk
# from nltk.corpus import udhr

# # Define a function find_language() that takes a string as its argument, and returns a list of languages that have that string as a word. Use the udhr corpus and limit your searches to files in the Latin-1 encoding.

# def find_language(string):
#     languages = []
#     target_languages = []

#     for name in nltk.corpus.udhr.fileids():
#         if 'Latin1' in name:
#             languages.append(name)

#     for lang in languages:
#         if string in nltk.corpus.udhr.words(lang):
#             target_languages.append(lang)

#     return target_languages

# print(find_language("solo"))

# ch2 26
# import nltk
# from nltk.corpus import wordnet as wn

# all_noun_synsets = list(wn.all_synsets('n'))

# hyponym_count = 0
# synset_count = 0

# for item in all_noun_synsets:
# 	if item.hyponyms():
# 		hyponym_count += len(item.hyponyms())
# 		synset_count += 1

# # print(hyponym_count)
# # print(synset_count)
# average_hyponym_branching = hyponym_count / synset_count
# print(average_hyponym_branching)

#ch5 ex35
# import nltk
# from nltk.corpus import brown

# tagged_words = brown.tagged_words()
# cfd = nltk.ConditionalFreqDist(tagged_words)
# tagged_sents = brown.tagged_sents()

# bigram_tags = list(nltk.bigrams(tagged_words))

# words_following_must = []
# for bigram in bigram_tags:
#     # returns a list of the form [['of', 'years'], ['IN', 'NNS']]
#     zipped_tag = [list(t) for t in zip(*bigram)]
#     if zipped_tag[0][0] == 'must' or zipped_tag[0][0] == 'Must':
#         words_following_must.append((zipped_tag[0][1], zipped_tag[1][1]))

# tags_following_must = set([tag for (__,tag) in words_following_must])

# for bigram in bigram_tags:
#     zipped_tag = [list(t) for t in zip(*bigram)]
#     if zipped_tag[0][0] == 'must' or zipped_tag[0][0] == 'Must':
#         print(zipped_tag[0][0] + " " + zipped_tag[0][1])
#         if zipped_tag[1][1] in ['BE', 'BE-HL', 'NN', 'NNS', 'NP-HL']:
#             print("Context is likely epistemic")
#         elif zipped_tag[1][1] in ['HV', 'HV-TL', 'DO',  'RB', 'RB-HL', 'VB', 'VB-HL', 'VB-TL', 'VBZ']:
#             print("Context is likely deontic")
#         else:
#             print("Context is unclear")

from nltk.corpus import wordnet as wn
pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'), ('boy', 'lad'), ('coast', 'shore'), 
         ('asylum', 'madhouse'), ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'), 
         ('bird', 'cock'), ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'), 
         ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'), ('food', 'rooster'), 
         ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'), ('monk', 'slave'), ('coast', 'forest'), 
         ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'), ('rooster', 'voyage'), ('noon', 'string')]
lch = []
for word1, word2 in pairs:
    lch.append((word1, word2, wn.lch_similarity(wn.synsets(word1)[0], wn.synsets(word2)[0])))
from operator import itemgetter
lch = sorted(lch,key=itemgetter(2),reverse=True)
print(lch)

path = []
for word1, word2 in pairs:
    path.append((word1, word2, wn.path_similarity(wn.synsets(word1)[0], wn.synsets(word2)[0])))
path = sorted(path,key=itemgetter(2),reverse=True)
print(path)