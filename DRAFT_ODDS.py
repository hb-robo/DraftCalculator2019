import operator
import random

def generate_odds():
	draft_odds = []
	for i in range(22):
		draft_odds.append(8)
	for i in range(168):
		draft_odds.append(7)
	for i in range(257):
		draft_odds.append(6)
	for i in range(72):
		draft_odds.append(5)
	for i in range(115):
		draft_odds.append(4)
	for i in range(119):
		draft_odds.append(3)
	for i in range(122):
		draft_odds.append(2)
	for i in range(125):
		draft_odds.append(1)
	return draft_odds		

def generate_pick(pos, picks):
	

	# adds draft pick to 
	if pick in picks.keys():
		picks[pick] += 1
	else:
		picks[pick] = 1

def main():	
	picks = {}
	odds = generate_odds();
	for pos in odds:
		pick = generate_pick(pos, picks)
	
	sorted_odds = sorted(picks.items(), key=operator.itemgetter(1), reverse=True)

	i = 1
	for key, value in sorted_odds:
		print("#%d: %s - %d" % (i, key, value)) 
		i += 1

main()
