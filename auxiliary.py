from nltk.corpus import wordnet
import inspect
import re

class AuxFunctions:
    
    
    def findSynonyms(word):
        synsets=[]
        synonyms=[]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synsets.append(l.name())
#        for item in synsets:
#            type=re.findall('\..\.',item.synset())[0]
#            if type==".n.":
#                synonyms.append(item.name())
        return synonyms
    
    def findAntonyms(word):
        antonyms=[]
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    [antonyms.append(anti.name()) for anti in l.antonyms()]
        return antonyms
        
    def findHypernyms(word):
        hypernyms=[] 
        for syn in wordnet.synsets(word):
            [hypernyms.append(i.name()) for i in syn.closure(lambda s:s.hypernyms(), depth=2)]
        return hypernyms
        
    
    def findHyponyms(word):
        hyponyms=[]  
        for syn in wordnet.synsets(word):
            [hyponyms.append(i.name()) for i in syn.closure(lambda s:s.hyponyms(), depth=2)]
        return hyponyms

a=AuxFunctions.findSynonyms("dog")
  
#    def wordnet_pos_code(tag):
#	#Source:http://www.ling.helsinki.fi/~gwilcock/Tartu-2011/P2-nltk-2.xhtml
#        if tag.startswith('NN'):
#            return wordnet.NOUN
#        elif tag.startswith('VB'):
#            return wordnet.VERB
#        elif tag.startswith('JJ'):
#            return wordnet.ADJ
#        elif tag.startswith('RB'):
#            return wordnet.ADV
#        else:
#            return ''
#
#
#    def wordnet_pos_label(tag):
#	     #Source:http://www.ling.helsinki.fi/~gwilcock/Tartu-2011/P2-nltk-2.xhtml
#        if tag.startswith('NN'):
#            return "Noun"
#        elif tag.startswith('VB'):
#            return "Verb"
#        elif tag.startswith('JJ'):
#            return "Adjective"
#        elif tag.startswith('RB'):
#            return "Adverb"
#        else:
#            return tag