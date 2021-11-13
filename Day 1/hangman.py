from os import waitpid
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    cnt = 0
    for word in secret_word:
        if word in letters_guessed:
            #print(word+" contains in the string")
            cnt += 1
    if cnt == len(secret_word):
        return True
    return False
    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    i = ""
    for word in secret_word:
      if word not in letters_guessed:
        i = i+"_"
      else:
          i = i + word
    
    if i == "_____":
      i = "_ _ _ _"
        
    return i
 



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    a = string.ascii_lowercase
    if letters_guessed == 0:
        return a
    
    for i in letters_guessed:
        a = a.replace(i,"")
    return a





def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Starting Info
    guess = 6
    letters_guessed = []
    word = "_ _ _ _"
    warn = 3
    vowels = ["a","i","o","e"]
    
    
    print("Welcome to the game Hangman\n"+"I am thinking of a word that is",len(secret_word),"letters long.\n" + "You have 3 warnings left\n")
    
    # Game Loop
    while(guess>0):
      #prints main info for the user
      print("-------------\n" + f"You have {guess} guesses left.\n"+"Available letters :",get_available_letters(letters_guessed))
      word = ""
      word = input("Please guess a letter : ")
      
      
      # Decrement Warning or Guesses if word is not a character
      if str.isalpha(word) == False:
        if warn == 0:
            guess -= 1
            print("All of your warning have lost, Taking one from the guesses\n")
            continue
        warn -= 1 
        print(f"Oops! That is not a valid letter. You have {warn} warnings left\n")
        continue
      
      word = str.lower(word)
      
      #If the vowel hasn’t been guessed and the vowel is not in the secret
      ## word, the user loses two guesses. Vowels are a, e, i , o, and u. y does not
      ### count as a vowel.
      if word in vowels and word not in secret_word:
        print("You have guessed a vowel that is not in my word, Taking 2 guesses\n")
        guess -= 2
        continue
      main_Word = word
      # If the word has been typed before
      if main_Word in letters_guessed:
        if warn == 0:
            guess -= 1
            print("All of your warning have lost, Taking one from the guesses\n")
            continue
        warn -= 1
        print(f"Oops! You've already guessed that letter. You now have {warn} warnings left:",main_Word)
        continue
      
      
      
      letters_guessed.append(main_Word)
      
      
      # Breaks the loop if the word has been guessed
      if is_word_guessed(secret_word,letters_guessed) == True:
        total_score = len(set(secret_word)) * guess
        print("------------\n"+"Congratulations, you won!")
        print("Your total score for this game :",total_score)
        break
      
      # Gives feedback to the user by printing If the word is one of the letters of secret_word or not
      if main_Word in secret_word:
        print("Good Guess :", get_guessed_word(secret_word,letters_guessed))
      else : print("Oops! That letter is not in my word:",main_Word)
      
      guess -= 1
      
      
    # Print the 'Lost Msg' -> If user hasn't been able to guess the word
    if guess == 0 and is_word_guessed(secret_word,letters_guessed) == False:
      print("Sorry, you ran out of guesses. The word was",secret_word+".\n")  



if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)

