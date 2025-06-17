# -*- coding: utf-8 -*-
"""
Funciones para la creación, apertura y guardado de archivos.
También importación y exportación.

@author: Cristian
"""

import flet as ft

#from universidad import Universidad


def nuevo_archivo(page: ft.Page, file_picker: ft.FilePicker):
    # Se instancia la "ventana de archivo".
    # file_picker = ft.FilePicker()
    
    # Función que se llama cuando se selecciona una ruta.
    def archivo_guardado(e):
        if file_picker.result != None and file_picker.result.path != None:
            ruta = file_picker.result.path
            
            # Se crea un archivo vacío.
            with open(ruta, "w") as f:
                f.write("")
    
    file_picker.on_result = archivo_guardado
    
    # Se ejecuta la función para abrir la ventana de archivo.
    file_picker.save_file(
        dialog_title="Guardar como...",
        file_name="Sin título.unrn",
        allowed_extensions=["unrn"],
    )

def abrir_archivo(page: ft.Page, file_picker: ft.FilePicker):
    # Función que se llama cuando se selecciona una ruta.
    def archivo_guardado(e):
        if file_picker.result != None and file_picker.result.path != None:
            ruta = file_picker.result.path
            
            # Se crea un archivo vacío.
            # with open(ruta, "w") as f:
            #     f.write("")
    
    file_picker.on_result = archivo_guardado
    
    # Se ejecuta la función para abrir la ventana de archivo.
    file_picker.save_file(
        dialog_title="Abrir archivo",
        file_name="",
        allowed_extensions=["unrn"],
    )

def guardar_archivo(page: ft.Page, file_picker: ft.FilePicker):
    # Se instancia la "ventana de archivo".
    # file_picker = ft.FilePicker()
    
    # Función que se llama cuando se selecciona una ruta.
    def archivo_guardado(e):
        if file_picker.result != None and file_picker.result.path != None:
            ruta = file_picker.result.path
            
            # Se crea un archivo vacío.
            with open(ruta, "w") as f:
                f.write("")
    
    file_picker.on_result = archivo_guardado
    
    # Se ejecuta la función para abrir la ventana de archivo.
    file_picker.save_file(
        dialog_title="Guardar como...",
        file_name="Sin título.unrn",
        allowed_extensions=["unrn"],
    )

def importar_archivo(page: ft.Page, file_picker: ft.FilePicker):
    # Función que se llama cuando se selecciona una ruta.
    def archivo_guardado(e):
        if file_picker.result != None and file_picker.result.path != None:
            ruta = file_picker.result.path
            
            # Se crea un archivo vacío.
            # with open(ruta, "w") as f:
            #     f.write("")
    
    file_picker.on_result = archivo_guardado
    
    # Se ejecuta la función para abrir la ventana de archivo.
    file_picker.save_file(
        dialog_title="Importar archivo",
        file_name="",
        allowed_extensions=["csv", "xlsx"],
    )

def exportar_archivo(page: ft.Page, file_picker: ft.FilePicker):
    # Función que se llama cuando se selecciona una ruta.
    def archivo_guardado(e):
        if file_picker.result != None and file_picker.result.path != None:
            ruta = file_picker.result.path
            
            # Se crea un archivo vacío.
            # with open(ruta, "w") as f:
            #     f.write("")
    
    file_picker.on_result = archivo_guardado
    
    # Se ejecuta la función para abrir la ventana de archivo.
    file_picker.save_file(
        dialog_title="Exportar archivo como...",
        file_name="",
        allowed_extensions=["csv", "xlsx"],
    )