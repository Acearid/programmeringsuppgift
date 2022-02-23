def median(ls):
    n = len(ls)
    x = n // 2
    if n % 2:
        return sorted(ls)[x]
    else:
        return sum(sorted(ls)[x - 1:x + 1]) / 2
def std_dev(ls):
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)** 2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev
def medel(x):
    return sum(x) / len(x)
def varbred(x):
    return max(x) - min(x)
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
def z(x,y,k,m):
    return[x,y-(k*x+m)]
def medel(x):
    return sum(x) / len(x)
def coordinates(ls):
    for i in range(len(ls)):
        ls[i][1] = ls[i][1] - 1
    return ls