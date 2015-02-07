""" Just trying to make a Tarot deck database of course """


import sqlite3

DB = None
CONN = None

tarot_deckF = open("tarot-deck-001.tsv")
tarot_deck_entry = []

# def deck_from_file(f):
# 	for line in f:
# 		tarot_deck_entry = line.rstrip().split("	")
# 		card_name = tarot_deck_entry[0] 
# 		card_meaning = tarot_deck_entry[1] 
# 		card_img = tarot_deck_entry[2]
		
		# return card_name, card_meaning, card_img

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("20150203-tarot-deck-database.db")
    DB = CONN.cursor()
    
def make_new_entry(file_name):
	for line in file_name:
		tarot_deck_entry = line.rstrip().split("	")
		card_id = tarot_deck_entry[0] 
		card_name = tarot_deck_entry[1] 
		card_meaning = tarot_deck_entry[2]
		card_url = tarot_deck_entry[3]
		query = """INSERT into Tarot values (?, ?, ?, ?)"""
		DB.execute(query, (card_id, card_name, card_meaning, card_url))

		CONN.commit()
		print "Successfully added card: %s %s %s"%(card_name, card_meaning, card_url)

def main():
	connect_to_db()
	make_new_entry(tarot_deckF)

	CONN.close()

if __name__ == "__main__":
    main()

# TESTCODE:
# print deck_from_file(tarot_deckF)