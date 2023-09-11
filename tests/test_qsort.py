import pandas as pd
import quick_sort
import time

df = pd.read_excel(r"S:\Techtorium SD L6 2023\3.1 - Advanced Programming (Python)\Final Assessment\BirthWeight.xlsx")
datalist = df['BirthWeight'].tolist()
sorted_datalist = sorted(datalist)  

def test_sorted():
    #sorted == sorted
    start = time.time()
    assert quick_sort.quicksort(sorted_datalist) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_unsorted():
    #function(unsorted) == sorted
    start = time.time()
    assert quick_sort.quicksort(datalist) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")
    
def test_empty():
    nolist = []
    start = time.time()
    assert quick_sort.quicksort(nolist) == []
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_reversed():
    #a reversed sorted data == sorted
    reverse_list = sorted(datalist)
    reverse_list.reverse()
    start = time.time()
    assert quick_sort.quicksort(reverse_list) == sorted_datalist
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")

def test_duplicate():
    #duplicate unsorted == duplicate sorted
    duplicate = datalist * 2
    start = time.time()
    assert quick_sort.quicksort(duplicate) == sorted(duplicate)
    end = time.time()
    print("Execution Time: ", round(end - start, 3), "seconds")