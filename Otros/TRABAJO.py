"Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas. Un Anagrama" 
"consiste en formar una palabra reordenando"

"TODAS las letras de otra palabra inicial."
"NO hace falta comprobar que ambas palabras existan."
"Dos palabras exactamente iguales no son anagrama."
    
print("-Anagrama-")

print("Escribe 2 palabras para comprobar si son anagramas o no")

palabra1 = input("\n Escribe la primer palabra: ").lower

palabra2 = input("\n Escribe la segunda palabra: ").lower

if palabra1 == palabra2:

    print("Las palabras son iguales, no son anagramas")

else:
   
    if len(palabra1) != len(palabra2):

        print("Ambas palabras tienen diferente numero de letras")

    else:
        separador_palabra1 = {}

        for letra in palabra1:

            if letra in separador_palabra1:

                separador_palabra1[letra] += 1

            else:

                separador_palabra1[letra] = 1

            es_anagrama = True

        for letra in palabra2:

            if letra in separador_palabra1:

                separador_palabra1[letra] -= 1

                if separador_palabra1[letra] == 0:

                    del separador_palabra1[letra]

            else:

                es_anagrama = False

                break

            if len(separador_palabra1) == 0 and es_anagrama:
                print(True)

        else:

            print(False)