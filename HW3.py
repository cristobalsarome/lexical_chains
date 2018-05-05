# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:36:16 2018

@author: cristobal
"""
#References:Python Code to train a Hidden Markov Model, using NLTK 
#https://gist.github.com/blumonkey/007955ec2f67119e0909
from AuxFunctions import AuxFunctions as aux
import nltk
from nltk.corpus import wordnet

#nltk.download()

textFile=open("texts/text_02.txt","r")
text=textFile.read()
textSent=nltk.sent_tokenize(text)
textWords=nltk.word_tokenize(text)
wordPos=nltk.pos_tag(textWords)


nouns=[]
for item in wordPos:
    if item[1][0]=="N":
        nouns.append(item[0])
        
#print(nouns)        
wordnet.synsets("dog")
wordnet.synset("dog.n.01") 

syns=wordnet.synsets(nouns[1])
syns=wordnet.synsets("love")
lem=syns[0].lemmas()
lem[0].antonyms()
# An example of a synset:
#print(syns[0].name())
 
# Just the word:
#print(syns[0].lemmas())



hypo = lambda s: s.hyponyms()
hyper = lambda s: s.hypernyms()
dog=wordnet.synsets("dog")[0]
doglem=dog.lemmas()
dog.hypernyms()
doglem[1].hypernyms()
#dog.antonyms()
dog.hyponyms()
hyperdog = set([i for i in dog.closure(lambda s:s.hypernyms())])

synonyms = []
antonyms = []
hypernyms = []
hyponyms = [] 
for syn in wordnet.synsets("dog"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
        if l.hyponyms():
            print("AAAAAAA")
            [hyponyms.append(i.name()) for i in l.closure(lambda s:s.hyponyms())]
        if l.hypernyms():
            print("AAAAAAA")
            hypernyms.append(set([i for i in l.closure(lambda s:s.hypernyms())]))
 
#print(set(synonyms))
print(set(antonyms))
 
hyponyms.append(set([i for i in dog.closure(lambda s:s.hyponyms())]))
[hyponyms.append(i.name()) for i in dog.closure(lambda s:s.hyponyms())]
dog.hyponyms()

