import random

rawStudents = "Mikel,IA_400,Magnus,Thor,Terminator,Spiderman,Yerai,Carla,Jokin,Julen,Xabier,Eduardo,Manuel,Yahya,Oier,Irene,Ruben,David,Mamadi,Ibon,Eneko,Dimitri,Luka,Diego"
alumnos = rawStudents.split(",")

numAlumnos = int(input("Ingrese el número de alumnos: "))
if numAlumnos > 20 or numAlumnos <= 0:
    print("Introduce un numero entre el 1 y 20")
elif type(numAlumnos) != int:
    print("Introduce un numero")
else:
    while(numAlumnos > 0):
        randomNum = random.randint(1,20)
        print(alumnos[randomNum])
        numAlumnos -= 1
    
    print("Alumnos generados correctamente")
    