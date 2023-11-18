import pickle

def deserializar(nombre_objeto):
    """
    La función deserializar toma el nombre de un objeto, abre un archivo pickle correspondiente y devuelve el objeto deserializado.

    :param nombre_objeto: El parámetro "nombre_objeto" es una cadena que representa el nombre del objeto que deseas deserializar.
    :return: el objeto deserializado.
    """
    try:
        path = "./temp/" + nombre_objeto + ".pickle"
        file = open(path, "rb")
        objeto = pickle.load(file)
        return objeto
    except Exception:
        return []