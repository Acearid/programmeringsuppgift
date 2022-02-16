#importerade moduler
import math
import numpy as np
import statistics as st

#funktionerna
def medel(x):
    return sum(x) / len(x)
def standardav(x):
    return np.std(x)
def medianen(x):
    return st.median(x)

#listan
x = [1,2,3,4,5]

#variablerna för svaren
svarmed = medel(x)
svarstandard = standardav(x)
svarmedian = medianen(x)

#skriver ut svaren
print("medelvärde: ", svarmed)
print("standard avikelse: ", svarstandard )
print("median: ", svarmedian)

