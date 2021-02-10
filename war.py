from random import sample
from itertools import product

class War():
	"""A class to simulate the class card game war"""
	def __init__(self):
		card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		suit_symbols = ['♠','♦','♥','♣']
		self.deck_of_cards = list(product(card_values, suit_symbols))
		self.relevent_card_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

		print('Welcome to WAR!!')
		print('A Cody Brooks Python Program')
		print('Without further delay, lets shuffle and deal!')

	def game_loop(self):

		player_hand, cpu_hand = self.shuffle_and_deal()
		player_score, cpu_score = 0, 0
		i = 0
		hand_value = 1 # Increases in the event of a tie

		while i < 26:
			player_card, cpu_card = self.draw_off_top_of_deck(i, player_hand, cpu_hand)

			lay_down_cards = input("Hit Enter to lay down cards or 'q' to quit  ")
			if lay_down_cards == 'q': 
				break

			if hand_value > 1: 
				self.tie_visiual(player_card, cpu_card)
				winner = self.who_gets_the_point(player_card, cpu_card)
				self.tie_break(player_old_card, cpu_old_card, player_card, cpu_card, winner)
			else: 
				self.war_round_visiual(player_card, cpu_card)
				winner = self.who_gets_the_point(player_card, cpu_card)

			if winner == 1:
				player_score += hand_value
				if hand_value > 1:
					hand_value = 1
				print('You win that round')
			elif winner == 0:
				cpu_score += hand_value
				if hand_value > 1:
					hand_value = 1 
				print('The computer wins that round')
			else: 
				print('We got a tie')
				print('Play your next three cards face down')
				player_old_card = player_card
				cpu_old_card = cpu_card


			if winner == 'TIE' and i <= 22:
				hand_value += 3
				i += 3
			elif winner == 'TIE':
				hand_value = 25 - i
				i = 25
			else: 
				i += 1

		if player_score > cpu_score:
			print('You beat the computer. Nice Work.')
			print(f'Final Score: Player 1 - {player_score}  Computer - {cpu_score}')
		elif player_score == cpu_score:
			print('Tie Game. Everyone Wins?')
			print(f'Final Score: Player 1 - {player_score}  Computer - {cpu_score}')
		else: 
			print('You Lose. You bring shame to your dojo.')
			print(f'Final Score: Player 1 - {player_score}  Computer - {cpu_score}')

		play_again = input("Play again 'y' or 'n':  ")
		if y:
			self.game_loop()

	def shuffle_and_deal(self):
		"""Randomly shuffles a deck of cards and splits it into two hands"""
		shuffled_deck = sample(self.deck_of_cards, len(self.deck_of_cards))
		return (shuffled_deck[:26], shuffled_deck[26:])

	def draw_off_top_of_deck(self, i, player_hand, cpu_hand):
		return player_hand[i], cpu_hand[i]


	def who_gets_the_point(self, player_card, cpu_card):
		try:
			player_card_value = int(player_card[0])
		except ValueError:
			player_card_value = self.relevent_card_values[player_card[0]]
		try: 
			cpu_card_value = int(cpu_card[0])
		except ValueError: 
			cpu_card_value = self.relevent_card_values[cpu_card[0]]

		if player_card_value == cpu_card_value:
			return 'TIE'
		elif player_card_value > cpu_card_value:
			return 1
		else: 
			return 0

	def war_round_visiual(self, card1, card2):
		if card1[0] in '23456789JKQA':
			x = " "
		else:
			x = ''
		
		if card2[0] in '23456789JKA':
			y = '  '
		else:
			y = ' '

		print('╔════════════╗          ╔════════════╗')
		print('║ {}     {}    ║          ║ {}  {}      ║'.format(card1[0], x, card2[0], y))
		print('║ {}          ║          ║ {}          ║'.format(card1[1], card2[1]))
		print('║            ║          ║            ║')
		print('║      {}     ║  vrs.    ║      {}     ║'.format(card1[1], card2[1]))
		print('║            ║          ║            ║')
		print('║          {} ║          ║          {} ║'.format(card1[1], card2[1]))
		print('║      {}   {} ║          ║          {} ║'.format(x ,card1[0], card2[0]))
		print('╚════════════╝          ╚════════════╝')
		print('  Your Card             Computers Card')

	def tie_visiual(self, player1, cpu1):
		print('╔════════════╗             ╔════════════╗')
		print('║ {}╔════════════╗          ║ {}╔════════════╗'.format(player1[0], cpu1[0]))
		print('║ {}║░░░░░░░░░░░░║   To     ║ {}║░░░░░░░░░░░░║'.format(player1[1], cpu1[1]))
		print('║  ║▒▒▒▒▒▒▒▒▒▒▒▒║   The    ║  ║▒▒▒▒▒▒▒▒▒▒▒▒║')
		print('║  ║░░░░░░░░░░░░║  Victor  ║  ║░░░░░░░░░░░░║')
		print('║  ║▒▒▒▒▒▒▒▒▒▒▒▒║   Goes   ║  ║▒▒▒▒▒▒▒▒▒▒▒▒║')
		print('║  ║░░░░░░░░░░░░║   The    ║  ║░░░░░░░░░░░░║')
		print('║  ║▒▒▒▒▒▒▒▒▒▒▒▒║  Spoils  ║  ║▒▒▒▒▒▒▒▒▒▒▒▒║')
		print('╚══║░░░░░░░░░░░░║          ╚══║░░░░░░░░░░░░║')
		print('   ╚════════════╝             ╚════════════╝')

def tie_break(player1, cpu1, player2, cpu2, winner):
	if winner == 1:
		x = " "
		y = ' WIN'
	elif winner == 'TIE':
		x = ' '
		y = ' TIE'
	else:
		x = ' '
		y = 'LOSS'

	print('╔════════════╗             ╔════════════╗')
	print('║ {}╔═╔═══════════╗         ║ {}╔═╔═══════════╗'.format(player1[0], cpu1[0]))
	print('║ {}║░║ {}         ║         ║ {}║░║ {}         ║'.format(player1[1], player2[0], cpu1[1], cpu2[0]))
	print('║  ║▒║ {}         ║   A     ║  ║▒║ {}         ║'.format(player2[1], cpu2[1]))
	print('║  ║░║           ║   BIG   ║  ║░║           ║')
	print('║  ║▒║     {}     ║ {} {}  ║  ║▒║     {}     ║'.format(player2[1], x, y, cpu2[1]))
	print('║  ║░║           ║         ║  ║░║           ║')
	print('║  ║▒║         {} ║         ║  ║▒║         {} ║'.format(player2[1], cpu2[1]))
	print('╚══║░║         {} ║         ╚══║░║         {} ║'.format(player2[0], cpu2[0]))
	print('   ╚═╚═══════════╝            ╚═╚═══════════╝')


if __name__ == "__main__":
	WAR = War()
	WAR.game_loop()

