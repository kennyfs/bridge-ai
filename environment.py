import numpy as np
import my_config
import player
class Card:
	def __init__(self, suit, num):
		self.suit = suit#0:spade, 1:heart, 2:diamond, 3:club
		self.num = num#0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:8, 7:9, 8:T, 9:J, 10:Q, 11:K, 12:A
	def __str__(self):
		return {0: 'S',1: 'H',2: 'D',3: 'C'}[self.suit]+{0: '2',1: '3',2: '4',3: '5',4: '6',5: '7',6: '8',7: '9',8: 'T',9: 'J',10: 'Q',11: 'K',12: 'A'}[self.num]
class Deck:
	def __init__(self, shuffle:bool=True):
		self.cards = []
		for i in range(4):
			for j in range(13):
				self.cards.append(Card(i, j))
		if shuffle:
			self.shuffle()
	def shuffle(self):
		np.random.shuffle(self.cards)
class Environment:
	def __init__(self, config:my_config.Config, players:list=None, deck:Deck=None, info:dict=None):
		if players is None:
			self.players = []
		else:
			self.players = players
			#list of player.Player
		self.config = config
		self.deck = Deck() if deck is None else deck
		self.dummy=info['dummy']
		self.dealer=info['dealer']
	def get_features(self, player_index:int):
		ret=np.zeros((4,2,4,13), dtype=np.float32)
		for i in range(4):
			ret[(player_index+i)%4,:,:,:] = self.players[player_index].get_features()
		return ret
		#unfinished