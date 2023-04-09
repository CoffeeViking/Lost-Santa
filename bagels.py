import random

NUM_DIGITS = 5 # (!) Try changing this to 1 or 10
MAX_GUESSES = 3 # (!) Try setting this to 1 or 100

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {} digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the correct position.
Bagels          No digit is correct.

For example, if the secret number is 248 and you guess 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True: # Main Game Loop
        # This stores the secret number to be guessed.
        secretNum = getSecretNum()
        print('I have thought up a code of 1-9 and A-J.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep Looping until they enter a valid guess
            while len(guess) != NUM_DIGITS:
                print('Guess #{}: '.format(numGuesses))
                guess = list(input('> '))
            for i in guess:
                if i > 'j':
                    print('Guess #{}: '.format(numGuesses))
                    guess = list(input('> '))

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're Correct so break the loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for Playing!')

def getSecretNum():
    # Returns a string made up of NUM_DIGITS uniquee random digits
    numbers = list('0123456789abcdefghij') # Create a list of 1-9
    random.shuffle(numbers) # Shuffle them in random order
    
    # Get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    # Returns string with the pico, fermi, bagels clues
    if guess == secretNum:
        return 'You got it!'
   
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit in a correct place
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            #A correct digit in the wrong place
            clues.append('Pico ')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits
    else:
        #Sort clues into alphabetical order so the original order doesn't give it away
        clues.sort()
        # Make a single string from the list of clues
        return ''.join(clues)

# If the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()
