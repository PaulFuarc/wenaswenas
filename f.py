# Convertimos ambas palabras a minúsculas para ignorar diferencias de mayúsculas/minúsculas
palabra1 = input("Introduce la primera palabra: ").lower()
palabra2 = input("Introduce la segunda palabra: ").lower()

# Si las palabras son exactamente iguales, no son anagramas
if palabra1 == palabra2:
    print(False)
else:
    # Si las palabras tienen diferentes longitudes, no pueden ser anagramas
    if len(palabra1) != len(palabra2):
        print(False)
    else:
        # Contamos las letras en la primera palabra
        contador_palabra1 = {}
        for letra in palabra1:
            if letra in contador_palabra1:
                contador_palabra1[letra] += 1
            else:
                contador_palabra1[letra] = 1

        # Restamos las letras al contador usando la segunda palabra
        es_anagrama = True
        for letra in palabra2:
            if letra in contador_palabra1:
                contador_palabra1[letra] -= 1
                if contador_palabra1[letra] == 0:
                    del contador_palabra1[letra]
            else:
                es_anagrama = False
                break

        # Si el diccionario queda vacío, las palabras son anagramas
        if len(contador_palabra1) == 0 and es_anagrama:
            print(True)
        else:
            print(False)
