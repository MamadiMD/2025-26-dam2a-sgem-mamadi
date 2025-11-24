palabra = input("Introduce una palabra: ")
palabra = palabra.strip()

if palabra.isalpha():
    letras = list(palabra)
    letras.sort()
    print(letras)
else:
    print("No es una entrada valida")


