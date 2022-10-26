import random

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
def si_o_no(pregunta):
  while True:
    ayuda = input(pregunta + " si/no\n")
    if ayuda == "si":
     return True
    elif ayuda == "no":
      return False
    else:
      print("responde con si o no")  

def pedir_cartas(lista1, lista2):
    for i in range(2):
     lista1.append(random.choice(lista2))

for key in cartas:
    print(key, "vale", cartas[key]) 

while True:
    menu = si_o_no("¿Quieres jugar a una partida?")
    if menu == False:
     break
    lista_cartas = [i for i in cartas]
    cartas_jugador = []
    cartas_banca = []
    pedir_cartas(cartas_jugador, lista_cartas)
    pedir_cartas(cartas_banca, lista_cartas)
    puntos_jugador = cartas[cartas_jugador[0]]+cartas[cartas_jugador[1]]
    puntos_cpu = cartas[cartas_banca[0]]+cartas[cartas_banca[1]]
    print(f"Tienes {cartas_jugador[0]} y {cartas_jugador[1]}, en total: {puntos_jugador} puntos")
    print(f"Tienes {cartas_banca[0]} y {cartas_banca[1]}, en total: {puntos_cpu} puntos")
    ganar = {
    puntos_jugador > puntos_cpu: "Has ganado",
    puntos_jugador < puntos_cpu: "Has perdido",
    puntos_jugador == puntos_cpu: "Empate"
    }
    print(ganar[True])