# Base de Datos - SQLite

Esta carpeta contiene la Query para la generación de la Base de Datos, así como
también el archivo binario de la misma (sin datos).

Solamente la Query SQL debe formar parte del programa final, ya que por medio de
la misma se creará la base de datos al ejecutar por primera vez el programa.

La estructura de la misma contiene las siguientes tablas con sus respectivas columnas:

- Edificios:
    - <u>Edificio</u>: Nombre único de edificio `TEXT`.
    - Día: Contiene el horario de apertura y cierre correspondiente en formato `TEXT` `"HH:MM-HH:MM"`.
- Aulas:
    - <u>Aula</u>: Nombre de aula `TEXT`.
    - <u>Edificio</u>: ref. a nombre de edificio (`TEXT`).
    - Día: Contiene el horario del día correspondiente en formato `TEXT` `"HH:MM-HH:MM"`.
- Aulas Dobles:
    - <u>Primera</u>: ref. a nombre de primera aula a vincular (`TEXT`).
    - <u>Segunda</u>: ref. a nombre de segunda aula a vincular (`TEXT`).
- Carreras:
    - <u>Carrera</u>: Nombre único de carrera `TEXT`.
    - Preferencia de Edificio: ref. a nombre de edificio para preferencia (`TEXT`).
- Materias:
    - <u>Código</u>: Código de la materia `TEXT`.
    - <u>Nombre</u>: Nombre de la materia `TEXT`.
    - Comisión: Nombre de la comisión `TEXT`.
    - Año: Número de año dentro de la carrera `INTEGER`.
    - Carrera: ref. a nombre de la carrera `TEXT`.
- Equipamientos:
    - <u>Equipamiento</u>: Nombre [único] del equipamiento `TEXT`, por ejemplo: `"Pizarra"`.
- Clases:
    - Materia: ref. a nombre de la materia `TEXT`.
    - Día: Día de la semana `TEXT`, `"Lunes"` a `"Domingo"`.
    - Horario: Contiene el horario en el que se cursará en formato `TEXT` `"HH:MM-HH:MM"`.
    - Equipamiento: nombres de equipamientos necesarios, separados por comas `TEXT`, por ejemplo `"Pizarra,Proyector"`

Tener en cuenta que el manejo, ingreso y validación de datos se hace por fuera, desde Python mismo.
