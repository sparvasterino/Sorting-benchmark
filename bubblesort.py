from timeit import time
from random import randrange



                                                                                    

# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10000)]

# Algoritmo di ordinamento
print("lista prima:")
print(mylist)


# Scrivere qui l'algoritmo di Bubble Sort
def bubblesort(list):  
    start_time = time.time() 
    m = len(list)
    m = m - 1 
    while m > 0:
        for i in range(m):
            if list[i] > list[i + 1]:
                backup = list[i]
                list[i] = list[i + 1]
                list[i + 1] = backup
        m -= 1



    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")
bubblesort(mylist)

# Stampo la lista appena calcolata
print("lista dopo:")
print(mylist)           