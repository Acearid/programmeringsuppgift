from sammling import mean,z #imported mean och z

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

meanresidualer = mean(residualer)


#Räknar ut meanvärdet av residualerna
print(meanresidualer)