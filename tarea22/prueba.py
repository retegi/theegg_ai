
lista=[[1,0.23,400],[2,0.48,64],[3,0.74,90],[4,0.53,55],[5,0.28,30]]
listaNueva=[[0,0,0]]
for i in range(3):
     for j in range(3):
          if(lista[i][2]>lista[j][2]):
               if(j>i):
                    listaNueva[0]=lista[j]
                    lista[j]=lista[j+1]
                    lista[j+1]=listaNueva[0]
print(lista)