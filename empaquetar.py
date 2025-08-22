from subprocess import run
from os import path
import os


raíz_del_repo = path.dirname(__file__)
assets = path.join(raíz_del_repo, 'assets')
archivo_main = path.join(raíz_del_repo, 'src', 'asignacion_aulica', 'main.py')
archivo_de_configuración_del_empaquetador = path.join(path.dirname(archivo_main), 'pysidedeploy.spec')

reemplazar_configuración = dict(
    title = 'Asignación Áulica',
    icon = path.join(assets, 'iconos', 'unrn.ico'),
    exec_directory = raíz_del_repo
)

apendear_configuración = dict(
    extra_args = f' --include-data-dir={assets}=assets'
)

run(
    [
        'pyside6-deploy',
        '--verbose',
        '--init',
        'src/asignacion_aulica/main.py'
    ],
    check = True
)

if not path.isfile(archivo_de_configuración_del_empaquetador):
    raise RuntimeError(f'Falta el archivo de configuración en {archivo_de_configuración_del_empaquetador}')

with open(archivo_de_configuración_del_empaquetador, 'r') as archivo:
    líneas_configuración = archivo.readlines()

for i, línea in enumerate(líneas_configuración):
    # Ignorar líneas vacías
    if len(línea) == 0 or línea.isspace():
        continue
    # Chequear si la primera palabra es uno de los parámetros a modificar
    primera_palabra = línea.split(maxsplit=1)[0]
    if primera_palabra in reemplazar_configuración:
        líneas_configuración[i] = f'{primera_palabra} = {reemplazar_configuración[primera_palabra]}\n'
    elif primera_palabra in apendear_configuración:
        líneas_configuración[i] = línea.rstrip() + apendear_configuración[primera_palabra] + '\n'
    
with open(archivo_de_configuración_del_empaquetador, 'w') as archivo:
    archivo.writelines(líneas_configuración)

run(
    [
        'pyside6-deploy',
        '--verbose',
        f'--config-file={archivo_de_configuración_del_empaquetador}'
    ],
    check = True
)
