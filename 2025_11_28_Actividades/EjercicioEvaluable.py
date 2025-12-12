bruce = {"nombre": "Bruce Banner", "trabajos": [80,50,40,20], "test": [75,75], "practicas": [78.20,77.20]}
harry = {"nombre": "Harry Potter", "trabajos": [82,56,44,30], "test": [80,80], "practicas": [67.90,78.72]}
hermione = {"nombre": "Hermione Ranger", "trabajos": [95,100,100,100], "test": [99,100], "practicas": [95.0,80.5]}
peter = {"nombre": "Peter Parker", "trabajos": [30,10,100,100], "test": [90,10], "practicas": [50.0,50.0]}
mario = {"nombre": "Super Mario", "trabajos": [77,82,23,39], "test": [18,60], "practicas": [80.6,59.3]}


estudiantes = {1:bruce, 2:harry, 3:hermione, 4:peter, 5:mario}


def calcular_nota_media(estudiante):
    trabajos = sum(estudiante["trabajos"]) / len(estudiante["trabajos"]) * 0.1
    tests = sum(estudiante["test"]) / len(estudiante["test"]) * 0.5
    practicas = sum(estudiante["practicas"]) / len(estudiante["practicas"]) * 0.4
    notamedia = trabajos + tests + practicas
    return notamedia

    
def listarNotas(estudiante):
    notas = {"Sobresaliente":[],"Notable":[],"Bien":[],"Suficiente":[],"Necesita mejorar":[]}
    for estudiante in estudiantes.values():
        nota_media = calcular_nota_media(estudiante)
        if nota_media >= 90:
            notas["Sobresaliente"].append(estudiante)
        elif nota_media >= 70:
            notas["Notable"].append(estudiante)
        elif nota_media >= 60:
            notas["Bien"].append(estudiante)
        elif nota_media >= 50:
            notas["Suficiente"].append(estudiante)
        else:
            notas["Necesita mejorar"].append(estudiante)
    return notas

def asignar_calificacion(estudiante):
    nota_media = calcular_nota_media(estudiante)
    nombre = estudiante["nombre"]
    if nota_media >= 90:
        return (f"Calificacion final de {nombre}: Sobresaliente")
    elif nota_media >= 70:
        return (f"Calificacion final de {nombre}: Notable")
    elif nota_media >= 60:
        return (f"Calificacion final de {nombre}: : Bien")
    elif nota_media >= 50:
        return (f"Calificacion final de {nombre}: Suficiente")
    else:
        return (f"Calificacion final de {nombre}: Necesita mejorar")


def mostrar_informe(estudiante):
    nota_media = calcular_nota_media(estudiante)
    calificacion = asignar_calificacion(estudiante)
    nombre = estudiante["nombre"]
    print(nombre)
    print(f"Nota media final para {nombre} : {round(nota_media,2)}")
    print(calificacion)

def menu_filtro(estudiantes):
    seguir = True
    while(seguir):
        respuesta = input("Desea filtar por calificacion (S/N): ")
        if respuesta == "S":
            notas = listarNotas(estudiantes)
            filtracion = input("Introduzca uno de los siguientes valores (Sobresaliente - Notable - Bien - Suficiente - Necesita Mejorar - Mostrar todo): ")
            if filtracion in notas:
                for estudiante in notas[filtracion]:
                    mostrar_informe(estudiante)
            elif filtracion == "Mostrar todo":
                for estudiante in estudiantes.values():
                    mostrar_informe(estudiante)
                    seguir = False
            else:
                print("Valor no valido")

        elif respuesta == "N":
            for estudiante in estudiantes.values():
                mostrar_informe(estudiante)
                seguir = False
        else:
            print("Introduce S o N")


for estudiante in estudiantes.values():
        mostrar_informe(estudiante)

menu_filtro(estudiantes)

    


        




