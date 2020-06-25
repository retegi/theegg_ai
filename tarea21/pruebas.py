############################################################################
#### Tarea21 - FRACCIÓN IRREDUCIBLE by Iñaki Retegi (TheEgg) 2020/06/18 ####
############################################################################

#ALGORITMO#

num=0.75
min=1
max=9999
estimado=int(min+max/2)
#print(estimado)

for i in range(10):
    if(i>0):
        while((i/estimado)!=num):
            if(i/estimado>num):
                estimado=int(estimado*1.5)+1
                print(i,"/",estimado, "=",i/estimado)
            else:
                estimado=int(estimado*0.5)+1
                print(i,"/",estimado, "=",i/estimado)
#print(1/estimado)
    