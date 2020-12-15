import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np
""" 
Bug - because of punctuations there is misinfo about word counts. 
to solve it in context variable, get rid of punctuations before spliting words
regex can be helpful
"""
# subtitle opened and named life
with open("IronManDutch.srt") as file:
    # returned list seperated with \n
    lines = file.read().splitlines()
    print("checking first 10 element of list")
    print(lines[:10])

    # empty strings, numbers and times eliminated from list by creating new list
    justSentances = []
    for line in lines:
        if line == "":
            continue
        if line[0].isdigit():
            continue
        else:
            justSentances.append(line)
    print("checking how many sentences do we have")
    print(len(justSentances))
    print("checking first 7 sentences")
    print(justSentances[:7])

    # Time to count words
    # first combine list to seperate all text via space to take words
    context = " ".join(justSentances).lower()
    #eliminate punctuation
    context = context.translate(str.maketrans("","",string.punctuation))
    #make all lower case and split
    words = context.split(sep=" ")


    print("checking how many words do we have: " + str(len(words)))

    # Creating dictionary for words and their frequency
    wordOccurance = {}
    uniqueWords=set(words)
    print("checking how many unique Words do we have: " + str(len(uniqueWords)))
    for word in uniqueWords:
        wordOccurance[word] = words.count(word)

    print("wordOccurance len: " + str(len(wordOccurance)))

    #turn dic ti pandas series to sorting and seeing head and writing as csv
    df = pd.Series(wordOccurance)
    values = df.sort_values(ascending=False)
    print("dataframe len: " + str(len(df)))

    print(values.head(10))

    print(values.describe())

    plt.scatter(values.get_values(), range(len(values.get_values())), s=values.get_values(), c=np.random.rand(1771), alpha=0.5)
    plt.show()
    # values.to_csv('out.csv')

    # with open("words.txt","a") as words:
    #     for item in justSentances:
    #         words.write(item+"\n")
    #     print("done")


