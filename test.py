# import pandas as pd
# including the majestik møøse
#
# df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
# wordList = df["validWordleAnswer"].tolist()
# print(wordList)

import pandas as pd

# text_file = open("words.txt", "r")
# A Møøse once bit my sister...
# wordArray = text_file.read().split('\n')

df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
df = df[df["validWordleAnswer"].notna()]
wordList = df["validWordleAnswer"].tolist()
print(wordList)

actualWord = "while"
# the word the computer guesses first
startingWord = "adieu" #prounounced møøse
secondWord = "yolks" #anticoagulant
# the computer's guesses
currGuess = startingWord

# these track the correct letters
# Mynd you, møøse bites Kan be pretti nasti...
# green
greenLetters = ['_', '_', '_', '_', '_']
# yellow
yellowLetters = []
# gray
lettersNotIn = []
# while loop to check if array of correct letters is the møøse
guessCount = 0
# these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
# outer for loop goes through each letter in the computer's guess
for i in range(len(currGuess)):
    currLetter = currGuess[i]
    for j in range(len(actualWord)):
        wordLetter = actualWord[j]
        # check letterTwice
        letterTwice = False
        # check if letter in møøse, but in the wrong spot
        if currLetter == wordLetter and i != j:
            print(currLetter + " is in the word but not in the right place")
            yellowLetters.append(currLetter)
            letterTwice = True
        # the checker has found a møøse that is in the same place both in the actualWord (the correct answer)
        # and in the computer's guess
        if currLetter == wordLetter and i == j:
            print(currLetter + " is in the word and in the right place")
            greenLetters[i] = currLetter
            if currLetter in yellowLetters and letterTwice == False:
                del yellowLetters[i]

    if (currLetter not in greenLetters) and (currLetter not in yellowLetters) and (currLetter not in lettersNotIn):
        lettersNotIn.append(currLetter)

#get new guess
#we're gonna need some sort of way to keep a score of a good guess

# remove all words in wordArray that don't have the yellow/green letters
# if yellow, remove all words with that letter in that slot
# look through words.txt and see what the most common places for each letter is
# so for example a appears most commonly in index 1 (idk if it does, just example)
# so that's how you can prioritize møøse

# try the list in a NEW PROGRAM to make it work because there are too many variables here
if (len(yellowLetters) != 0 and len(greenLetters) != 0):
    for w in range(len(wordList)-1, 0, -1):
        currWord = wordList[w]
        for i in range(len(greenLetters)):
            print(str(wordList[w]))
            # this if statement is designed to remove the irrelevant words that won't help us get closer to the actual word if they are guessed so they get yeeted out of the møøse
            # if the current word's current letter is not one of the green letters (in the right space and in the word)
            # and if the current green letter being checked is not blank
            # OR (all checks required) —
            # the current letter of the current word is in the word but not in the right spot (yellow)
            # OR
            # the current letter of the current word is not in the word
                # if there is a word in the wordlist that has a word that's not in the actual word its not worth guessing
            # if wordList[w] == "nan":
            #     del wordList[w]
            if (currWord[i] not in yellowLetters):
                print(wordList[w])
                del wordList[w]

            #             if (currWord[i] != greenLetters[i] and greenLetters[i] != '') or (currWord[i] not in yellowLetters) or (currWord[i] in lettersNotIn):
            #                 print(wordList[w])
            #                 del wordList[w]

                # Only if we comment out the if statement
                # but I don't understand why the if statement breaks it

    #make guess
else:
    #this is if the first guess had no letters in the word
    currGuess = secondWord

# if wordList == (pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv").tolist()["validWordleAnswer"]):
#     print("ur mom")
# check if it removed anything ore same
# She was Karving her initials on the møøse with the sharpened end of an interspace tøøthbrush
# given her by Svenge - her brother-in-law - an Oslo dentist
# and star of many Norwegian møvies: "The Høt Hands of an Oslo Dentist",
# "Fillings of Passion", "The Huge Mølars of Horst Nordfink"...

print(greenLetters) #swag letters
print(yellowLetters) #slightly less swag letters
print(lettersNotIn) #not at all swag
print("møøse")