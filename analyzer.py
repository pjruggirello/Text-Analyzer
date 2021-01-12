# Philip Ruggirello 1/12/21

class Analyzer:
	"""This will be the analyzer onbject whihc will contains the mehtods for the different ways the inputed txt file can be analyzed."""
	def __init__(self):
		"""Conatins the attributes of the analyzer object."""
		self.list_of_nouns = '/home/peejay/python/text_analysis/nouns.txt'
		self.list_of_pronouns = '/home/peejay/python/text_analysis/pronouns.txt'
		self.list_of_verbs = '/home/peejay/python/text_analysis/verbs.txt'
		self.list_of_adjectives = '/home/peejay/python/text_analysis/adjectives.txt'
		self.list_of_adverbs = '/home/peejay/python/text_analysis/adverbs.txt'
		self.list_of_prepositions = '/home/peejay/python/text_analysis/prepositions.txt'
		self.list_of_conjunctions = '/home/peejay/python/text_analysis/conjunctions.txt'
		self.list_of_interjections = '/home/peejay/python/text_analysis/interjections.txt'

	def select_file(self):
		"""Greets the user and ask's for them to input the file path of the file that they wish to analyze."""
		self.text_file = input("Please enter the path of the text file you would like to have analyzed: ")

		return self.text_file

	def nouns(self):
		"""Tells the user how many nouns are in their text file."""
		nouns = 0
		with (self.text_file) open as f:
			f.readline
		for noun in self.list_of_nouns:
			if noun in 