import statistics as st
from sammling import median
def kvartilun(ls):
    ls.sort()
    return ls[0:int(len(ls)/2)]
def kvartilup(ls):
    ls.sort()
    return ls[int(median(ls)):-1]
def kvartilavst(ls):
    up = median(kvartilup(ls))
    un = median(kvartilun(ls))
    return up - un

ls = [1,2,11,3,14,13,5,6,7,22]

print("övre kvartil: ",median(kvartilup(ls)))
print("nedre kvartil: ", median(kvartilun(ls)))
print("kvartil avstånd: ", kvartilavst(ls))
