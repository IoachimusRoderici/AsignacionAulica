CREATE TABLE IF NOT EXISTS "Edificios" (
	"Edificio"	TEXT NOT NULL UNIQUE,
	"Preferencia"	TEXT NOT NULL DEFAULT True,
	"Lunes"	TEXT DEFAULT NULL,
	"Martes"	TEXT DEFAULT NULL,
	"Miercoles"	TEXT DEFAULT NULL,
	"Jueves"	TEXT DEFAULT NULL,
	"Viernes"	TEXT DEFAULT NULL,
	"Sabado"	TEXT DEFAULT NULL,
	"Domingo"	TEXT DEFAULT NULL,
	PRIMARY KEY("Edificio")
)

CREATE TABLE IF NOT EXISTS "Aulas" (
	"Aula"	TEXT NOT NULL,
	"Edificio"	TEXT NOT NULL,
	"Capacidad"	INTEGER NOT NULL DEFAULT 0,
	"Lunes"	TEXT DEFAULT NULL,
	"Martes"	TEXT DEFAULT NULL,
	"Miercoles"	TEXT DEFAULT NULL,
	"Jueves"	TEXT DEFAULT NULL,
	"Viernes"	TEXT DEFAULT NULL,
	"Sabado"	TEXT DEFAULT NULL,
	"Domingo"	TEXT DEFAULT NULL,
	"Equipamiento"	TEXT DEFAULT NULL,
	PRIMARY KEY("Aula","Edificio"),
	FOREIGN KEY("Edificio") REFERENCES "Edificios"("Edificio")
);

CREATE TABLE IF NOT EXISTS "Aulas Dobles" (
	"Nombre"	TEXT NOT NULL,
	"Primera_Edificio"	TEXT NOT NULL,
	"Primera_Aula"	TEXT NOT NULL,
	"Segunda_Edificio"	TEXT NOT NULL,
	"Segunda_Aula"	TEXT NOT NULL,
	PRIMARY KEY("Primera_Edificio","Segunda_Edificio","Segunda_Aula","Primera_Aula"),
	FOREIGN KEY("Primera_Aula") REFERENCES "Edificios"("Edificio") ON UPDATE CASCADE,
	FOREIGN KEY("Primera_Edificio") REFERENCES "Aulas"("Aula") ON UPDATE CASCADE,
	FOREIGN KEY("Segunda_Aula") REFERENCES "Edificios"("Edificio") ON UPDATE CASCADE,
	FOREIGN KEY("Segunda_Edificio") REFERENCES "Aulas"("Aula") ON UPDATE CASCADE
)

CREATE TABLE IF NOT EXISTS "Carreras" (
	"Carrera"	TEXT NOT NULL,
	"Preferencia de Edificio"	TEXT NOT NULL,
	PRIMARY KEY("Carrera"),
	FOREIGN KEY("Preferencia de Edificio") REFERENCES "Edificios"("Edificio")
)

CREATE TABLE IF NOT EXISTS "Equipamientos" (
	"Equipamiento"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Equipamiento")
)

CREATE TABLE IF NOT EXISTS "Materias" (
	"ID"	INTEGER NOT NULL,
	"Codigo"	TEXT NOT NULL,
	"Nombre"	TEXT NOT NULL,
	"Carrera"	TEXT,
	"Año"	INTEGER NOT NULL,
	"Duracion"	TEXT NOT NULL DEFAULT Cuatrimestral,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Carrera") REFERENCES "Carreras"("Carrera") ON UPDATE CASCADE
)

CREATE TABLE IF NOT EXISTS "Docentes" (
	"Docente"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("Docente")
)

CREATE TABLE IF NOT EXISTS "Clases" (
	"ID"	INTEGER NOT NULL,
	"Materia"	INTEGER NOT NULL,
	"Carrera"	TEXT NOT NULL,
	"Dia"	TEXT NOT NULL,
	"Horario"	TEXT NOT NULL,
	"Virtual"	TEXT NOT NULL DEFAULT "False",
	"Cantidad de Alumnos"	INTEGER,
	"Equipamiento"	TEXT,
	"Tipo"	TEXT NOT NULL DEFAULT "Teórica",
	"Promocionable"	TEXT NOT NULL DEFAULT "True",
	"Docente"	TEXT NOT NULL,
	"Auxiliar"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Carrera") REFERENCES "Carreras"("Carrera") ON UPDATE CASCADE,
	FOREIGN KEY("Materia") REFERENCES "Materias"("ID") ON UPDATE CASCADE
)
