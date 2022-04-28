import os

print (" Crear un archivo ")
print (" ================ ")

NOMBRE_ARCHIVO = "datos.txt"

archivo = open(NOMBRE_ARCHIVO, "w")
archivo.write("Bajo el cielo más puro de América\nY en la tierra de Ñuflo de Chávez\nLibertad van trinando las aves\nDe sureste ostentando el primor\n\nDe las flores del mundo galano\nSu ambrosía perfumada ofreciendo\n\nLibertad, libertad van diciendo\nEn efluvios de paz y de amor\nLibertad, libertad van diciendo\nEn efluvios de paz y de amor")
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


print("\nEliminar un archivo")
print("======================")

os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO)
print ("\n Eliminado archivo desde la ruta: \n\n\t{0}/{1}".format(
    os.getcwd(), NOMBRE_ARCHIVO))

#ID DEL CUPON, NOMBRE DEL CUPON, CANTIDAD DEL CUPON
# Ari Antoine Rocha Moret
