import pandas as pd

# text_file = open("words.txt", "r")
# wordArray = text_file.read().split('\n')

wordArray = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
wordList = wordArray["validWordleAnswer"].tolist()
wordList = [w for w in wordList if w != "nan"]
print(wordList)

actualWord = "which"
# the word the computer guesses first
startingWord = "adieu" #prounounced addy-ow
secondWord = "yolks" #anticoagulant
# the computer's guesses
currGuess = startingWord

#these track the correct letters
# green
greenLetters = ['', '', '', '', '']
# yellow
yellowLetters = []
# gray
lettersNotIn = []
# while loop to check if array of correct letters is the word
guessCount = 0
while (actualWord != "".join(greenLetters)) or guessCount < 6:
    # these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
    # outer for loop goes through each letter in the computer's guess
    for i in range(len(currGuess)):
        currLetter = currGuess[i]
        for j in range(len(actualWord)):
            wordLetter = actualWord[j]
            # check letterTwice
            letterTwice = False
            # check if letter in word, but in the wrong spot
            if currLetter == wordLetter and i != j:
                print(currLetter + " is in the word but not in the right place")
                yellowLetters.append(currLetter)
                letterTwice = True
            # the checker has found a letter that is in the same place both in the actualWord (the correct answer)
            # and in the computer's guess
            if currLetter == wordLetter and i == j:
                print(currLetter + " is in the word and in the right place")
                greenLetters[i] = currLetter
                if currLetter in yellowLetters and letterTwice == False:
                    yellowLetters.remove(currLetter)

        if (currLetter not in greenLetters) and (currLetter not in yellowLetters) and (currLetter not in lettersNotIn):
            lettersNotIn.append(currLetter)

    #get new guess
    #we're gonna need some sort of way to keep a score of a good guess

    # remove all words in wordArray that don't have the yellow/green letters
    # if yellow, remove all words with that letter in that slot
    # look through words.txt and see what the most common places for each letter is
    # so for example a appears most commonly in index 1 (idk if it does, just example)
    # so that's how you can prioritize guesses

    if (len(yellowLetters) != 0 and len(greenLetters) != 0):
        for w in range(len(wordList)):
            currWord = wordList[w]
            for i in range(len(greenLetters)):
                if (currWord[i] != greenLetters[i] and greenLetters[i] != "") or (currWord[i] not in yellowLetters) or (currWord[i] in lettersNotIn):
                    wordList.remove(w)
                    w -= 1

        #keep guessing
    else:
        #this is if the first guess had no letters in the word
        currGuess = secondWord

    print("NEW WORD LIST")
    # if wordList == (pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv").tolist()["validWordleAnswer"]):
    #     print("ur mom")
        # check if it removed anything or if its just the same
    print(wordList)

print(greenLetters) #swag letters
print(yellowLetters) #slightly less swag letters
print(lettersNotIn) #not at all swag
