'''
#bagels :
In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues.

 The game offers one of the following hints in response to your guess:
  Pico” when your guess has a correct digit in the wrong place, 
  Fermi” when your guess has a correct digit in the correct place, and 
  Bagels” if your guess has no correct digits.
   You have 10 tries to guess the secret number.


#The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
# It encrypts letters by shifting them over by a certain number of places in the alphabet.
#  We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on.
#  To decrypt the message, you must shift the encrypted letters in the opposite direction. 
# This program lets the user encrypt and decrypt messages according to this algorithm. 
example : 

Do you want to (e)ncrypt or (d)ecrypt? e
Please enter the key (0 to 25) to use. 4
Enter the message to encrypt. Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.'''

'''
string = 123
input =
if input matche sstring return fermi ( all true)
if input not in string return bagels
if input is in string return pico

#https://pastebin.com/69p0X7Qp
#https://www.reddit.com/r/learnpython/comments/6sv7mw/help_improve_my_bagels_games_code/
#https://inventwithpython.com/invent4thed/chapter11.html

'''
import random

NUM_DIGITS = 3

def getSecretNum():
    numbers = list(range(10))
    print(f'{ numbers=  }')
    random.shuffle(numbers)
    print(f'{ numbers=  }')

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])# cant concat integers
    return secretNum

print(getSecretNum())