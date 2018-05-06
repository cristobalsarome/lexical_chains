# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:36:16 2018

@author: cristobal
"""
import nltk
import re
from nltk.corpus import wordnet
#nltk.download()
class LexicalChain:
    #We define the class Lexical Chain, with the methods
    #and fields needed. We'll create one object of this class
    #for each lexical chain that we find
    def __init__(self,word,wordIndex,sentIndex):
        #We assign index to every word and sentence
        #so we can track down from the chains to the
        #original text.
        self.wordIndexes=[]
        self.sentIndexes=[]
        #the word belonging to each chain
        self.words=[]
        #We find synonyms, antonyms, hypernyms, hyponyms
        #and holonyms for each word we add to the chain
        self.synonyms=[]
        self.antonyms=[]
        self.hypernyms=[]
        self.hyponyms=[]
        self.holonyms=[]
        #We initialize the object with the first word added to
        #the chain
        self.add(word,wordIndex,sentIndex)
        self.closed=False
        #we keep record of how many words we add by
        #different method. This is usefull to adjuts the
        #threshold
        self.bycomparison=0
        self.bysimilarity=0

    def add(self,word,wordIndex,sentIndex):
        #this method adds a new word and calls the 
        #auxiliary methods to store related words
        #(synonyms, antonyms, etc)
        self.wordIndexes.append(wordIndex)
        self.sentIndexes.append(sentIndex)
        self.words.append(word)
        self.synonyms.extend(AuxFunctions.findSynonyms(word))
        self.antonyms.extend(AuxFunctions.findAntonyms(word))
        self.hypernyms.extend(AuxFunctions.findHypernyms(word))
        self.hyponyms.extend(AuxFunctions.findHyponyms(word))
        self.holonyms.extend(AuxFunctions.findHolonyms(word))
        
    def checkAdd(self,word,wordIndex,sentIndex):
        #This method checks a candidate word for
        #addition to the list. If the result is positive
        #it adds the word to the chain and return true.
        #Otherwise ignores the word and returns false
        #The decision is based on two main criteria
        #1)Is equal to some of the related words
        #2)Computing the similaryti function
        #with wordnet (more expensive)
        cond1=word in self.words
        cond2=word in self.synonyms
        cond3=word in self.antonyms
        cond4=word in self.hypernyms
        cond5=word in self.hyponyms
        cond6=word in self.holonyms
        
        #We check first for related word because is less expensive
        if (cond1 or cond2 or cond3 or cond4 or cond5):# or cond6):
            self.add(word,wordIndex,sentIndex)
            #We keep track of the number of words added through
            #different criteria for tunning purposes
            self.bycomparison+=1
            return True
        else:
#            #Only if we dont find related words we compute the similarity
#            #of the new words with the existings words in the chain
#            if AuxFunctions.findSimilarity(0.90,word,self.words):
#                self.add(word,wordIndex,sentIndex)
#                #We keep track of the number of words added through
#                #different criteria for tunning purposes
#                self.bysimilarity+=1
#                return True
            return False
        
    def getChain(self):
        #we compute the word counts with a dictionary
        #first we initialize to 0
        chain={word: 0 for word in self.words}
        #after that we count the word occurrence
        for word in self.words:
            chain[word]=chain[word]+1
        return chain

class AuxFunctions:
    def findSynonyms(word):
        #This functions returns a list of synonims of the input
        synsets=[]
        synonyms=[]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synsets.append(l)
        for item in synsets:
            type=re.findall('\..\.',item.synset().name())[0]
            if type==".n.":
                synonyms.append(item.name())
        return synonyms
    
    def findAntonyms(word):
        #This functions returns a list of antonyms of the input
        synsets=[]
        antonyms=[]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    [antonyms.append(anti.name()) for anti in l.antonyms()]
        for item in synsets:
            type=re.findall('\..\.',item.synset().name())[0]
            if type==".n.":
                antonyms.append(item.name())
        return antonyms
        
    def findHypernyms(word):
        #This functions returns a list of hypernyms of the input
        synsets=[]
        hypernyms=[] 
        for syn in wordnet.synsets(word):
            for i in syn.closure(lambda s:s.hypernyms(), depth=3):
                synsets.append(i.name())
        for item in synsets:
            type=re.findall('\..\.',item)[0]
            hyper=re.findall('.*?(?=\.)',item)[0]
            if type==".n.":
                hypernyms.append(hyper)
        return hypernyms        
    
    def findHyponyms(word):
        #This functions returns a list of hyponyms of the input
        synsets=[]
        hyponyms=[]  
        for syn in wordnet.synsets(word):
            for i in syn.closure(lambda s:s.hyponyms(), depth=3):
                synsets.append(i.name())
        for item in synsets:
            type=re.findall('\..\.',item)[0]
            hypo=re.findall('.*?(?=\.)',item)[0]
            if type==".n.":
                hyponyms.append(hypo)
        return hyponyms
    
    def findHolonyms(word):
        #This functions returns a list of holonyms of the input
        holonyms=[]
        synsets=[]
        for syn in wordnet.synsets(word):
            synsets.extend(syn.member_holonyms())
        for item in synsets:
            type=re.findall('\..\.',item.name())[0]
            holo=re.findall('.*?(?=\.)',item.name())[0]
            if type==".n.":
                holonyms.append(holo)
        return holonyms
    
    def findSimilarity(threshold,word,bagWords):
        #This functions compute the similarity a word and a word list
        #using the wup_similarity function. The parameter threshold
        #can be used as a tunning parameter. It returns true if the
        #similarity is greater than the threshold for any of the words
        #and false otherwise. This is an expensive function, specially
        #if the word list to compare contains many elements.
        for synset1 in wordnet.synsets(word):
            for word2 in bagWords:
                for synset2 in wordnet.synsets(word2):
                    simil=synset1.wup_similarity(synset2)
                    if (simil and(float(simil) > threshold)): 
                            return True
        return False                    

    def printResult(lexChains):
        #This function prints the results in the console
        #as requested in the assignment
        i=0
        for chain in lexChains:
            print()
            i+=1
            c=chain.getChain()
            print("chain "+str(i)+': ',end='')
            for word in c:
                print(word+"("+str(c[word])+"), ",end='')                
                
    def summarize(lexChains, sentences):
        #This function takes as input the lexical chains
        #and the original sentences and returns a Summary
        #in form of string.
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
        #Not important.
        #Test functions used during development/debugging
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

                
        
def main():
    #Main Method, we indicate here the number of the text
    #to explore and summarize
    text_number="01"           
    #We set the path with the text to analyze
    textFile=open("texts/text_"+text_number+".txt","r")
    text=textFile.read()
    textFile.close()
    
    #the list nouns will contain all words (nouns)
    #that we'll consider for our lexical chains
    nouns=[]
    #We'll also have a dictionary that map the number of sentence
    #with the complete sentence text in order to create a summary
    sentences=dict()   

    #We assign index to every word and sentence
    #so we can track down from the chains to the
    #original text. Here we initialize those indexes
    sentIndex=0
    wordIndex=0
    #We'll tokenize and extract the sentences
    textSent=nltk.sent_tokenize(text)
    for sent in textSent:
            #we record the sentence number
            sentIndex+=1
            #we split the sentence in words
            textWords=nltk.word_tokenize(sent)
            #we get the POS tag for each word
            wordPos=nltk.pos_tag(textWords)
            #we record the sentence text and number
            sentences[sentIndex]=sent
            for item in wordPos:
                #we record the word number (the position of the 
                #word in the text). This is useful, to
                #keep a record of which words have been already added
                #to some lexical chain
                wordIndex+=1
                #We keep only the nouns
                if item[1][0]=="N":
                    word=item[0].lower()
                    if len(word)>1:
                        nouns.append([word,wordIndex,sentIndex])
        

    
    print("Obtaining Lexical Chains")
    #this list will contain all our lexical chains
    lexChains=[]
    wordsAdded=[]
    i=0
    #We traverse through the nouns extracted previously
    for initial in nouns:
        #we choose one word
        word1=initial[0]
        index1=initial[1]
        sentIndex1=initial[2]
        i+=1
        print('.', end='')#this is for progress visualization
        #if the word selected is not in any chain
        if index1 not in wordsAdded:
            #We create a new chain with that word and append it to the list
            lexChains.append(LexicalChain(word1,index1,sentIndex1))
            #We record that word as added, so it won't be added to another chain
            wordsAdded.append(index1)
            #Now we traverse the whole text looking for more
            #words to add to the chain
            for lc in lexChains:
                #We don't add words to closed chains
                if not lc.closed:             
                    for item in nouns:
                        word2=item[0]
                        index2=item[1]
                        sentIndex2=item[2]
                        #If the new word is not in any chain
                        #we consider it a candidate for the new chain
                        if index2 not in wordsAdded:
                            #The method checkAdd, look for similarities and
                            #determine weather to add the word to the chain or not.
                            added=lc.checkAdd(word2,index2,sentIndex2)
                            #If the word is added we record it as added
                            if added: wordsAdded.append(index2)
                    #When we finish traversing the text, we flag the current
                    #chain as closed, so we don't add more words to it
                    #and don't expend computing power comparing words to this chain
                    lc.closed=True
    
    #We print the results in the format requested
    AuxFunctions.printResult(lexChains)
    
    #We use the lexical chains to create a summary
    #And save it to a file
    text_file = open("texts/summary_"+text_number+".txt", "w")
    text_file.write(AuxFunctions.summarize(lexChains,sentences))
    text_file.close()
    

if __name__ == "__main__":
    main()



