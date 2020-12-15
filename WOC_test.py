import WordOccuranceCounter as woc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
st=time.time()


fileNames=["IronMan1Dutch.srt","IronMan2Dutch.srt","IronMan3Dutch.srt","PenguinsOfMadagascarDutch.srt","AbominableDutch.srt","TurboDutch.srt"]

df = pd.DataFrame([woc.txtTofreqDic(name, False) for name in fileNames], index=fileNames).T.fillna(0) #transpose
df['Total'] = df.sum(axis=1)
df = df.sort_values(by=["Total"], ascending=False)
# print(df.tail())

#To not writing over and over again
# df = pd.read_csv("out.csv", index_col=0)
# print(df.head())

# df.to_csv('out.csv')

#tracking time
print("----%.2f----"%(time.time()-st))

# sns.heatmap(df.head(10).T, annot=True, fmt=".1f")
# plt.show()
