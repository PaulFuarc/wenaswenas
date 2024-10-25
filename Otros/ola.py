
palabra1 = input("Introduce la primera palabra: ").lower()
palabra2 = input("Introduce la segunda palabra: ").lower()


if palabra1 == palabra2:
    print(False)
else:
   
    if len(palabra1) != len(palabra2):
        print(False)
    else:
        
        contador_palabra1 = {}
        for letra in palabra1:
            if letra in contador_palabra1:
                contador_palabra1[letra] += 1
            else:
                contador_palabra1[letra] = 1

        
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
