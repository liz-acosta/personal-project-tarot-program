"""A very very basic Tarot reading program"""
#Works so far, but there's a bug: Sometimes the First and Second decks return ducplicates.

import random
# import csv


tarot_deckD = {}
new_tarot_deck = []

first_deck = []
second_deck = []

second_draw = []
second_drawD= {}

final_readingList = []
final_reading = []


tarot_deckF = open("tarot-deck-tab.tsv")

# FIXTHIS01: How do I write this to a new file in the desired format?
# new_tarot_deckF = csv.writer(open('new-tarot-deck.tsv', 'wb'))

for line in tarot_deckF:
	card = line.rstrip().split("	")

	tarot_deckD[card[0]] = card[1]

for k, v in tarot_deckD.items():
        new_tarot_deck.append(tarot_deckD[k])
        for line in new_tarot_deck:
                new_tarot_line = line.rstrip().split(": ")
                del new_tarot_line[0]
                tarot_deckD[k] = ' '.join(new_tarot_line)

# FIXTHIS: See FIXTHIS01, refers to code below
# for key, value in tarot_deckD.items():
#         new_tarot_deckF.writerow([key, value])

for i in range(39):
	draw_card = random.choice(tarot_deckD.keys())
	if draw_card not in first_deck:
		first_deck.append(draw_card)

for k, v in tarot_deckD.items():
	if k not in first_deck:
		second_deck.append(k)

#TESTCODE:
# print first_deck
# print len(first_deck)
# print
# print second_deck
# print len(second_deck)
print
print

print raw_input("Welcome to the 2-5-3 Tarot Reading." '\n' "In this type of reading, you'll be asked to select from a shuffled cut deck." '\n' "From that selection, five cards will be drawn for you to select your final three cards from." '\n' "Press enter to continue with your reading >"
        )

print raw_input("A deck of 78 cards is shuffled and cut." '\n' "Before you are two decks of cards." '\n' "Trust your insticts and select the deck that calls to you," '\n' " following the instructions and capitalization exactly." '\n' "(Tarot is, after all, a precise science.)" '\n' "Press enter to continue >"
        )

print

deck_selection1 = raw_input(str("Select your deck by typing either First Deck or Second Deck >"))

if deck_selection1 == "First Deck":
        deck_selection1 = first_deck
else:
        deck_selection1 = second_deck

for i in range(5):
        draw_card = random.choice(deck_selection1)
        second_draw.append(draw_card)

print
print

print raw_input("From the deck you select, five cards are drawn" '\n' "and laid before you face down." '\n' "What kind of destiny do they foretell?" '\n' "Trust your instincts and select the three cards" '\n' "that speak the strongest to you." '\n' "Follow the instructions and capitalization precisely." '\n' "(Since, after all, Tarot's grasp of Python isn't as good as its grasp on the future.)" '\n' "Press enter to continue >")

# TESTCODE:
# print second_draw

second_drawList = ['First Card', 'Second Card', 'Third Card', 'Fourth Card', 'Fifth Card']

# print second_drawList

second_drawD = dict(zip(second_drawList, second_draw))

#TESTCODE:
# print second_drawD

deck_selection2 = raw_input(str("Select your first final card by typing either First Card, Second Card, Third Card, Fourth Card, or Fifth Card >"))

final_readingList.append(deck_selection2)

deck_selection2 = raw_input(str("Select your second final card by typing either First Card, Second Card, Third Card, Fourth Card, or Fifth Card >"))

final_readingList.append(deck_selection2)

deck_selection2 = raw_input(str("Select your third and last final card by typing either First Card, Second Card, Third Card, Fourth Card, or Fifth Card >"))

final_readingList.append(deck_selection2)

print
print

print "The cards have spoken. Your destiny lies before you." '\n' "Remember! The cards tell no lies:"

print

# print final_readingList

for item in final_readingList:
        k = second_drawD[item]
        print k, ":", tarot_deckD[k]

print
print 
