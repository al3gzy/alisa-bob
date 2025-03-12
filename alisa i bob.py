import numpy as np
import sys

def alisa_igra(niz, zbirA, prethodniA, zbirB, prethodniB):
    if len(niz) == 0:
        pobednik(zbirA, zbirB)
        return zbirA, zbirB
    
    if prethodniA == 0:
        prethodniA = np.max(niz)
        zbirA += prethodniA
        niz = np.delete(niz, np.where(niz == prethodniA)[0][0])
    else:
        max_val = -sys.maxsize
        index = -1
        for i in range(len(niz)):
            if niz[i] > max_val and niz[i] % 2 != prethodniA % 2:
                max_val = niz[i]
                index = i
        if index == -1:  # No valid number found, return zbirA
            return zbirA, zbirB
        zbirA += max_val
        prethodniA = max_val
        niz = np.delete(niz, index)
    
    return bob_igra(niz, zbirA, prethodniA, zbirB, prethodniB)

def bob_igra(niz, zbirA, prethodniA, zbirB, prethodniB):
    if len(niz) == 0:
        pobednik(zbirA, zbirB)
        return zbirA, zbirB
    
    if prethodniB == 0:
        prethodniB = np.max(niz)
        zbirB += prethodniB
        niz = np.delete(niz, np.where(niz == prethodniB)[0][0])
    else:
        max_val = -sys.maxsize
        index = -1
        for i in range(len(niz)):
            if niz[i] > max_val and niz[i] % 2 != prethodniB % 2:
                max_val = niz[i]
                index = i
        if index == -1:  # No valid number found, return zbirB
            return zbirA, zbirB
        zbirB += max_val
        prethodniB = max_val
        niz = np.delete(niz, index)
    
    return alisa_igra(niz, zbirA, prethodniA, zbirB, prethodniB)

def pobednik(zbirA, zbirB):
    if zbirA > zbirB:
        print('Alisa')
    else:
        print('Bob')

niz = np.array([1, 3, 4, 2, 6, 4])
zbirA, zbirB = alisa_igra(niz, 0, 0, 0, 0)
pobednik(zbirA, zbirB)