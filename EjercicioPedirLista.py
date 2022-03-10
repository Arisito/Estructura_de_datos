lista = []
n=int(input("Cuantos numeros tendra la lista?"))
for i in range(n):
    lista.append(int(input("Introduce un numero a la lista")))
lista.sort()
print("La lista se conforma por: " , lista)