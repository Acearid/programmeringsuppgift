#Lista med koordinater
lista=[[0,1],[2,3],[4,5]]
k=3
m=7
#Funktionen Z och medel
def z(x,y,k,m):
    return[x,y-(k*x+m)]
def medel(x):
    return sum(x) / len(x)
#For loop
residualer=[]
for i in lista:
    #i = [x,y]
    x = i[0]
    y = i[-1]
    #Svar är (x, residual)
    svar = z(x,y,k,m)
    #Sparar bara residualer i kvadrat, för senare
    residualer.append(svar[1]**2)



#Räknar ut medelvärdet av residualerna
print(medel(residualer))

print(residualer)

