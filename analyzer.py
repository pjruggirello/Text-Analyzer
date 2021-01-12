# Philip Ruggirello 1/12/21

class Analyzer:
	"""This will be the analyzer onbject whihc will contains the mehtods for the different ways the inputed txt file can be anaylzed."""
	def __init__(self):
		"""Conatins the attributes of the analyzer object."""
		self.nouns = '/home/peejay/python/text_analysis/nouns.txt'
		self.pronouns = ['i', 'me', 'my', 'mine', 'myself',
					     'you', 'your', 'yours', 'yourself',
					     'he', 'him', 'his', 'himself',
					     'she', 'her', 'hers', 'herself',
					     'it', 'its', 'itself',
					     'we', 'us', 'our', 'ours', 'ourselves', 
					     'yourselves',
					     'they', 'them', 'their', 'theirs', 'themselves']
		self.verbs = '/home/peejay/python/text_analysis/verbs.txt'
		self.adjectives = '/home/peejay/python/text_analysis/adjectives.txt'
		self.adverbs = '/home/peejay/python/text_analysis/adverbs.txt'
		self.prepositions = []
		self.conjunctions = []
		self.interjections = []
