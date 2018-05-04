# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:36:16 2018

@author: cristobal
"""
#References:Python Code to train a Hidden Markov Model, using NLTK 
#https://gist.github.com/blumonkey/007955ec2f67119e0909

import nltk
from nltk.tag import hmm
nltk.download('maxent_treebank_pos_tagger')
#nltk.download()

textFile=open("texts/text_02.txt","r")
text=textFile.read()
textSent=nltk.sent_tokenize(text)
textWords=nltk.word_tokenize(text)
wordPos=nltk.pos_tag(textWords)

nltk.tag

train_data =nltk.corpus.conll2000.chunked_sents('train.txt')[99]
#print()

train_data = nltk.corpus.treebank.tagged_sents()
#print(train_data[0])
# Setup a trainer with default(None) values
# And train with the data
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

tagger.tag(textSent[0].lower().split())

print(tagger.tag("He is a Fortunate Fan.".split()))
print(tagger.tag("The man is a classic story.".lower().split()))

nltk.tag.hmm.tag(text)

nltk.batch_pos_tag(text)

for item in wordPos[0:20]:
    print(item)
        
