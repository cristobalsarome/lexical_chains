# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:36:16 2018

@author: cristobal
"""

from AuxFunctions import AuxFunctions as aux
import nltk
from nltk.corpus import wordnet

#nltk.download()

textFile=open("texts/text_02.txt","r")
text=textFile.read()
textFile.close()
textSent=nltk.sent_tokenize(text)
textWords=nltk.word_tokenize(text)
wordPos=nltk.pos_tag(textWords)


nouns=[]
index=0
wordIndex=[]
for item in wordPos:
    if item[1][0]=="N":
        nouns.append(item[0])
        wordIndex.append(index)
    index+=1
    
        



synonyms = []
antonyms = []
hypernyms = []
hyponyms = [] 
for syn in wordnet.synsets("dog"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
    [hyponyms.append(i.name()) for i in syn.closure(lambda s:s.hyponyms())]
    [hypernyms.append(i.name()) for i in syn.closure(lambda s:s.hypernyms())]
    

#print(nouns)        
wordnet.synsets("dog")
wordnet.synset("dog.n.01") 

syns=wordnet.synsets(nouns[1])
syns=wordnet.synsets("love")
lem=syns[0].lemmas()
lem[0].antonyms()
 

