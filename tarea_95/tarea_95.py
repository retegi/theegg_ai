#1.- Realiza un programa que lea 2 números por teclado y determine:
#Si los dos números son igualesSi los dos números son diferentesSi el primero es mayor que el segundoSi el segundo es mayor o igual que el primero

"""num1=int(input("Número 1"))
num2=int(input("Número 2"))

if num1 > num2:
    print("Mayor",num1)
if num1 < num2:
    print("Mayor",num2)
else:
    print("Iguales")"""


#2.- Determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10.

"""texto=str(input("Insertar texto"))
long=len(texto)
if long >= 5 and long < 10:
    print("El texto introducido, \"",texto,"\" tiene entre 5 y 10 caracteres")
else:
    print("El texto introducido, \"",texto,"\" no tine entre 5 y 10 caracteres")"""


#3.- Realiza un programa que haga la tabla de multiplicación de un número introducido de valor entre 0 y 99:
#Guarda en una variable el número introducido por el usuario
#Añade un filtro que asegure que el número sea entre 0 y 99
# Escribe la tabla multiplicando el valor introducido por valores entre 1 y 10

"""def filtro(n):
    return(n>=0 and n<=99)

numValido=False

while numValido == False:
    num1=int(input("Inserta número: "))
    numValido=filtro(num1)
    print(numValido)

x=range(10)
for n in x:
    print(n+1," X ",num1, " = ",(n+1) * num1)"""


#4.- El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

"""numero_1 = 9   
numero_2 = 3
numero_3 = 6
media = (numero_1 + numero_2 + numero_3) / 3 #La solución es que los 3 números deben ir entre paréntesis, si no es así se divide únicamente el último número
print("La nota media es", media)"""


#5.- Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar el proceso debe repetirse hasta que lo introduzca correctamente.
"""inpar=False
while inpar == False:
    num=int(input("Introduce número impar: "))
    inpar=num%2!=0
print("¡Correcto! ¡Es impar!")"""

#6.- Realiza un programa que sume todos los números enteros impares desde el 0 hasta el 115.
suma=0
x=range(115)
for n in x:
    if n%2!=0:
        suma=suma+n
print(suma)

