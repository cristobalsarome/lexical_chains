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
    def checkAdd(self,word,index):
        cond1=word in self.words
        cond2=word in self.synonyms
        cond3=word in self.antonyms
        cond4=word in self.hypernyms
        cond5=word in self.hyponyms
        if (cond1 or cond2 or cond3 or cond4 or cond5):
            self.add(word,index)
            return True
        else:
            return False
            
#    def tryAdd(word):
        
    

textFile=open("texts/text_01.txt","r")
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
    
#lexicalChains=[]
#lc1=LexicalChain(nouns[0][0],nouns[0][1])

lexChains=[]
wordsAdded=[]
lexChains=[LexicalChain(nouns[0][0],nouns[0][1])]
#i=0
for lc in lexChains:
    print(len(lexChains))
    for item in nouns:
        word=item[0]
        index=item[1]
        if index not in wordsAdded:
            added=lc.checkAdd(word,index) 
            if added: 
                wordsAdded.append(index)
                print(["exi",word])
            else:
                lexChains.append(LexicalChain(word,index))
                wordsAdded.append(index)
                print(["new",word])
#            if len(lexChains)>20: 
#                print("TOO MUCH")
#                break
#i+=1
    


#for lc in lexChains[:50]: 
#    print(lc.words)
#for lc in lexChains[:10]: 
#    print(lc.indexes)
#for lc in lexChains:
#    a=len(lc.indexes)
#    if a>1: print([a,lc.words])
#
#
#    
#len(lexChains)
#lc1.indexes
#lc
#lc1.antonyms
#lc1.synonyms
#lc1.hypernyms
#lc1.hyponyms



