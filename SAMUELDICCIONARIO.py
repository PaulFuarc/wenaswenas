#COMPRESION DICCIONARIO, COMPRENSION LISTAS

#CREA UNA LISTA QUE GENERE LOS NUMEROS AL CUADRADO DEL 1 AL 20
print("LISTA GENERADORA LOS NUMEROS AL CUADRADO")
cuadrados = [x**2 for x in range(10)]
print(cuadrados) 


#Crea una lista que contenga solo los números pares del 1 al 50
print("\nLISTA DE NUMEROS PARES")
pares = [x for x in range(51) if x % 2 == 0]
print(pares)  # Output: [0, 2, 4, 6, 8]

#Dada una lista de cadenas, crea una nueva lista con todas las cadenas en minúsculas
print("\nLISTA DE CADENA MAYUSCULAS")
frutas = ["gallinon", "charro", "benito"]
frutas_mayusculas = [fruta.upper() for fruta in frutas]
print(frutas_mayusculas)

#Dada una lista de diccionarios que representan estudiantes con sus nombres y calificaciones, 
#usa comprensiones de listas para crear una lista de nombres de estudiantes que tiene una calificación mayor de 70
print("\nLISTA DE ALUMNOS APROBADOS")
estudiantes = [
    {"nombre": "Alan", "calificacion": 85},
    {"nombre": "Angel", "calificacion": 75},
    {"nombre": "Adrian", "calificacion": 90},
    {"nombre" : "Memo", "calificacion" : 60}
    ]

nombres_aprobados = [estudiante["nombre"] for estudiante in estudiantes if estudiante["calificacion"] > 70]

print("LISTA DE CALIFICACIONES")
print(nombres_aprobados) 


