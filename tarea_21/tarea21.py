############################################################################
#### Tarea21 - FRACCIÓN IRREDUCIBLE by Iñaki Retegi (TheEgg) 2020/06/18 ####
############################################################################

#ALGORITMO#

def fraccion(decimal):
    #Inicialización de datos
    start = 1
    stop  = 10000 
    step  = 1
    encontrado = False

    #Busqueda de fracción irreducible
    for dividendo in range(start, stop, step):
        if(encontrado==True):
            break
        for divisor in range(start, stop, step):
            if(encontrado==True):
                break
            resultado=dividendo/divisor
            if(resultado==decimal and encontrado==False):
                resultado=1
                valor=(str(dividendo)+"/"+str(divisor))
                encontrado=True
    if encontrado == False:
        resultado=2
        
    #Return
    if resultado==1:
        return valor
    if resultado==2:
        return "Vaya parece que no lo encontramos...prueba otro."

                

#PROGRAMA#

min=0.0001
max=0.9999

while True:
    while True:
        try:
            decimal=float(input("Introduce un número entre 0.0001 y 0.9999 "))
            if(decimal>=min and decimal<=max):
                break
            else:
                print("Ese número no vale. Prueba de nuevo...")
        except ValueError:
            print("No has escrito un número. Prueba de nuevo...")
    a=fraccion(decimal)
    print(a)


