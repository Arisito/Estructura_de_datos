import pickle
with open('ejemplo.pkl', 'wb') as archivo:
    pkl = pickle.Pickler(archivo)
    
    lista1 = [1, 2, 3]
    lista2 = [4, 5]
    diccionario = {'campo1': 1, 'campo2': 'dos'}
    
    pkl.dump(lista1)  #el .dump es pa meter datos
    pkl.dump(None)
    pkl.dump(lista2)
    pkl.dump('Hola mundo')
    pkl.dump(diccionario)
    pkl.dump(1)
    
with open('ejemplo.pkl', 'rb') as archivo:
    seguir_leyendo = True
    while seguir_leyendo:
        try:
            data = pickle.load(archivo) # Leo del archivo un elemento
        except EOFError:
            seguir_leyendo = False
        else:
            print ('### Esta linea no es del archivo ###')
            print (data)
lista = [
    {'usuario': 'usuario1', 'puntaje': 5},
    {'usuario': 'usuario2', 'puntaje': 3},
    {'usuario': 'usuario3', 'puntaje': 1},
]

with open('ejemplo_2.pkl', 'wb') as archivo:
    pkl = pickle.Pickler(archivo)
    pkl.dump(lista)
    
with open('ejemplo_2.pkl', 'rb') as archivo:
    data = pickle.load(archivo)
    print(data)