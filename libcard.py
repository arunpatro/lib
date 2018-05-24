import random

class Card(object):
	"""docstring for Card"""
	def __init__(self, suite, value):
		super(Card, self).__init__()
		self.suite = suite
		self.value = value
		
class Deck(object):
	"""docstring for Deck"""
	cards = []
	def __init__(self, seed=0):
		super(Deck, self).__init__()
		for i in ['spade', 'club', 'heart', 'diamond']:
			for j in range(1, 14):
				self.cards.append(Card(i, j))
		random.seed(seed)
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()

	def shuffle(self, seed):
		random.seed(seed)
		random.shuffle(self.cards)

		


