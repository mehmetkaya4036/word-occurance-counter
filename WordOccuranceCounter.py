import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np


def readSubtitleToList(filepath):
    """this function reads file and returns as list of sentances splited line by line"""
    with open(filepath, encoding="cp437") as file:
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
    getRidOf = ["<i>", "</i>"] + [str(i) for i in range(10)]
    for unnecessaryPunch in getRidOf: text = text.replace(unnecessaryPunch, "")
    return text.translate(str.maketrans("", "", string.punctuation))


def wordFreqDic(wordsList, report=True):
    """takes list of words and returns word:frequency dictionary"""
    wordOccuranceDic = {}
    uniqueWords = set(wordsList) - {""}
    if report:
        print("checking how many unique Words do we have: " + str(len(uniqueWords)))
    for word in uniqueWords:
        wordOccuranceDic[word] = wordsList.count(word)
    return wordOccuranceDic


def txtTofreqDic(filepath, report=True):
    """takes filePath of subtitle-.srt- or .txt strip from punctuation, time, digits and
    returns a dictionary of word:occuranceFrewuency"""
    linesAsList = readSubtitleToList(filepath)
    linesAsListWithoutNumbers = eliminateNumEmpStr(linesAsList)
    text = eliminatePunctuation(listToLowercaseString(linesAsListWithoutNumbers))
    textToWordsAsList = text.split(sep=" ")

    if report:
        print("checking how many words do we have: " + str(len(textToWordsAsList)))

    return wordFreqDic(textToWordsAsList, report)


if __name__ == "__main__":
    ## part 1 ##
    # subtitle opened and returned list seperated with \n
    lines = readSubtitleToList(filepath="TurboDutch.srt")
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
    print("checking first 10 element of list: ", words[:20])

    # Creating dictionary for words and their frequency
    # turn dic ti pandas series to sorting and seeing head and writing as csv
    df = pd.Series(wordFreqDic(words))
    values = df.sort_values(ascending=False)
    print("dataframe len: " + str(len(df)))
    print(values.head(10))
    print(values.describe())

    plt.scatter(values.get_values(), range(len(values.get_values())), s=values.get_values(),
                c=np.random.rand(len(values.get_values())),
                alpha=0.5)
    plt.show()
    # values.to_csv('out.csv')

    # with open("words.txt","a") as words:
    #     for item in justSentances:
    #         words.write(item+"\n")
    #     print("done")
