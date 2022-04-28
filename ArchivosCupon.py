import os

print (" Crear un archivo ")
print (" ================ ")

NOMBRE_ARCHIVO = "datos.txt"

archivo = open(NOMBRE_ARCHIVO, "w")
archivo.write("256 ; CUPON_20 ; 20 Bs. \n245 ; CUPON_10 ; 10 Bs.\n875 ; CUPON_15 ; 15 Bs.\n275 ; CUPON_25 ; 25 Bs.\n425 ; CUPON_15 ; 15 Bs.  ")
archivo.write("")
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):
    print("\nArchivo creado en la ruta: \n\n\t{0}\{1}".format(
        os.getcwd(), NOMBRE_ARCHIVO))
else:
    print ("El archivo fue creado!!\n")
    
archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print (contenido)
archivo.close()

print("\n\n Iterar sobre un archivo")
print("============================")

archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
    print (linea)
print ("\n")
archivo.close()


#print("\nEliminar un archivo")
#print("======================")

#os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO)
#print ("\n Eliminado archivo desde la ruta: \n\n\t{0}/{1}".format(
#    os.getcwd(), NOMBRE_ARCHIVO))

#ID DEL CUPON, NOMBRE DEL CUPON, CANTIDAD DEL CUPON
# Ari Antoine Rocha Moret