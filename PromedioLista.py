lista = []
suma = 0
n=int(input("Cuantos numeros tendra la lista?"))
for i in range(n):
    suma = suma + lista[i]
    lista.append(int(input("Introduce un numero a la lista")))
promedio = suma / n
print("El promedio de la lista es: ", promedio)