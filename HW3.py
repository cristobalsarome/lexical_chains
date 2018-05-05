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
        
print(nouns)        
wordnet.synsets("dog")
wordnet.synset("dog.n.01") 

wordnet.synsets(nouns[1])




