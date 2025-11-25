
jugadorFutbol1 = [("Nombre","Lionel Messi"),("Posicion","Delantero"),("Equipo","FC Barcelona"),("Dorsal","10")]
jugadorFutbol2 = [("Nombre","Cristiano Ronaldo"),("Posicion","Delantero"),("Equipo","Real Madrid"),("Dorsal","7")]
jugadorFutbol3 = [("Nombre","Mbappe"),("Posicion","Delantero"),("Equipo","PSG"),("Dorsal","9")]

jugadores = {1:jugadorFutbol1,2:jugadorFutbol2,3:jugadorFutbol3}

for jugador in jugadores:
    for player in jugador:
        print("La etiqueta " + player[0] +" tiene el valor " + player[1])