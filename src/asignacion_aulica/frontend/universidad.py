import pandas as pd
from datetime import time
import re

from asignacion_aulica.frontend.excepciones_universidad import *
from asignacion_aulica.get_asset_path import get_asset_path



class Universidad:
    def __init__(self, 
        df_list = pd.read_excel(get_asset_path('edificios_default/Universidad.xlsx'), sheet_name=None)
        #df_list = pd.read_excel("./src/assets/edificios_default/Universidad.xlsx", sheet_name=None)
    ):        
        
        self.edificios = df_list['Edificios']
        self.aulas = df_list['Aulas']


    # Sector de edificios:

    def columnas_edificios(self): 
        """
        Metodo que retorna lista de nombres de columnas, del dataframe de Edificios

        Parameters
        -None
        Returns
            La lista de columnas de los edificios
        TYPE
            List[str]
        """
        return self.edificios.columns.tolist()
        
    def mostrar_edificios(self):
        """
        Retorna el dataframe de los edificios instanciados

        Parameters
        -None
        Returns
            La lista de columnas de los edificios
        TYPE
            DataFrame
        """
        return self.edificios

    def nombres_edificios(self):
        """
        Metodo para mostrar los nombres de los edificios instanciados.
        Sirve para el menu dropdown al intentar crear aulas.

        Parameters
        -None
        Returns
            La lista de nombres de los edificios instanciados
        TYPE
            List[str]
        """
        return self.edificios.iloc[:,0].tolist()

    def agregar_edificio(self, nombre_edificio:str):
        """
        Metodo para agregar un edificio a la universidad.

        Parameters
        ----------
        nombre_edificio : str
            El nombre del edificio a agregar. Funciona como clave primaria.
        Returns
            None
        Throws:
            ElementoYaExistenteException , si se trata de agregar un edificio ya existente.
        """
        nombre_edificio = nombre_edificio.strip()
        if nombre_edificio == "":
            raise(ElementoInvalidoException("No se puede agregar un edificio sin nombre"))

        if nombre_edificio in self.nombres_edificios():
            raise(ElementoDuplicadoException("Ya existe un edificio con ese nombre"))

        aux_dict = {'Edificio':nombre_edificio}
        for col in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']:
            aux_dict[col] = "9:00-23:00"
        aux_dict['Domingo'] = "CERRADO"
        aux_row = pd.DataFrame([aux_dict])
        self.edificios = pd.concat([self.edificios, aux_row], ignore_index=True)

    def eliminar_edificio(self, nombre_edificio:str): #TODO Prohibir si hay aulas que usan el edificio
        """
        Metodo para eliminar un edificio existente de la universidad

        Parameters
        ----------
        nombre_edificio : str
            El nombre del edificio a eliminar. Funciona como clave primaria.
        Returns
            None
        Throws:
            ElementoNoExisteException, si se trata de borrar un edificio que no existe en sistema.
            EdificioTieneAulasException , si se trata de agregar un edificio ya existente.
        """
        if nombre_edificio in self.aulas['Edificio']:
            raise(ElementoTieneDependenciasException("Hay aulas que contienen este edificio, eliminacion cancelada."))
        if nombre_edificio not in self.nombres_edificios():
            raise(ElementoNoExisteException("El edificio que desea borrar no existe en el sistema."))
        
        self.edificios = self.edificios[self.edificios['Edificio'] != nombre_edificio].reset_index(drop=True)
    
    def modificar_edificio(self, nombre_edificio:str, columna_a_modificar:str, valor_nuevo:str):
        """
        Modifica el valor de una columna específica para el edificio dado.

        Parameters
        ----------
        nombre_edificio : str
            Nombre del edificio a modificar (clave primaria, debe estar en la primera columna).
        columna_a_modificar : str
            Nombre de la columna a modificar.
        valor_nuevo : str
            Valor nuevo a establecer en la celda correspondiente.
        
        Returns
        -------
        None
        Throws
            - ElementoInvalidoException , si se trata de ingresar algun parametro vacio.


        """

        if nombre_edificio=="":
            raise(ElementoInvalidoException("Debe ingresar un edificio a modificar."))
        if columna_a_modificar=="":
            raise(ElementoInvalidoException("Debe elegir el dia al que quiera modificar su horario."))
        if columna_a_modificar not in self.columnas_edificios():
            raise(ElementoInvalidoException(f"La columna que desea modificar ({columna_a_modificar}) no se encuentra entre los datos del edificio ({self.columnas_edificios()}.)"))
        if valor_nuevo=="":
            raise(ElementoInvalidoException("No se puede ingresar una cadena vacia como valor nuevo."))


        # Buscar la fila donde la primera columna (nombre de edificio) coincide
        filtro = self.edificios[self.edificios['Edificio'] == nombre_edificio]
        # Obtener el índice de esa fila
        index = filtro.index[0]
        # Modificar el valor
        self.edificios.at[index, columna_a_modificar] = valor_nuevo

    def modificar_horario_edificio(self, nombre_edificio:str, dia:str, 
        hora1:int, hora2:int, minuto1:int, minuto2:int):

        if (
            hora1 not in range(0,24) or
            hora2 not in range(0,24) or
            minuto1 not in range(0,60) or
            minuto2 not in range(0,60)
        ):
            raise(HorarioInvalidoException("Error: Los datos de horario deben estar en un rango de 0-23 horas y 0-59 minutos."))


        if time(hora1, minuto1) < time(hora2, minuto2):
            self.modificar_edificio(nombre_edificio, dia, f"{hora1}:{minuto1:02}-{hora2}:{minuto2:02}")
        else:
            raise(HorarioInvalidoException("La hora de cierre no puede ser menor que la de apertura"))

    def edificio_esta_cerrado(self, nombre_edificio:str, dia:str):
        filtro = self.edificios[self.edificios['Edificio'] == nombre_edificio]
        index = filtro.index[0]
        # Modificar el valor
        cadena = self.edificios.at[index, dia]
        return cadena=="CERRADO"


    def horario_segmentado_edificio(self, nombre_edificio:str, dia:str):

        filtro = self.edificios[self.edificios['Edificio'] == nombre_edificio]
        index = filtro.index[0]
        # Modificar el valor
        cadena = self.edificios.at[index, dia]
        if cadena=="CERRADO":
            pass
        matches = re.findall(r'\d+', cadena) 
        if len(matches)==4:
            return matches
        else:
            raise(HorarioInvalidoException("Error, no se puede parsear el horario: " + cadena))


    



    # Sector de aulas
    def columnas_aulas(self): # Retorna lista de columnnames
        return self.aulas.columns.tolist()
    def mostrar_aulas(self): # Retorna el dataframe de aulas
        return self.aulas
    def agregar_aula(self, identificador_aula:str , capacidad:int, edificio_aula:str): #TODO implementar. Que no permita aulas huerfanas.
        
        aux_dict = {col:None for col in self.columnas_aulas}
        aux_dict[self.columnas_aulas[0]] = identificador_aula    #   Primer columna es identificador aula. Escribo
        aux_dict[self.columnas_aulas[1]] = capacidad
        aux_dict[self.columnas_aulas[-1]] = edificio_aula        #   Ultima columna es edificio. Escribo.
        print("falta IMPLEMENTAR TODAVIA")

    def eliminar_aula(self, id_aula): #TODO implementar
        print("A IMPLEMENTAR")
    def modificar_aula(self, row_aula): #TODO implementar
        print("A IMPLEMENTAR")
    """Metodo para recuperar el horario de un aula.
    Si el valor es null en el aula, devuelve el del edificio.
    Si el edificio esta cerrado en ese horario, #TODO decidir que hacer"""
    def horario_aula_entrada(self, id_aula): #TODO
        print("A IMPLEMENTAR")
    def horario_aula_salida(self, id_aula): #TODO
        print("A IMPLEMENTAR")

################3
###############CARRERAS
#############3



def main():
    uni = Universidad()

    print("Edificios antes del eliminar:")
    print(uni.mostrar_edificios())

    try:
        for i in uni.horario_segmentado_edificio("Anasagasti 1", "Martes"):
            print(i)
    except Exception as e:
        print(e)


    print("Edificios despues del eliminar:")
    print(uni.mostrar_edificios())



if __name__ == '__main__':
    main()






