import time

class Jugador:
  def __init__(self, name, vida, ataque):
    self.name = name
    self.ataque = ataque
    self.vida = vida

pikachu = Jugador("Pikachu",100,55)
jigglypuff = Jugador("Jigglypuff",100,45)

print(pikachu.name)
print("Vida: ",pikachu.vida)
print("Ataque: ",pikachu.ataque)

print(jigglypuff.name)
print("Vida: ",jigglypuff.vida)
print("Ataque: ",jigglypuff.ataque)
print("")
turno=1 # 1 toca a pikachu| 0 toca a jigglypuff
print("¡COMIENZA EL COMBATE!")
while pikachu.vida > 0 and jigglypuff.vida > 0:

    if turno==1:
        print("Turno de ", pikachu.name)
        time.sleep(3)
        print(pikachu.name, " ataca a ", jigglypuff.name, " con una fuerza de ", pikachu.ataque)
        jigglypuff.vida = jigglypuff.vida - pikachu.ataque
        if jigglypuff.vida < 0:
            jigglypuff.vida=0
        time.sleep(3)
        print("Vida de", jigglypuff.name, " = " , jigglypuff.vida)
        turno = 0
        time.sleep(3)
    else:
        print("Turno de ", jigglypuff.name)
        time.sleep(3)
        print(jigglypuff.name, " ataca a ", pikachu.name, " con una fuerza de ", jigglypuff.ataque)
        pikachu.vida = pikachu.vida - jigglypuff.ataque
        if pikachu.vida < 0:
            pikachu.vida=0
        time.sleep(3)
        print("Vida de", pikachu.name, " = " , pikachu.vida)
        turno = 1
        time.sleep(3)

if pikachu.vida > 0:
    print("Ganador: ", pikachu.name)
else:
    print("Ganador: ", jigglypuff.name)
print("¡Fin del Juego!")

