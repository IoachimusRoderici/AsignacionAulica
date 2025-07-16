'''
En este módulo se definen validadores de datos para usar en las plantillas.

Los validadores de datos son operadores que excel usa para evitar que los
usuarios ingresen datos no válidos. Estos validadores no se ejecutan en nuestro
programa sino que son parte de excel.
'''
from openpyxl.worksheet.datavalidation import DataValidation

no_cambiar_este_valor = DataValidation(type='list', formula1='')
'''
Un validador que no acepta ningún valor.

Sirve para evitar que los usuarios modifiquen el contenido de una celda.
'''
no_cambiar_este_valor.error = 'Por favor no modificar el valor de esta celda.'
no_cambiar_este_valor.showErrorMessage = True
no_cambiar_este_valor.showDropDown = True # True significa False

año_del_plan_de_estudios = DataValidation(type='whole', operator='between', formula1=1, formula2=9)
'''
Un validador para la columna de "Año".

Solamente acepta los números naturales de un dígito.
'''
año_del_plan_de_estudios.errorTitle = 'El dato ingresado no es válido.'
año_del_plan_de_estudios.error = 'El valor debe ser un año del plan de estudios.\n1, 2, etc.'
año_del_plan_de_estudios.showErrorMessage = True
año_del_plan_de_estudios.errorStyle = 'information'

número_natural = DataValidation(type='whole', operator='greaterThanOrEqual', formula1=0)
'''
Un validador que solamente acepta números naturales (incluyendo el 0).
'''
número_natural.errorTitle = 'El dato ingresado no es válido.'
número_natural.error = 'El valor debe ser un número entero no negativo.'
número_natural.showErrorMessage = True
número_natural.errorStyle = 'information'

def opciones_válidas(*valores: str) -> DataValidation:
    '''
    Devuelve un validador que solamente acepta los valores pasados como argumentos.
    '''
    validador = DataValidation(type='list', formula1=','.join(valores))
    validador.errorTitle = 'El dato ingresado no es válido.'
    validador.error = f'Las opciones válidas son: {', '.join(valores)}.'
    validador.showErrorMessage = True
    validador.showDropDown = False # False significa True
    return validador
