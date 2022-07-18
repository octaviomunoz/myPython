
# List

# Las listas son estructuras de datos que pueden almacenar cualquir tipo de datos

nombres = ["Mia", "Haba", "Tona", "Mona", "Lupita"]
edad = [8, 1, 6, 3, 10]
random = ["abc", 5, 10.2, False, [0, 20, True]]

# La forma de acceder a los elementos
nombres[2]  # "Tona"

nombres[-2] # "Mona"

# La forma de agregar elementos en la lista es con 'append'
nombres.append("Chapita")
print(nombres)  #['Mia', 'Haba', 'Tona', 'Mona', 'Lupita', 'Chapita']

# El método 'remove' elimina un elemento de una lista
nombres.remove("Lupita")
print(nombres) #['Mia', 'Haba', 'Tona', 'Mona', 'Chapita']

# Si el valor de 'remove' no existe devuelve un 'ValueError'


# Tuple

# Las tuplas son secuencias de elementos similares a las listas, la diferencias
# es que las tuplas no pueden ser modificadas directamente.

# se definen
colores = ("Rojo", "Azul", "Amarillo", "Verde", "Naranjo")

# La forma de acceder a los elementos
colores[0]  # "Rojo"

colores[-1] # "Naranjo"

# Si se intenta modificar algun elementos de la tupla devolvera un  'TypeError'


# Dict

# Los diccionarios son estructuras que contienen una colección de elementosde la
# forma 'clave: valor', los que se separan por comas y encerrados en llaves

edades = {"Mia": 8, "Haba": 1, "Tona": 6, "Mona": 3, "Lupita": 10}

# Para acceder a un valor del diccionario se hace mediante la clave
edades["Haba"] # 1


