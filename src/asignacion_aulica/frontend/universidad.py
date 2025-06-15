import pandas as pd


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

    def agregar_edificio(self, nombre_edificio:str): #TODO agregar el row generado
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
        ## ACA CHEQUEO DE QUE OTRO EDIFICIO NO TENGA ESE NOMBRE

        if nombre_edificio in self.nombres_edificios:
            print("KABOOM, ACA DEBERIA TIRAR EXCEPCION")
            return

        aux_dict = {self.edificios.columns[0]:nombre_edificio}
        for col in self.edificios.columns[1:-1]:
            aux_dict[col] = "9:00-23:00"
        aux_dict[self.edificios.columns[-1]] = "CERRADO"
        aux_row = pd.DataFrame([aux_dict])
        self.edificios.loc[len(self.edificios)] = aux_row



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
    uni.agregar_edificio("Agregable 1")
    uni.agregar_edificio("Agregable 2")
    uni.agregar_edificio("Agregable 1")
    print(uni.mostrar_edificios())

if __name__ == '__main__':
    main()