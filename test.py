from numpy import *
import random
from math import *


h = [float(input()) for i in range(int(input()))]
chislo = int(input())
k = 0

if chislo not in h:
    for i in range(len(h)):
        # print(chislo / h[i], h[i], '|', i, h.index(h[i]))
        if h[i] == 0:
            continue
        if chislo / h[i] in h:
            if h.index(chislo / h[i]) != h.index(h[i]) or k >= 1:
                print('ДА')
                break
            if h.index(chislo / h[i]) == h.index(h[i]):
                k += 1
    else:
        print('НЕТ')
else:
    if 1 in h:
        print("ДА")
    elif chislo == 0 and 0 in h:
        print("ДА")
    else:
        print('НЕТ')