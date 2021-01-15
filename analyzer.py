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
		self.done = False

	def analyze(self):
		"""Process for text analysis."""
		self.select_file()
		while self.done == False:
			info = input("What would you like to know about this story?: (Word Count/Noun Count) ")
			if info == "Word Count":
				self.word_count()
			elif info == "Noun Count":
				self.noun_count() 

			keep_going = input("Would you like to get more information?: (Yes/No) ")
			if keep_going == "No":
				self.done = True


	def select_file(self):
		"""Greets the user and ask's for them to input the file path of the file that they wish to analyze."""
		self.text_file = input("Please enter the path of the text file you would like to have analyzed: ")

		self.words_from_story = []

		with open(self.text_file) as f:
			for line_of_book in f:
				for word in line_of_book.split():
					self.words_from_story.append(word.strip())

		return self.words_from_story

	def word_count(self):
		"""Tells the user how many words are in their text file."""
		length = len(self.words_from_story)

		print(f"There are {length} words in the story.")


	def noun_count(self):
		"""Tells the user how many nouns are in their text file."""
		nouns_in_list = []

		with open(self.list_of_nouns) as n:
			for line_of_list in n:
				for noun in line_of_list.split():
					nouns_in_list.append(noun.strip())

		print("These are the nouns used in the sotry, as well as how many times they are each used:\n")

		self.counter(nouns_in_list, self.words_from_story)

	def counter(self, list1, list2):
		"""Shows the common elements as well as how many tiems they were seen."""
		c1 = Counter(list1)
		c2 = Counter(list2)

		intersections = { k: c1[k] * c2[k] for k in c1.keys() & c2.keys() }

		for key, value in intersections.items():
			print(f"{key}: {value}")

if __name__ == '__main__':

	a = Analyzer()
	a.analyze()