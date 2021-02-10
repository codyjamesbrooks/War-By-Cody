from itertools import product

def war_round_visiual(card1, card2):
	if card1[0] in '23456789JKQA':
		player_rank = card1[0] + ' '
		y = ' ' 
	else: 
		player_rank = card1[0]
		y= ''
	if card2[0] in '23456789JQKA':
		cpu_rank = card2[0] + ' '
		x = ' '
	else:
		cpu_rank = card2[0]
		x = ''

	print('╔════════════╗          ╔════════════╗')
	print('║ {}         ║          ║ {}         ║'.format(player_rank, cpu_rank))
	print('║ {}          ║          ║ {}          ║'.format(card1[1], card2[1]))
	print('║            ║          ║            ║')
	print('║      {}     ║  vrs.    ║      {}     ║'.format(card1[1], card2[1]))
	print('║            ║          ║            ║')
	print('║          {} ║          ║          {} ║'.format(card1[1], card2[1]))
	print('║    {}     {} ║          ║    {}     {} ║'.format(y, player_rank.rstrip(),x, cpu_rank.rstrip()))
	print('╚════════════╝          ╚════════════╝')
	print('  Your Card             Computers Card')

def tie_visiual(player1, cpu1):
	if player1[0] == '10':
		play_view = '1'
	else:
		play_view = player1[0]
	if cpu1[0] == '10':
		cpu_view = '1'
	else:
		cpu_view = cpu1[0]	
	print('╔════════════╗             ╔════════════╗')
	print('║ {}╔════════════╗          ║ {}╔════════════╗'.format(play_view, cpu_view))
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

	play1view, play2view = player1[0], player2[0]
	cpu1view, cpu2view = cpu1[0], cpu2[0]
	if player1[0] == '10':
		play1view = '1'
	if cpu1view == '10':
		cpu1view = '1'
	if play2view == '10':
		k = ""
	else:
		k = ' '

	if cpu2view == '10':
		z = ''
	else:
		z = ' '
	print('╔════════════╗             ╔════════════╗')
	print('║ {}╔═╔═══════════╗         ║ {}╔═╔═══════════╗'.format(play1view, cpu1view))
	print('║ {}║░║ {}  {}      ║         ║ {}║░║ {}    {}    ║'.format(player1[1], play2view, k, cpu1[1], cpu2view, z))
	print('║  ║▒║ {}         ║   A     ║  ║▒║ {}         ║'.format(player2[1], cpu2[1]))
	print('║  ║░║           ║   BIG   ║  ║░║           ║')
	print('║  ║▒║     {}     ║ {} {}  ║  ║▒║     {}     ║'.format(player2[1], x, y, cpu2[1]))
	print('║  ║░║           ║         ║  ║░║           ║')
	print('║  ║▒║         {} ║         ║  ║▒║         {} ║'.format(player2[1], cpu2[1]))
	print('╚══║░║     {}   {} ║         ╚══║░║     {}   {} ║'.format(k, play2view, z, cpu2view))
	print('   ╚═╚═══════════╝            ╚═╚═══════════╝')

card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit_symbols = ['♠','♦','♥','♣']
deck_of_cards = list(product(card_values, suit_symbols))






