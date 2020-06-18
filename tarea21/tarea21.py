#Mínimo y máximo
min=0.0001
max=0.9999

#Tomar dato
while True:
    decimal=float(input("Introduce un número entre 0.0001 y 0.9999 "))
    if(decimal>=min and decimal<=max):
        break
print(decimal)

start = 1
stop  = 10000 
step  = 1
encontrado = False

for dividendo in range(start, stop, step):
    if(encontrado==True):
        break
    for divisor in range(start, stop, step):
        if(encontrado==True):
            break
        #print(dividendo , "/" , divisor)
        resultado=dividendo/divisor
        if(resultado==decimal and encontrado==False):
            print(dividendo , "/" , divisor)
            encontrado=True
if encontrado == False:
    print("¡Vaya parece que no lo encontramos...")            
            