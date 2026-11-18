frecuencias = {}

# while True crea un bucle infinito que se repite hasta que encontramos un break.
while True:
    texto = input("Introduce una frase (o escribe fin para terminar): ")
    if texto.lower() == "fin":
        break

    texto = texto.lower()
    # split() separa las formas para recorrerlas de una en una.
    for palabra in texto.split():
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] = frecuencias[palabra] + 1
    print(frecuencias)