

import pandas as pd





class Universidad:
    def __init__(self, 
        edificios=pd.read_excel("./src/asignacion_aulica/data/edificios.xlsx"), 
        aulas = pd.read_excel("./src/asignacion_aulica/data/aulas.xlsx")
    ):
        
        self.edificios = edificios
        self.aulas = aulas

    # Sector de edificios:
    def col_names_edificios(self): # Retorna lista de columnnames
        print(self.edificios.columns.tolist())
    def mostrar_edificios(self): #TODO implementar, actualmente es un print
        print(self.edificios)
    def agregar_edificio(self, row_edificio): #TODO implementar
        print("A IMPLEMENTAR")
    def eliminar_edificio(self, id_edificio): #TODO implementar. Prohibir si aulas lo usan
        print("A IMPLEMENTAR")
    def modificar_edificio(self, row_edificio): #TODO implementar
        print("A IMPLEMENTAR")
    # Sector de aulas
    def col_names_aulas(self): # Retorna lista de columnnames
        print(self.aulas.columns.tolist())
    def mostrar_aulas(self): #TODO implementar, actualmente es un print
        print(self.aulas)
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
    uni.mostrar_edificios()
    uni.mostrar_aulas()
    uni.col_names_edificios()
    uni.col_names_aulas()


if __name__ == '__main__':
    main()