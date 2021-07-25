################################################################################
#### Tarea22 - EL ALGORITMO DEL LECHERO by Iñaki Retegi (TheEgg) 2020/06/20 ####
################################################################################

# ALGORITMO #

from decimal import *
def lechero(totalVacas,pesoCamion,pesosVacas,lecheVacas):
    #Creamos lista multidimensional con datos
    lista={}
    for k in range(totalVacas):
        lista[k]=[k],[lecheVacas[k]/pesosVacas[k]],pesosVacas[k],lecheVacas[k]

    #Ordenamos la lista multidimensional de datos
    listaNueva=[]
    for i in range(totalVacas):
        for j in range(totalVacas-1):
            if(lista[i][1]>lista[j][1]):
                if(j>i):
                    listaNueva=lista[j]
                    lista[j]=lista[i]
                    lista[i]=listaNueva

    #Calcular las vacas que entran, suma de peso de vacas y producción de leche
    cuentaVacas=0
    pesoSumado=0
    prodLeche=0
    sigueSumando=True
    
    for i in range(totalVacas):
        while True:
            sumado=Decimal(pesoSumado)+Decimal(lista[i][2])
            if(sumado<pesoCamion):
                #Suma peso de vacas en camión
                pesoSumado=sumado
                #Número de vacas en camión
                cuentaVacas=cuentaVacas+1
                #Producción de leche de las vacas
                prodLeche=prodLeche+lista[i][3]
            else:
                sigueSumando==False
                break
            if sigueSumando==False:
                break
    return (cuentaVacas,pesoSumado,prodLeche)


# PROGRAMA #

#Datos(son ejemplos):
totalVacas=10
pesoCamion=5000
pesosVacas=[800,920,850,834,868,872,872,871,817,888]
lecheVacas=[18,19,17,18.5,19.4,20,17.5,16,18,19]
#Llamada a la función
a=lechero(totalVacas, pesoCamion, pesosVacas, lecheVacas)
#Resultados
print("Número de vacas en camión:",a[0])
print("Peso total de vacas en camión:",a[1],"kg")
print("Producción de leche:",a[2],"L/día")