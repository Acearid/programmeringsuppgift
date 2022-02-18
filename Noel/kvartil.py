from sammling import *

ls = [1,2,11,3,14,13,5,6,7,22]

print("övre kvartil: ",median(kvartilup(ls)))
print("nedre kvartil: ", median(kvartilun(ls)))
print("kvartil avstånd: ", kvartilavst(ls))
