import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np


def readSubtitleToList(filepath="IronManDutch.srt"):
    """this function reads file and returns as list of sentances splited line by line"""
    with open(filepath) as file:
        return file.read().splitlines()


def eliminateNumEmpStr(linesList):
    """ empty strings, numbers and times eliminated from list by returning new list which has just sentances """
    justSentances = []
    for line in linesList:
        if line == "" or line == " ":
            continue
        if line[0].isdigit():
            continue
        else:
            justSentances.append(line)
    return justSentances


def listToLowercaseString(linesList, merger=" "):
    """takes list of sentances makes them lowercase returns string merged with space"""
    return merger.join(linesList).lower()


def eliminatePunctuation(text):
    """takes text returns text without punctuation """
    return text.translate(str.maketrans("", "", string.punctuation))


def wordFreqDic(wordsList):
    """takes list of words and returns word:frequency dictionary"""
    wordOccuranceDic = {}
    uniqueWords = set(wordsList)
    print("checking how many unique Words do we have: " + str(len(uniqueWords)))
    for word in uniqueWords:
        wordOccuranceDic[word] = wordsList.count(word)
    return wordOccuranceDic


## part 1 ##
# subtitle opened and returned list seperated with \n
lines = readSubtitleToList(filepath="IronManDutch.srt")
print("checking first 10 element of list: ", lines[:10])

# empty strings, numbers and times eliminated from list by creating new list
justSentances = eliminateNumEmpStr(lines)
print("checking how many sentences do we have: ", len(justSentances))
print("checking first 7 sentences: ", justSentances[:7])

## part 2 ##    # Time to count words
# first combine list to seperate all text via space to take words
context = eliminatePunctuation(listToLowercaseString(justSentances, merger=" "))
# make all lower case and split
words = context.split(sep=" ")
print("checking how many words do we have: " + str(len(words)))

# Creating dictionary for words and their frequency
# turn dic ti pandas series to sorting and seeing head and writing as csv
df = pd.Series(wordFreqDic(words))
values = df.sort_values(ascending=False)
print("dataframe len: " + str(len(df)))
print(values.head(10))
print(values.describe())

plt.scatter(values.get_values(), range(len(values.get_values())), s=values.get_values(), c=np.random.rand(len(values.get_values())),
            alpha=0.5)
plt.show()
# values.to_csv('out.csv')

# with open("words.txt","a") as words:
#     for item in justSentances:
#         words.write(item+"\n")
#     print("done")
