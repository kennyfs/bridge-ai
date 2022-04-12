
import numpy as np
from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
	def __init__(self, cards=None, onboard=None):
		if cards is None:
			self.cards = []
		else:
			self.cards = cards
		if onboard is None:
			self.onboard = None
	def get_features(self):
		ret=np.zeros((2,4,13), dtype=np.float32)
		for card in self.cards:
			ret[0][card.suit][card.num]=1.
		if self.onboard is not None:
			ret[1][self.onboard.suit][self.onboard.num]=1.
		return ret
