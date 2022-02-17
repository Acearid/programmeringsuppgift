import statistics as st

def kvartilun(ls):
    ls.sort()
    return ls[0:int(len(ls)/2)]
def kvartilup(ls):
    ls.sort()
    return ls[int(st.median(ls)):-1]
def kvartilavst():
    up = st.median(kvartilup(ls))
    un = st.median(kvartilun(ls))
    return up - un

ls = [1,2,11,3,14,13,5,6,7,22]

print("övre kvartil: ",st.median(kvartilup(ls)))
print("nedre kvartil: ", st.median(kvartilun(ls)))
print("kvartil avstånd: ", kvartilavst())
