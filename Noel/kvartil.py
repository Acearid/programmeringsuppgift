import statistics as st

def kvartilun(ls):
    ls.sort()
    return ls[0:int(len(ls)/2)]
def kvartilup(ls):
    ls.sort()
    return ls[int(st.median(ls)):-1]

ls = [1,2,11,3,14,13,5,6,7,22]

print("övre kvartil: ",st.median(kvartilup(ls)))
print("nedre kvartil: ", st.median(kvartilun(ls)))
