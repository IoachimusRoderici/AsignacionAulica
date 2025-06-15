

import pandas as pd





class Universidad:
    def __init__(self, 
        edificios=pd.read_excel("./src/asignacion_aulica/data/edificios.xlsx"), 
        aulas = pd.read_excel("./src/asignacion_aulica/data/aulas.xlsx")
    ):
        
        self.edificios = edificios
        self.aulas = aulas

    def mostrar_edificios(self):
        print(self.edificios)

    def mostrar_aulas(self):
        print(self.aulas)

    def col_names_edificios(self):
        print(self.edificios.columns.tolist())
    
    def col_names_aulas(self):
        print(self.aulas.columns.tolist())




def main():
    uni = Universidad()
    uni.mostrar_edificios()
    uni.mostrar_aulas()
    uni.col_names_edificios()
    uni.col_names_aulas()


if __name__ == '__main__':
    main()