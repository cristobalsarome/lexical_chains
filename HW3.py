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
        self.holonyms=[]
        self.add(word,index)
        self.closed=False
    def add(self,word,index):
        self.indexes.append(index)
        self.words.append(word)
        self.synonyms.extend(aux.findSynonyms(word))
        self.antonyms.extend(aux.findAntonyms(word))
        self.hypernyms.extend(aux.findHypernyms(word))
        self.hyponyms.extend(aux.findHyponyms(word))
        self.holonyms.extend(aux.findHolonyms(word))
    def checkAdd(self,word,index):
        cond1=word in self.words
        cond2=word in self.synonyms
        cond3=word in self.antonyms
        cond4=word in self.hypernyms
        cond5=word in self.hyponyms
        cond6=word in self.holonyms
        
        #find similarity
        
        if (cond1 or cond2 or cond3 or cond4 or cond5 or cond6):
            self.add(word,index)
            return True
        else:
            cond7=aux.findSimilarity(0.9,word,self.words)
            if cond7:
                self.add(word,index)
                print("match!")
                return True
            return False
            
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
        word=item[0].lower()
        if len(word)>1:
            nouns.append([word,index])
#        wordIndex.append(index)
    index+=1
    
#lexicalChains=[]
#lc1=LexicalChain(nouns[0][0],nouns[0][1])

lexChains=[]
wordsAdded=[]
i=0 
for initial in nouns:
    word1=initial[0]
    index1=initial[1]
    i+=1
    print(i)
    if index1 not in wordsAdded:
        lexChains.append(LexicalChain(word1,index1))
        wordsAdded.append(index1)
        #print(len(lexChains))
        for lc in lexChains:
            if not lc.closed:
                               
                for item in nouns:
                    #i+=1
                    #print([i,len(lc.words)])
                    word2=item[0]
                    index2=item[1]
                    if index2 not in wordsAdded:
                        added=lc.checkAdd(word2,index2) 
                        if added: wordsAdded.append(index2)
                        #print(["exi",word])
                lc.closed=True
                
print(len(lexChains))

for lc in lexChains[:20]: 
    print(set(lc.words))
for lc in lexChains[:10]: 
    print(lc.indexes)
for lc in lexChains:
    a=len(lc.indexes)
    if a>1: print([a,lc.words])
    
for lc in lexChains:
    print(len(lc.indexes))


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



