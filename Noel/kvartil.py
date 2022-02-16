import statistics as st

def kvartilun(ls):
    return ls[0:int(len(ls)/2)]
def kvartilup(ls):
    return ls[int(st.median(ls)):]

ls = [1,2,3,4,5]

print("övre kvartil: ",st.median(kvartilup(ls)))
print("övre kvartil: ", st.median(kvartilun(ls)))
