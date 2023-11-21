import pickle
import os

def serializar(nombre_objeto, objeto):
    
    """
    La función 'serializar' toma un objeto y lo guarda como un archivo pickle con un nombre dado en el directorio "./temp".

    :param nombre_objeto: El parámetro "nombre_objeto" es una cadena que representa el nombre del objeto que deseas serializar. Se utilizará como parte del nombre de archivo al guardar el objeto serializado.
    :param objeto: El parámetro objeto es el objeto que deseas serializar. Puede ser cualquier objeto de Python, como una lista, diccionario, instancia de clase, etc.
    """
    try:
        if not os.path.exists("./temp"):
            os.makedirs("./temp")

        path = "./temp/" + nombre_objeto + ".pickle"
        pickle_file = open(path, 'wb')
        pickle.dump(objeto, pickle_file)
    except Exception:
        print("Algo salio mal al serializar")
        return