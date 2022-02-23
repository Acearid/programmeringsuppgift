#importerar cordinat funktionen från sammlingen
from sammling import coordinates
#ls som variabel för kordinaterna
ls = [[0,1],[2,3],[4,5]]
#tar bort onödiga []
cordinater = str(coordinates(ls))[1:-1]
#skriver ut kordinaterna
print("cord:", cordinater)



