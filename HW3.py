# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:36:16 2018

@author: cristobal
"""

from auxiliary import AuxFunctions as aux
import nltk
import re
from nltk.corpus import wordnet

#nltk.download()
class LexicalChain:
    def __init__(self,word,index):
        self.indexes=[]
        self.words=[]
        self.synonyms=[]
        self.antonyms=[]
        self.hypernyms=[]
        self.hyponyms=[]
        self.add(word,index)
    def add(self,word,index):
        self.indexes.append(index)
        self.words.append(word)
        self.synonyms.extend(aux.findSynonyms(word))
        self.antonyms.extend(aux.findAntonyms(word))
        self.hypernyms.extend(aux.findHypernyms(word))
        self.hyponyms.extend(aux.findHyponyms(word))
#    def tryAdd(word):
        
    

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
        nouns.append([item[0].lower(), index])
#        wordIndex.append(index)
    index+=1
    
lexicalChains=[]
lc1=LexicalChain(nouns[1][0],nouns[1][1])
  
for item in nouns:
    
    




