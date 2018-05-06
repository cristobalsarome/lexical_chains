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
    def __init__(self,word,wordIndex,sentIndex):
        self.wordIndexes=[]
        self.sentIndexes=[]
        self.words=[]
        self.synonyms=[]
        self.antonyms=[]
        self.hypernyms=[]
        self.hyponyms=[]
        self.holonyms=[]
        self.add(word,wordIndex,sentIndex)
        self.closed=False
        #we keep record of how many words we add by
        #different method. This is usefull to adjuts the
        #threshold
        self.bycomparison=0
        self.bysimilarity=0

    def add(self,word,wordIndex,sentIndex):
        self.wordIndexes.append(wordIndex)
        self.sentIndexes.append(sentIndex)
        self.words.append(word)
        self.synonyms.extend(aux.findSynonyms(word))
        self.antonyms.extend(aux.findAntonyms(word))
        self.hypernyms.extend(aux.findHypernyms(word))
        self.hyponyms.extend(aux.findHyponyms(word))
        self.holonyms.extend(aux.findHolonyms(word))
    def checkAdd(self,word,wordIndex,sentIndex):
        cond1=word in self.words
        cond2=word in self.synonyms
        cond3=word in self.antonyms
        cond4=word in self.hypernyms
        cond5=word in self.hyponyms
        cond6=word in self.holonyms
        
        #find similarity
        if (cond1 or cond2 or cond3 or cond4 or cond5 or cond6):
            self.add(word,wordIndex,sentIndex)
            self.bycomparison+=1
            return True
        else:
            if aux.findSimilarity(0.90,word,self.words):
                self.add(word,wordIndex,sentIndex)
                #print("match!")
                self.bysimilarity+=1
                return True
            return False
    def getChain(self):
        #we compute the word counts with a dictionary
        #first we initialize to 0
        chain={word: 0 for word in self.words}
        #after that we count the word occurrence
        for word in self.words:
            chain[word]=chain[word]+1
        return chain
                
        
def main():
    text_number="02"           
    #We set the path with the text to analyze
    textFile=open("texts/text_"+text_number+".txt","r")
    text=textFile.read()
    textFile.close()

    nouns=[]
    sentences=dict()

    #We assign index to every word and sentence
    #so we can track down from the chains to the
    #original text.
    sentIndex=0
    wordIndex=0
    #We'll tokenize and extract the nouns
    textSent=nltk.sent_tokenize(text)
    for sent in textSent:
            sentIndex+=1 #the position of the sentence in the text
            textWords=nltk.word_tokenize(sent)
            wordPos=nltk.pos_tag(textWords)
            sentences[sentIndex]=sent
            for item in wordPos:
                wordIndex+=1 #the position of the word in the text
                if item[1][0]=="N":
                    word=item[0].lower()
                    if len(word)>1:
                        nouns.append([word,wordIndex,sentIndex])
        
    #lexicalChains=[]
    #lc1=LexicalChain(nouns[0][0],nouns[0][1])
    
    print("Obtaining Lexical Chains")
    lexChains=[]
    wordsAdded=[]
    i=0 
    for initial in nouns:
        word1=initial[0]
        index1=initial[1]
        sentIndex1=initial[2]
        i+=1
        print('.', end='')
        if index1 not in wordsAdded:
            lexChains.append(LexicalChain(word1,index1,sentIndex1))
            wordsAdded.append(index1)
            #print(len(lexChains))
            for lc in lexChains:
                if not lc.closed:             
                    for item in nouns:
                        #i+=1
                        #print([i,len(lc.words)])
                        word2=item[0]
                        index2=item[1]
                        sentIndex2=item[2]
                        if index2 not in wordsAdded:
                            added=lc.checkAdd(word2,index2,sentIndex2) 
                            if added: wordsAdded.append(index2)
                    lc.closed=True

    Functions.printResult(lexChains)
    
    text_file = open("texts/summary_"+text_number+".txt", "w")
    text_file.write(Functions.summarize(lexChains,sentences))
    text_file.close()
    

class auxFun:                    

        def printResult(lexChains):
            i=0
            for chain in lexChains:
                print()
                i+=1
                c=chain.getChain()
                print("chain "+str(i)+': ',end='')
                for word in c:
                    print(word+"("+str(c[word])+"), ",end='')
        def summarize(lexChains, sentences):
            summary=''
            maxLen=0
            for chain in lexChains:
                if len(chain.words)>maxLen:
                    maxLen=len(chain.words)
                    mainChain=chain

            sumSentences=set(mainChain.sentIndexes)
            for sen in sumSentences:
                summary=summary+sentences[sen]
                
            return summary
            
            
            
        def test(lexChains):
            
            print(len(lexChains))
            
            for lc in lexChains[:20]: 
                print(set(lc.words))
            for lc in lexChains[:10]: 
                print(lc.indexes)
            i=0
            for lc in lexChains:
                a=len(lc.indexes)
                if a>1:
                    i+=1
                    print([a,lc.words])
            print(i)
                
            for lc in lexChains:
                print(len(lc.indexes))
            for lc in lexChains:
                print([lc.bycomparison,lc.bysimilarity])
            for lc in lexChains:
                print(lc.getChain())


if __name__ == "__main__":
    main()



