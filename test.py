import pandas as pd

df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
wordList = df["validWordleAnswer"].tolist()
print(wordList)

