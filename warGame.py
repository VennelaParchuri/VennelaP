import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three':3, 'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9, 'Ten':10,'Jack':11,'Queen':12,
			'King':13,'Ace':14}

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit,rank)
				self.deck.append(card)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal_one(self):
		return self.deck.pop()


class Player:
	def __init__(self,name):
		self.name = name
		self.playerCards = []

	def playOneCard(self):
		return self.playerCards.pop(0)

	def takeCards(self,newCards):
		if type(newCards) == type([]):
			self.playerCards.extend(newCards)
		else:
			self.playerCards.append(newCards)
	def __str__(self):
		return f'Player {self.name} has {len(self.playerCards)} cards'




player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
	player_one.takeCards(new_deck.deal_one())
	player_two.takeCards(new_deck.deal_one())


game_on = True
round_num = 0

while game_on:
	round_num+=1
	print(f'Round {round_num}')

	if len(player_one.playerCards) == 0:
		print(f"There are no cards with player {player_one.name}, Game Over, {player_two.name} has won ")
		game_on = False
		break
	if len(player_two.playerCards) == 0:
		print(f"There are no cards with player {player_two.name}, Game Over, {player_one.name} has won ")
		game_on = False
		break

	player_one_cards = []
	player_one_cards.append(player_one.playOneCard())
	player_two_cards = []
	player_two_cards.append(player_two.playOneCard())

	playing= True

	while playing:

		if player_one_cards[-1].value > player_two_cards[-1].value:
			player_one.takeCards(player_one_cards)
			player_one.takeCards(player_two_cards)
			playing= False

		elif player_one_cards[-1].value < player_two_cards[-1].value:
			player_two.takeCards(player_one_cards)
			player_two.takeCards(player_two_cards)
			playing= False
		else:

			print("Cards are equal")
			if(len(player_one.playerCards))< 5:
				print(f"There are no cards with player {player_one.name}, Game Over, {player_two.name} has won ")
				game_on = False
				break
			elif(len(player_two.playerCards))<5:
				print(f"There are no cards with player {player_two.name}, Game Over, {player_one.name} has won ")
				game_on = False
				break
			else:
				for i in range(5):
					player_one_cards.append(player_one.playOneCard())
					player_two_cards.append(player_two.playOneCard())





