# Philip Ruggirello 1/12/21

from collections import Counter

class Analyzer:
	"""This will be the analyzer onbject whihc will contains the mehtods for the different ways the inputed txt file can be analyzed."""
	def __init__(self):
		"""Conatins the attributes of the analyzer object."""
		self.list_of_nouns = '/home/peejay/python/text_analysis/dictionaries/nouns.txt'
		self.list_of_pronouns = '/home/peejay/python/text_analysis/dictionaries/pronouns.txt'
		self.list_of_verbs = '/home/peejay/python/text_analysis/dictionaries/verbs.txt'
		self.list_of_adjectives = '/home/peejay/python/text_analysis/dictionaries/adjectives.txt'
		self.list_of_adverbs = '/home/peejay/python/text_analysis/dictionaries/adverbs.txt'
		self.list_of_prepositions = '/home/peejay/python/text_analysis/dictionaries/prepositions.txt'
		self.list_of_conjunctions = '/home/peejay/python/text_analysis/dictionaries/conjunctions.txt'
		self.list_of_interjections = '/home/peejay/python/text_analysis/dictionaries/interjections.txt'

	def select_file(self):
		"""Greets the user and ask's for them to input the file path of the file that they wish to analyze."""
		self.text_file = input("Please enter the path of the text file you would like to have analyzed: ")

		return self.text_file

	def how_many_nouns(self):
		"""Tells the user how many nouns are in their text file."""
		words_from_story = []
		nouns_in_list = []
		nouns = 0
		contained = []
		with open(self.text_file) as f:
			for line_of_book in f:
				for word in line_of_book.split():
					words_from_story.append(word.strip())
		with open(self.list_of_nouns) as n:
			for line_of_list in n:
				for noun in line_of_list.split():
					nouns_in_list.append(noun.strip())

		c1 = Counter(words_from_story)
		c2 = Counter(nouns_in_list)

		intersections = { k: c1[k] * c2[k] for k in c1.keys() & c2.keys() }

		for key, value in intersections.items():
			print(f"{key}: {value}")

if __name__ == '__main__':
	a = Analyzer()
	a.select_file()
	a.how_many_nouns()