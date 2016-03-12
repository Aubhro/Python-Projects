"""
This program decodes simple shift ciphers. 
Shift means that all the letters in the message shift a certain number of letters away to a new letter.

Created by Aubhro Sengupta
"""

import enchant
d = enchant.Dict("en_US")

#Initializes array with the letters of the alphabet in order
numArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Takes user input as a string
message = raw_input('Enter code \n')    
message = message.lower()
message = message.split()



def word(code):
	#Turns string into a list for better manipulation
	code = list(code)

	#Creates copy of code to decode
	decode = code		
 
	#Shifts to every letter of the alphabet
	for alphabetnum in range(26):

		#Changes the word to shifted word letter by letter
		for pos in range(len(code)):
		
			#Gets character in the specified position of the word listed in the second for loop
			char = code[pos]
					
			#Determines the character's place in the array above
			shift = numArray.index(char)
		
			#Shifts index value by the specified value in the first for loop  
			shift = shift + alphabetnum
		
			if shift > 25:
				shift = shift - 25
			
			#Finds the character at the newly shifted index
			char = numArray[shift]
		
			#Changes old character to the newly shifted character in new string
			decode[pos] = char
			shift = 0
		
		
		
		#Turns array back into the list to check if it is a word	
		decode = "".join(decode)
		
		if d.check(decode):
			shift = alphabetnum
			#print 'Code Solved!!!!!!!!!!!!!!!'
			return decode
		decode = list(decode)
	
def sort(code): 
	handlen = len(code[0])
	hand = code[0]
	for index in range(len(code)):
		for pos in range(len(code)-index):
			print hand
			pos = pos+index
			if handlen < len(code[pos]):
				hand = code[pos]
			pos = pos - index
		handlen = 0
		code[index] = hand
	return code



print sort(message)	
for wordpos in range(len(message)):
	print word(message[wordpos])