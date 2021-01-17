import re
 
nup153 = open('/home/retegi/Documents/proyectos/theegg/theegg_ai/tarea41/nup153.txt').read()
 
patron = "(((GG(A|C|G)))|(TT(T|C))){2,}"
 
x = re.findall(patron, nup153)
 
print("Se han encontrado " + str(len(x)) + " repeticiones")