############################################################################
#### Tarea80 - FRACCIÓN IRREDUCIBLE by Iñaki Retegi (TheEgg) 2021/12/12 ####
#### (Es una versión mejorada respecto al anterior tarea_21) ###############
############################################################################

#ALGORITMOS#

#Comprueba si es decimal o división:
def comprobarDecimalDivision(num):
    contiene_division="/" in num
    if contiene_division:
        print('Ha insertado una división, lo convertiremos a decimal.')
    return contiene_division

#Si se ha insertado una división, se convierte a decimal:
def convertirADecimal(num):
    lista = num.split("/")
    dividendo=int(lista[0])
    divisor=int(lista[1])
    num = dividendo / divisor
    dividendo=0
    divisor=0
    print('Convertido a decimal:',num)
    return num

def estaDentroDeRango(num):
    num = float(num)
    enrango = (num >= 0.0001 and num <= 0.9999)
    return enrango


#PROGRAMA#
busqueda = "No encontrado"
dentro_de_rango = False

while not dentro_de_rango:
    num=(input("Inserte un número entre 0.0001 y 0.9999\n"))
    contiene_division=comprobarDecimalDivision(num)
    if contiene_division:
        num=convertirADecimal(num)
    dentro_de_rango=estaDentroDeRango(num)
    if not dentro_de_rango:
        print('El número no está dentro del rango indicado.')
    dentro_de_rango=estaDentroDeRango(num)
    
print('Buscando división...')
for dividendo in range (1,10000):
    if busqueda == 'Encontrado':
        break
    for divisor in range (1,10000):
        if busqueda == 'Encontrado':
            break
        resultado = float(dividendo/divisor)
        #print (num,"  ",resultado)
        num = float(num)
        if resultado == num:
            print(dividendo,'/',divisor)
            busqueda = 'Encontrado'
            break
print(busqueda)


    
