import pandas as pd

def insertsort(datalist):
    totalnum = len(datalist)
    for i in range(totalnum):
        j = i
        while j > 0 and datalist[j - 1] > datalist[j]:
            datalist[j], datalist[j - 1] = datalist[j - 1], datalist[j]
            j = j - 1
    return datalist

df = pd.read_excel('BirthWeight.xlsx')
datalist = df['BirthWeight'].tolist()

# print(insertsort(datalist))

