#↓Här är alla funktioner sammlade↓

#↓Funktionen för medianen↓
def median(ls):
    n = len(ls)
    x = n // 2
    if n % 2:
        return sorted(ls)[x]
    else:
        return sum(sorted(ls)[x - 1:x + 1]) / 2
#↓Funktionen för standardavikelse↓
def std_dev(ls):
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)** 2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev
#Funktionen för meanvärde↓
def mean(x):
    return sum(x) / len(x)
#↓Funktionen för variations bred↓
def varbred(x):
    return max(x) - min(x)
#↓Funktionen för undre kvartilen↓
def kvartilun(ls):
    ls.sort()
    return ls[0:int(len(ls)/2)]
#↓Funktionen för övre kvartilen↓
def kvartilup(ls):
    ls.sort()
    return ls[int(median(ls)):-1]
#↓Funktionen för kvartilavstånd↓
def kvartilavst(ls):
    up = median(kvartilup(ls))
    un = median(kvartilun(ls))
    return up - un
#↓Funktionen för meanvärde av residualerna↓
def z(x,y,k,m):
    return[x,y-(k*x+m)]