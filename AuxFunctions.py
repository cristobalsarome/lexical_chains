


class AuxFunctions:
	def wordnet_pos_code(tag):
	#Source:http://www.ling.helsinki.fi/~gwilcock/Tartu-2011/P2-nltk-2.xhtml
		if tag.startswith('NN'):
			return wordnet.NOUN
		elif tag.startswith('VB'):
			return wordnet.VERB
		elif tag.startswith('JJ'):
			return wordnet.ADJ
		elif tag.startswith('RB'):
			return wordnet.ADV
		else:
			return ''


	def wordnet_pos_label(tag):
	#Source:http://www.ling.helsinki.fi/~gwilcock/Tartu-2011/P2-nltk-2.xhtml
		if tag.startswith('NN'):
			return "Noun"
		elif tag.startswith('VB'):
			return "Verb"
		elif tag.startswith('JJ'):
			return "Adjective"
		elif tag.startswith('RB'):
			return "Adverb"
		else:
			return tag