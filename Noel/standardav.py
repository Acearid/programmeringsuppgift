def std_dev(ls):
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)** 2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev


ls = [1,2,3,4,5]

print(std_dev(ls))