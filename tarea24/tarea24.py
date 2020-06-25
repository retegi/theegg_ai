################################################################################
#### Tarea24 - CONSTRUYE UN SIMULADOR by Iñaki Retegi (TheEgg) 2020/06/25 ####
################################################################################

# ALGORITMO #

def pasarabinario(decimal,bits):
    salida = ""
    while(decimal!=1 and decimal!=0):
        resto=int(decimal%2)
        decimal=int(decimal/2)
        salida = str(resto) + str(salida)
    salida = str(decimal) + salida

    digitos = 0
    for c in salida:
        if c.isdigit():
            digitos += 1
    relleno = bits - digitos
    num=0
    while num < relleno:
        salida = "0" + salida
        num += 1

    return salida

# PROGRAMA #

decimal=int(input("Número en decimal: "))
bits=int(input("Bits: "))
resultado=pasarabinario(decimal,bits)
print(resultado)