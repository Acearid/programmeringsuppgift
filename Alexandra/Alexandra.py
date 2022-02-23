print("Detta är en Programmeringsuppgift av Noel, Alexandra och Axel NA21R")

#Lista med koordinaterna och k och m
lista=[[0,1],[2,3],[4,5]]
k=3
m=7
#Funktionerna Z och medel
def z(x,y,k,m):
    return[x,y-(k*x+m)]
def medel(x):
    return sum(x) / len(x)
#Koordinaterna loopas
residualer=[]
for i in lista:
    #i = [x,y]
    x = i[0]
    y = i[-1]
    #Svar är (x, residual)
    svar = z(x,y,k,m)
    #Residualer i kvadrat, för medelvärde senare
    residualer.append(svar[1]**2)



#Räknar ut medelvärdet av residualerna
print(medel(residualer))

print(residualer)