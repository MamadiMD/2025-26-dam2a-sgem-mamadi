bruce = {"nombre": "Bruce Banner", "trabajos": [80,50,40,20], "test": [75,75], "practicas": [78.20,77.20]}
harry = {"nombre": "Harry Potter", "trabajos": [82,56,44,30], "test": [80,80], "practicas": [67.90,78.72]}
hermione = {"nombre": "Hermione Ranger", "trabajos": [95,100,100,100], "test": [99,100], "practicas": [95.0,80.5]}
peter = {"nombre": "Peter Parker", "trabajos": [30,10,100,100], "test": [90,10], "practicas": [50.0,50.0]}
mario = {"nombre": "Super Mario", "trabajos": [77,82,23,39], "test": [18,60], "practicas": [80.6,59.3]}


estudiantes = {1:bruce, 2:harry, 3:hermione, 4:peter, 5:mario}
notas = {"Sobresaliente":[],"Notable":[],"Bien":[],"Suficiente":[],"Necesita mejorar":[]}

for estudiante in estudiantes.values():
        notamedia = 0
        trabajos = 0
        tests = 0
        practicas = 0
        
        for trabajo in estudiante["trabajos"]:
            trabajos += trabajo
        
        trabajos = (trabajos / len(estudiante["trabajos"])) * 0.1

        for test in estudiante["test"]:
            tests += test

        tests = (tests / len(estudiante["test"])) * 0.5

        for practica in estudiante["practicas"]:
            practicas += practica
        
        practicas = (practicas/len(estudiante["practicas"])) * 0.4

        notamedia = trabajos + tests + practicas

        nombre = estudiante["nombre"]

        datos = [nombre,notamedia]

        print(nombre)
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("Nota media final para " + nombre + " : " + str(round(notamedia , 2)))
        
        if notamedia >= 90:
            print("Calificacion final de " + nombre + " : Sobresaliente" )
            notas["Sobresaliente"].append(datos)
        elif notamedia >= 70:
            print("Calificacion final de " + nombre + " : Notable" )
            notas["Notable"].append(datos)
        elif notamedia >= 60:
            print("Calificacion final de " + nombre + " : Bien" )
            notas["Bien"].append(datos)
        elif notamedia >= 50:
            print("Calificacion final de " + nombre + " : Suficiente" )
            notas["Suficiente"].append(datos)
        elif notamedia < 50:
            print("Calificacion final de " + nombre + " : Necesita mejorar" )
            notas["Necesita mejorar"].append(datos)



seguir = True
while(seguir):
    respuesta = input("Desea filtar por calificacion (S/N): ")
    if respuesta == "S":
        filtracion = input("Introduzca uno de los siguientes valores (Sobresaliente - Notable - Bien - Suficiente - Necesita Mejorar)")
        if filtracion == "Sobresaliente":
            for sobresaliente in notas["Sobresaliente"]:
                print(sobresaliente[0])
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Nota media final para " + sobresaliente[0] + " : " + str(round(sobresaliente[1])))
                print("Calificacion final de " + sobresaliente[0] + " : Sobresaliente" )
        elif filtracion == "Notable":
            for notable in notas["Notable"]:
                print(notable[0])
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Nota media final para " + notable[0] + " : " + str(round(notable[1])))
                print("Calificacion final de " + notable[0] + " : Notable" )
        elif filtracion == "Bien":
            for bien in notas["Bien"]:
                print(bien[0])
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Nota media final para " + bien[0] + " : " + str(round(bien[1])))
                print("Calificacion final de " + bien[0] + " : Bien" )
        elif filtracion == "Suficiente":
            for suficiente in notas["Suficiente"]:
                print(suficiente[0])
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Nota media final para " + suficiente[0] + " : " + str(round(suficiente[1])))
                print("Calificacion final de " + suficiente[0] + " : Suficiente" )
        elif filtracion == "Necesita mejorar":
            for necesita in notas["Necesita mejorar"]:
                print(necesita[0])
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                print("Nota media final para " + necesita[0] + " : " + str(round(necesita[1])))
                print("Calificacion final de " + necesita[0] + " : Necesita mejorar" )
        else:
            print("Valor no valido")
    elif respuesta == "N":
        seguir = False
    else:
        print("Introduce S o N")

        




