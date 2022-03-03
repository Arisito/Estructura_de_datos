def factorial(numero):
    if numero > 1:
        numero = numero*factorial(numero-1)
    return(numero)
    
n=int(input("Hola, buenas tardes, porfavor ingrese el numero para factorializarlo"))
print (factorial(n))
