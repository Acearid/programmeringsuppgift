#importerade moduler
from sammling import *
#listan
ls = [1,2,3,4,5,6]
#variablerna för svaren
svarmed = mean(ls)
svarstdev = std_dev(ls)
svarmedian = median(ls)
svarvarbred = varbred(ls)
#skriver ut svaren
print("meanvärde: ", svarmed)
print("standard avikelse: ", svarstdev)
print("median: ", svarmedian)
print("variations bred: ", svarvarbred)