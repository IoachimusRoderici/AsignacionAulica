from os import path

directorio = path.dirname(path.abspath(__file__))

def get_path(*nombres: str) -> str:
    '''
    :param nombres: Una secuencia de nombres de directorios dentro de la carpeta
    assets. El último elemento de la lista puede ser el nombre de un archivo.

    :return: El path absoluto obtenido al unir el path de la carpeta assets con
    lal lista de nombres.
    '''
    return path.join(directorio, *nombres)
