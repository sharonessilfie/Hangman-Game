import random
from words import words
import string


#this allows the random module to pick a valid word with no white spaces pr hyphens
def get_valid_word(words):
    word = random.choice(words) #randomly chooses words from the list of words
    
    while "-" in word or " " in word: 
        word = random.choice(words) #stores the word that will be picked
        print(word)

    return word.upper()

#word_letters = set(word)

def hangman():
    word1= get_valid_word(words)
    word_letters = set(word1) #stores the letters in a word in a set
    alphabet = set(string.ascii_uppercase) #gives you all the english alphabets in uppercase
    used_letters = set() #stores the letters the user has guessed
    
    lives = 6 

    #taking in user input
    while len(word_letters) > 0 and lives > 0: #conditions on which the user can keep playing
        #letters used
        print("You have used these letters: ", " ".join(used_letters))
        print("You have", lives, "lives left")
    
    

        #what the word the user is supposed to guess is
        word_list = [letter if letter in used_letters else "-" for letter in word1]
        print("Current word: ", " ".join(word_list))
    
    
        user_letter = input("Guess a letter!: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")
            else:
                lives = lives - 1 #takes waya a life wrong
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("Already used")

        else:
            print("Invalid entry")
        

    if lives == 0:
        print("You died, sorry. The word was", word1)
    else:
        print("You guessed the word corrcetly!!")


if __name__ == "__main__":
    hangman()
