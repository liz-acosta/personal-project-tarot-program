import random
import sqlite3

song_lyrics = open("riding-with-the-ghost.txt")

song = []
reading = []

def connect_to_db():
	
	conn = sqlite3.connect("tarot-deck.db")
	cursor = conn.cursor()

	return cursor

def make_lyrics(filename):

	for line in filename:
		each_verse = line.rstrip().split(" ")
		for each_word in each_verse:
			song.append(each_word)

	return song


def how_many_draws(lyrics, word):
	
	if not lyrics:
		return 0
	
	else:
		if lyrics[0] == word:
			return 1 + how_many_draws(lyrics[1:], word) 
		else:
			return 0 + how_many_draws(lyrics[1:], word)

def tarot_draw(draws):

	print range(draws)

	cursor = connect_to_db()

	for i in range(draws):

		print "THIS", i
		
		draw = random.randint(1,78)

		print draw
		
		query = """SELECT card_name FROM Tarot WHERE card_id = ?"""
		
		cursor.execute(query, (draw,))

		card = cursor.fetchone()
	
		reading.append(card)

	return reading

def main():
	connect_to_db()
	return tarot_draw(how_many_draws(make_lyrics(song_lyrics), "change"))

if __name__ == "__main__":
    main()

print main()