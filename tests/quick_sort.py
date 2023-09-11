import pandas as pd
import random
import matplotlib.pyplot as plt

def swap(datalist, i, j):
    temp = datalist[i]
    datalist[i] = datalist[j]
    datalist[j] = temp

def partition(datalist, lo, hi):
    r = random.randint(lo, hi)
    datalist[lo], datalist[r] = datalist[r], datalist[lo]
    
    pivot = datalist[lo]
    (i, j) = (lo - 1, hi + 1)
    
    while True:
        while True:
            i += 1
            if datalist[i] >= pivot:
                break
        while True:
            j -= 1
            if datalist[j] <= pivot:
                break
        if i >= j:
            return j
        swap(datalist, i, j)

def qsort(datalist, lo, hi):
    if lo >= hi:
        return
    pivot = partition(datalist, lo, hi)
    qsort(datalist, lo, pivot)
    qsort(datalist, pivot + 1, hi)
    
def quicksort(datalist) -> list:
    qsort(datalist, 0, len(datalist) - 1)
    return datalist

df = pd.read_excel('BirthWeight.xlsx')
datalist = df['BirthWeight'].tolist()

x_val = range(len(datalist))
plt.subplot(1,2,1)
plt.bar(x_val, datalist)
plt.title("Unsorted Data")

sorted = quicksort(datalist)

plt.subplot(1,2,2)
plt.bar(x_val, sorted, color="green")
plt.title("Sorted Data with Quick Sort")
    
plt.show()

# print(quicksort(datalist))