from os import path, environ

este_directorio = path.dirname(__file__)

# Calcular el path de la carpeta assets según el ambiente de ejecución:
if 'NUITKA_ONEFILE_DIRECTORY' in environ:
    # Ambiente empaquetado, hay que ir un directorio para arriba
    assets_path = path.abspath(path.join(este_directorio, '..', 'ass'))
else:
    # Ambiente de desarrollo, hay que ir dos directorios para arriba
    assets_path = path.abspath(path.join(este_directorio, '..', '..', 'ass'))

def get_path(*nombres: str) -> str:
    '''
    Devuelve el path absoluto de un archivo dentro de la carpeta assets.

    Usar esta función para cargar archivos de manera independiente del ambiente
    de ejecución (ambiente de desarrollo o ambiente empaquetado).

    :param nombres: Una secuencia de nombres de directorios dentro de la carpeta
    assets. El último elemento de la lista puede ser el nombre de un archivo.

    :return: El path absoluto obtenido al unir el path de la carpeta assets con
    la lista de nombres.
    '''
    return path.join(assets_path, *nombres)
