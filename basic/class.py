

class Perro:
    
    # Las funciones que comienzan con doble guión bajo '__' son funciones especiales
    # que tiene, una funcion especial
    
    # La funcion '__init__()', es una funcion especial que se llama cada vez que se
    # crea una instancia de la clase
    def __init__(self, nombre="sin nombre", edad=0):
        self.edad = edad
        self.nombre = nombre
    
    # Funcion de una clase
    def ladra(self):
        print(f"{self.nombre} dice: Guau Guau")




if __name__=="__main__":
    
    perro1 = Perro("Mia", 8)
    perro2 = Perro("Haba", 1)
    
    perro1.ladra()


    # Cualquier atributo de un objeto puede ser eliminado utilizando 'del'
    perro2.ladra()
    del perro2.nombre
    #perro2.ladra()

    # Tambien se puede eliminar el objeto con 'del'
    del perro2

    # Con el comando 'del perro2' lo que hace es eliminar el nombre, el objeto sigue
    # existiendo, si al objeto no se le asigna otro nombre se destruye automaticamente.
    # La destruccion de objetos sin referencia se le denomina recoleccion de basura.

    
