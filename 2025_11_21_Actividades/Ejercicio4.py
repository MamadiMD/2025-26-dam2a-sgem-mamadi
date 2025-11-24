continua = True
while continua == True:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 's':
        print("Procesando, un momento...")
    elif respuesta.lower() == 'n':
        print("Gracias por usar el servicio")
        continua = False
    else:
        print("Comando no valido")