from time import sleep # for personal memory
import random
import pickle # for personal memory
import os # operating system agnostic way to control

### FUNCTIONS ###

# resets terminal window and emulates a perpetual program with a hangman title bar
def hangman_title():

	os.system('clear')

	print("\t*****************************")
	print("\t********** HANGMAN **********")
	print("\t*****************************")

# create list full of possible words and return a random selection from that list
def random_word():

	possible_words = ['alphabet', 'runescape', 'america', 'pie', 'jungle', 'warcraft', 'agent', 'peace']

	return random.choice(possible_words)
# create and return censored display version of word
def flat_word(word):
	flat_word = []
	for letter in word:
		flat_word.append('_')
	
	return flat_word
# print information about word being guessed and display currently deciphered word
def print_word(building_word):
	print("\n\tThe word that you are guessing is:")
	print("\n\t", end = '')
	for letter in building_word:
		print(letter, end = ' ')
	print()
# duplicate to print_word() though used for when word has been fully guessed
def print_word_finished(building_word):
	print("\n\tThe word that you were guessing was:")
	print("\n\t", end = '')
	for letter in building_word:
		print(letter, end = ' ')
	print()
# takes in correctly guessed letter, compares it to hidden word and returns list 
# 	with letter index locations within the word
def guess_letter_correct(letter, word):
	
	locations = []

	for index, item in enumerate(word):
		if letter == word[index]:

			locations.append(index)
			
	return locations
# takes in correctly guessed letter, colleted locations and currently deciphered word 
# 	and reveals guessed letters, returns updated currently deciphered word
def build_word(letter, locations, building_word):

	for number in locations:
		building_word.pop(number)
		building_word.insert(number, letter)
	
	return building_word
# returns true if letter guess is in the word
def guess_letter(guess, word):
	if guess in word:
		return True
	else:
		return False
# asks user for and returns guess
def user_option():
	letter_guess = input("\n\nPlease enter a letter guess (or type 'quit' to end the program): ")
	letter_guess.strip().lower()

	return letter_guess
# displays quit text
def user_quit():
	print("\nThank you for playing HANGMAN!")
# displays error message when user inputs an unrecognizable guess, asks for and returns new guess
def user_guess_unrecognized(bad_guess):
	new_guess = input(f"\nI'm sorry, I didn't recognize your guess of '{bad_guess}', please try again (type 'quit' to end the program): ")
	new_guess.strip().lower() 

	return new_guess
# displays error message when user inputs a duplicate guess, asks for and returns new guess
def duplicate_guess(user_duplicate_guess):
	new_guess = input(f"\nI'm sorry, but you've already guessed '{user_duplicate_guess}', please try again (type 'quit' to end the program:) ")
	new_guess.strip().lower()

	return new_guess
# draws the hangman dependent on current incorrect guesses
def draw_hangman():

	if user_incorrect_guess == 0:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
	elif user_incorrect_guess == 1:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
	elif user_incorrect_guess == 2:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
	elif user_incorrect_guess == 3:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
	elif user_incorrect_guess == 4:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t*************_|**************')
	elif user_incorrect_guess == 5:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t*************_|_*************')
	elif user_incorrect_guess == 6:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_*************')
	elif user_incorrect_guess == 7:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
	elif user_incorrect_guess == 8:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
		print('\t**************|**************')
	elif user_incorrect_guess == 9:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
		print('\t**************|**************')
		print('\t*************/***************')
	elif user_incorrect_guess == 10:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
		print('\t**************|**************')
		print('\t*************/*\\*************')
	elif user_incorrect_guess == 11:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
		print('\t**************|**************')
		print('\t*************/*\\*************')
		print('\t************/****************')
	else:
		print(f'\n\t# of incorrect guesses: {user_incorrect_guess}')
		print('\n\t*****************************')
		print('\t**************|**************')
		print('\t**************|**************')
		print('\t**************O**************')
		print('\t************\\_|_/************')
		print('\t**************|**************')
		print('\t*************/*\\*************')
		print('\t************/***\\************')

### MAIN PROGRAM ###

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_correct_guess = 0
user_incorrect_guess = 0
user_guesses = []
user_incorrect_guesses = []
user_letter_guess = 'a'

building_word = []

word = list(random_word())
building_word = flat_word(word)
print(word)

hangman_title()
print_word(building_word)
draw_hangman()
# initial while loop, ends when user quits or loses after 12 incorrect guesses
while user_letter_guess != 'quit' and user_incorrect_guess != 12 and building_word != word:

	user_letter_guess = user_option()
	
	while user_letter_guess not in alphabet and user_letter_guess != 'quit':
		hangman_title()
		print_word(building_word)
		draw_hangman() 
		user_letter_guess = user_guess_unrecognized(user_letter_guess)

	if user_letter_guess == 'quit':

		user_quit()

	elif guess_letter(user_letter_guess, word):
		locations = guess_letter_correct(user_letter_guess, word)
		building_word = build_word(user_letter_guess, locations, building_word)
		# victory condition
		if building_word == word:
			user_correct_guess = user_correct_guess + 1
			hangman_title()
			print(f"\tYou guessed the correct letter '{user_letter_guess.title()}' and the entire FUCKING word!\n\tWooooord bro, you fuckin' won in {user_correct_guess + user_incorrect_guess} guesses!")
			print_word_finished(building_word)
			draw_hangman()
		else:
			if user_letter_guess not in user_guesses:
				# correct guess
				user_correct_guess = user_correct_guess + 1
				user_guesses.append(user_letter_guess)
				hangman_title()
				print(f"\tYou guessed the correct letter '{user_letter_guess.title()}'!")
				print_word(building_word)
				draw_hangman() 
			else:
				# correct duplicate guess
				hangman_title()
				print(f"\tYou guessed the correct letter '{user_letter_guess.title()}', but you've guessed this letter already!  You okay bud?")
				print_word(building_word)
				draw_hangman()

	else:
		if user_letter_guess not in user_guesses:
			# incorrect guess
			user_incorrect_guess = user_incorrect_guess + 1
			if user_incorrect_guess < 12:
				user_guesses.append(user_letter_guess)
				hangman_title()
				print("\tYou guessed FUCKIN wrong bud!")
				print_word(building_word)
				draw_hangman()
			else: 
				hangman_title()
				print("\tYou guessed FUCKIN wrong bud \n\tand you FUCKIN killed Mr. Hangman!\n\tGame Fuckin OVER!")
				print_word_finished(building_word)
				print("\n\tThe full word was: ", end = '')
				for letter in word:
					print(letter.title(), end = ' ')
				print()
				draw_hangman()
		else:
			# incorrect duplicate guess
			hangman_title()
			print(f"\tYou guessed FUCKIN wrong bud and you already guessed '{user_letter_guess.title()}' already!  You okay bud?")
			print_word(building_word)
			draw_hangman()
















	