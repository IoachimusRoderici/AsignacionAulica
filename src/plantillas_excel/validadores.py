'''
En este módulo se definen validadores de datos para usar en las plantillas.

Los validadores de datos son operadores que excel usa para evitar que los
usuarios ingresen datos no válidos. Estos validadores no se ejecutan en nuestro
programa sino que son parte de excel.
'''
from openpyxl.worksheet.datavalidation import DataValidation

def opciones_válidas(*valores: str) -> DataValidation:
    '''
    Devuelve un validador que solamente acepta los valores pasados como argumentos.
    '''
    validador = DataValidation(
        type='list',
        formula1=','.join(valores),
        error = f'Por favor ingresar uno de los siguientes valores: {', '.join(valores)}.',
        errorStyle = 'warning',
        showErrorMessage = True,
        showDropDown = False # False significa True
    )
    return validador

día_de_la_semana = opciones_válidas('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
'''
Un validador que solamente acepta los días de la semana.
'''

no_cambiar_este_valor = DataValidation(
    type='list',
    formula1='',
    error = 'Por favor no modificar el valor de esta celda.',
    errorStyle = 'stop',
    showErrorMessage = True,
    showDropDown = True # True significa False
)
'''
Un validador que no acepta ningún valor.

Sirve para evitar que los usuarios modifiquen el contenido de una celda.
'''

año_del_plan_de_estudios = DataValidation(
    type='whole',
    operator='between',
    formula1=1,
    formula2=9,
    errorTitle = 'El dato ingresado no es válido.',
    error = 'El valor debe ser un año del plan de estudios.\n1, 2, 3, etc.',
    errorStyle = 'warning',
    showErrorMessage = True
)
'''
Un validador para la columna de "Año".

Solamente acepta los números naturales de un dígito.
'''

número_natural = DataValidation(
    type='whole',
    operator='greaterThanOrEqual',
    formula1=0,
    errorTitle = 'El dato ingresado no es válido.',
    error = 'El valor debe ser un número entero no negativo.',
    errorStyle = 'warning',
    showErrorMessage = True
)
'''
Un validador que solamente acepta números naturales (incluyendo el 0).
'''

horario = DataValidation(
    type='time',
    operator = 'between',
    formula1 = 0,
    formula2 = 1,
    error = 'Excel no reconoce el valor ingresado como un horario.',
    errorStyle = 'warning',
    showErrorMessage = True
)
'''
Un validador para horarios.
'''
