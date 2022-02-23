import matplotlib.pyplot as plt #grafverktyg
from sammling import medel,z #imported medel och z

#Lista med koordinater
lista=[[0,1],[2,3],[4,5]]
k=3
m=7
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

medelresidualer = medel(residualer)


#Räknar ut medelvärdet av residualerna
print(medelresidualer)

print(residualer)

plt.plot(lista, 'ro', lista)
plt.show()