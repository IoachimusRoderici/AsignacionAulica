import pandas as pd
from frontend.universidad_exceptions import ElementoDuplicadoException

class Universidad:
    def __init__(self, 
        edificios=pd.read_excel("./src/asignacion_aulica/data/edificios.xlsx"), 
        aulas = pd.read_excel("./src/asignacion_aulica/data/aulas.xlsx")
    ):        
        self.edificios = edificios
        self.aulas = aulas


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

    def agregar_edificio(self, nombre_edificio:str): #TODO Invocar excepcion apropiada en caso de no agregar elemento.
        """
        Metodo para agregar un edificio a la universidad.
        #TODO hacer que se agregue el row generado al dataframe

        Parameters
        ----------
        nombre_edificio : str
            El nombre del edificio a agregar. Funciona como clave primaria.
        Returns
            None
        Throws:
            ElementoYaExistenteException , si se trata de agregar un edificio ya existente.
        """

        if nombre_edificio in self.nombres_edificios():
            raise(ElementoDuplicadoException("Ya existe un edificio con ese nombre"))
            return

        aux_dict = {self.edificios.columns[0]:nombre_edificio}
        for col in self.edificios.columns[1:-1]:
            aux_dict[col] = "9:00-23:00"
        aux_dict[self.edificios.columns[-1]] = "CERRADO"
        aux_row = pd.DataFrame([aux_dict])
        self.edificios = pd.concat([self.edificios, aux_row], ignore_index=True)


    def eliminar_edificio(self, id_edificio:str): #TODO implementar. Prohibir si aulas lo usan
        print("A IMPLEMENTAR")
    def modificar_edificio(self, row_edificio): #TODO implementar
        print("A IMPLEMENTAR")
    
    
    def modificar_edificio(self, nombre_edificio, columna_a_modificar, valor_nuevo):

        df[Fila_correcta]['Martes'] = valor_nuevo

    



    # Sector de aulas
    def columnas_aulas(self): # Retorna lista de columnnames
        return self.aulas.columns.tolist()
    def mostrar_aulas(self): # Retorna el dataframe de aulas
        return self.aulas
    def agregar_aula(self, row): #TODO implementar. Que no permita aulas huerfanas.
        print("A IMPLEMENTAR")
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


def main():
    uni = Universidad()

    for nombre in ["Agregable 1", "Agregable 2" , "Agregable 3"]:
        try:
            uni.agregar_edificio(nombre)
        except ElementoDuplicadoException:
            print("Elemento duplicado")

    print(uni.mostrar_edificios())

if __name__ == '__main__':
    main()






###### ZONA DE EXCEPCIONES. Despues arreglar con la importacion de paquetes and stuff

class ElementoDuplicadoException(Exception):
    """Excepcion lanzada cuando quiere agregarse a un dataframe un dato que ya existe."""
    def __init__(self, mensaje, elemento=None):
        super().__init__(mensaje)
        self.elemento = elemento
