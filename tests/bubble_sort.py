import pandas as pd

def bubblesort(datalist):
    totalnum = len(datalist)
    for i in range(totalnum):
        for j in range(totalnum - 1):
            if datalist[j] > datalist[j + 1]:
                datalist[j], datalist[j + 1] = datalist[j + 1], datalist[j]
    return datalist

df = pd.read_excel('BirthWeight.xlsx')
datalist = df['BirthWeight'].tolist()

# print(bubblesort(datalist))


